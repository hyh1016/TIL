# Redis의 Atomicity - Transaction, Lua Script, Lock

## Redis에서 데이터 정합성 보장하기

- Redis가 싱글 스레드라는 것이 모든 데이터 정합성을 보장해준다는 의미는 (당연히) 아님
- ‘하나의 명령이라면’ 원자적으로 실행됨을 보장하지만 ‘여러 개 명령’이라면 보장하지 않음
- 그러므로 서버에서 ‘동시에 이루어져야 하는 여러 개의 명령’을 레디스로 전송할 때 명령들 사이에 이들과 충돌하는 다른 명령이 실행되면 정합성이 깨질 수 있음
- 이러한 상황을 예방하기 위해 레디스에서는 여러 도구를 제공
    - **Transaction**: 충돌(낙관적 락)을 이용
    - **Lua Script**: 스크립트 구조의 명령 실행
    - **Lock**: 특정 자원에 대한 권한(Lock)을 획득

## Transaction

- 다른 DB들의 트랜잭션과 마찬가지로 일괄 반영되거나 그렇지 않아야 할 명령들(All or Nothing)을 일괄적으로 수행하기 위한 기능

### 사용 방법

- `WATCH`, `MULTI`, `EXEC` 3가지 명령을 이용한 낙관적 락 구현
- `WATCH {key}` : 특정 키의 변경 여부를 감시
    - WATCH 시점부터 EXEC 호출 전까지 감시 중인 키의 변경이 일어나면 해당 트랜잭션은 즉시 취소(Abort)됨
- `MULTI`: 트랜잭션의 실행(start transaction). 해당 시점 이후의 명령어는 즉시 실행되지 않고 큐에 적재
- `EXEC`: 큐에 담긴 명령을 일괄 실행(commit)
- `UNWATCH`: 감시 해제. 트랜잭션을 하지 않을 때 직접호출 하거나, `EXEC` 호출 또는 트랜잭션 중 클라이언트와 연결이 종료되면 자동으로 호출됨
- 보통 아래와 같은 흐름으로 실행함
    1. 트랜잭션에서 정합성을 보장해야 할 데이터를 `WATCH` 시작
    2. `GET`을 통해 현재 키 값을 읽은 뒤 필요한 비즈니스 로직이 있다면 수행
    3. `MULTI`로 트랜잭션을 선언한 뒤
    4. 일괄 반영할 (데이터 변경) 명령을 실행해 큐에 적재시키고
    5. `EXEC`을 통해 일괄 반영

### 중간에 문제가 생기면?

1. 명령어를 큐에 쌓는 도중 명령어의 유효성 검증에 실패하거나 서버 자체의 문제로 실패하면?
    - 트랜잭션 실행 자체를 거부하고 에러를 반환
2. EXEC을 호출하여 일괄 실행하는 도중에 잘못된 명령어가 있어 실행에 실패하면?
    - **실패한 명령어를 제외한 나머지 명령은 정상 실행함**
    - 왜 이렇게 동작할까? 레디스는 ‘단순함’과 ‘고성능’이 설계 철학임. 롤백은 이 철학에 위배되는 행위이기 때문
    - 대신 각 명령의 성공/실패 여부를 리스트에 담아 클라이언트에게 제공함 (클라이언트에게 일부 실패에 대한 보상 로직을 수행할 책임을 위임한다고 볼 수 있음)

## Lua Script

- **핵심: 원자적으로 실행되어야 할 복잡한 로직을 스크립트로 짜서 Redis 내부로 던짐**
- Lua Script 자체도 Redis 입장에서는 ‘하나의 스크립트 실행’이라는 단일 명령이기 때문에 원자적으로 실행됨

### 사용 방법

- `EVAL {script} {numkey} [{key1} {key2} ...] [{arg1} {arg2} ...]`
    - script: 실행할 Lua Script 문자열 (파일명 같은 게 아니라 문자열!)
    - 키 개수(num key): 이후 뒤따라오는 인자 중 키의 개수를 명시
    - 키 (KEYS): 키의 이름들. 스크립트 내에서는 KEY[N]으로 사용
    - 인자 (ARGV): 스크립트에서 사용할 인자 값들. 스크립트 내에서는 ARGV[N] 으로 사용
- `EVALSHA {hash}`
    - 위의 EVAL 방식은 스크립트가 너무 길면 네트워크 대역폭을 낭비한다는 단점이 있음
    - 이 방식은 위 단점을 보완하기 위해 미리 레디스에 스크립트를 캐싱해두고 해시값만 전달하여 실행

### 스크립트 내부에서 레디스 명령어를 호출하는 방법

- `redis.call()`: 명령어를 실행하다 런타임 에러(예: 문법 오류)가 발생하면, 에러를 즉시 클라이언트에게 반환하고 스크립트 실행을 중단
- `redis.pcall()`: 에러가 발생하더라도 클라이언트에게 반환하는 대신 스크립트 내부에서 자체적으로 처리

### 유의사항

- 스크립트 내부에서 call 명령을 통해 키를 동적 생성하지 말고, 레디스에서 생성해 인자로 전달하도록 하는 편이 안전함
- 스크립트는 최대한 재사용 가능하도록 하는 편이 좋은데, 레디스에서 실행되는 스크립트들을 캐싱하기 때문. 따라서, 변경되는 부분은 최대한 ARGV로 분리할 것

## (Distributed) Lock

- **핵심: Redis를 자물쇠 저장소로 활용해, 특정 자원에 대한 접근 권한을 획득한 스레드만 외부 로직을 수행**

### 사용 방법

- 락 획득: `SET {key} {unique_id}  NX EX {ttl}`
    - unique id: 락을 획득한 클라이언트를 식별하기 위한 아이디로, 다른 클라이언트에서 락 해제를 할 수 없게 하기 위함
    - NX: 키가 존재하지 않을 때에만 설정
    - EX: 만료 시간을 설정
- 락 해제: Lua Script (GET key 후 unique_id가 자신의 아이디이면 DEL)

### 라이브러리 사용을 권장

- 직접 구현하는 경우는 잘 없고, **Redisson**과 같은 분산 락 기능을 지원하는 라이브러리를 사용해서 구현
- Redisson의 경우 위 사용 방법처럼 단순한 락 획득(Simple Lock)뿐만이 아닌 공정 락(Fair lock), 재진입 가능한 락(Reentrant Lock)과 같은 다양한 락 타입을 제공
    - Fair lock: 모든 클라이언트가 공평하게 락을 부여받음
    - Reentrant Lock: 현재 사용 중인 클라이언트가 락을 중첩 획득할 수 있으며 중첩 횟수를 기록
- 분산 락은 데드락, 성능 이슈 등의 문제가 많으니 바퀴를 재발명하기보다는 잘 만들어진 라이브러리를 사용할 것을 권장

### Redlock

- 레디스 노드가 다수 개일 때, 단순 락(SET-NX-EX) 방식은 아래의 문제가 발생할 수 있음
    - 마스터 노드가 죽어 새 마스터를 선출하기 전 락 정보가 유실되면 다른 클라이언트가 동일 락을 획득할 수도 있음
    - 네트워크 파티션으로 인해 노드가 여러 그룹으로 분리되었을 때(Split bran), 각 그룹에서 서로 다른 클라이언트가 락을 획득할 수도 있음
- 락은 Critical Section에 한 번에 하나의 스레드만 접근할 수 있도록 하는 것을 전제로 하므로, 위 상황은 치명적
- 따라서 노드가 다수 개일 때는 SET 락 패턴을 사용하는 대신 Redlock 알고리즘 사용을 권장하며, Redisson 같은 라이브러리에서는 이를 이미 지원

### 유의사항

- 데드락에 걸리지 않도록 유의해야 함. 반드시 동일 순서로 락을 획득하도록 할 것
- 크리티컬 섹션을 최소화하여 락 경합을 최소화해야 성능 저하를 줄일 수 있음
- 노드가 여러 개라면 Split brain 문제에 유의해야 함

## 언제 무엇을 사용할까?

### Redis Transaction: 유저 간 포인트 이체 시스템

- 상황: A의 포인트를 차감하고 B의 포인트를 증가하는 로직을 수행해야 함
- 아래와 같이 코드를 작성할 수 있음 (Java)
    
    ```java
    import org.springframework.data.redis.core.RedisOperations;
    import org.springframework.data.redis.core.SessionCallback;
    import org.springframework.data.redis.core.StringRedisTemplate;
    import org.springframework.stereotype.Service;
    
    import java.util.Arrays;
    import java.util.List;
    
    @Service
    public class PointService {
    
        private final StringRedisTemplate redisTemplate;
    
        public PointService(StringRedisTemplate redisTemplate) {
            this.redisTemplate = redisTemplate;
        }
    
        public boolean transferPoint(String userA, String userB, int amount) {
            List<Object> txResults = redisTemplate.execute(new SessionCallback<List<Object>>() {
                @Override
                public List<Object> execute(RedisOperations operations) {
                    String keyA = "point:" + userA;
                    String keyB = "point:" + userB;
    
                    // 1. A와 B의 키를 감시(WATCH) 시작
                    operations.watch(Arrays.asList(keyA, keyB));
    
                    // 2. 값 조회 및 검증 (여기서는 A의 잔고가 충분한지 확인)
                    String currentPointA = (String) operations.opsForValue().get(keyA);
                    if (currentPointA == null || Integer.parseInt(currentPointA) < amount) {
                        operations.unwatch(); // 잔고 부족 시 감시 해제
                        return null; // 로직 중단
                    }
    
                    // 3. 트랜잭션 시작 (MULTI)
                    operations.multi();
    
                    // 4. 커맨드 예약 (실제 실행은 EXEC 시점에 됨)
                    operations.opsForValue().decrement(keyA, amount);
                    operations.opsForValue().increment(keyB, amount);
    
                    // 5. 트랜잭션 실행 (EXEC)
                    return operations.exec(); 
                }
            });
    
            // 결과가 비어있다면 WATCH 중인 키가 변경되어 트랜잭션이 실패한 것
            return txResults != null && !txResults.isEmpty();
        }
    }
    ```
    
- Redis에서는 아래와 같은 명령이 실행됨
    
    ```bash
    # 1. 감시 시작 (operations.watch)
    WATCH point:userA point:userB
    
    # 2. 클라이언트 측 검증을 위한 데이터 조회 (operations.opsForValue().get)
    GET point:userA
    # -> (이 시점에 Java 애플리케이션으로 값이 반환되어 if문 로직이 평가됨)
    
    # 3. 트랜잭션 시작 (operations.multi)
    MULTI
    
    # 4. 커맨드 큐잉 (decrement, increment) - 즉시 실행되지 않고 QUEUED 응답을 받음
    DECRBY point:userA 1000
    INCRBY point:userB 1000
    
    # 5. 트랜잭션 실행 (operations.exec)
    EXEC
    ```
    
- 왜 트랜잭션을 사용할까?
    - Lua Script: 위 상황은 충돌이 잦은 상황은 아니기 때문에 Lua를 쓰는 것은 불필요하게 복잡도 증가와 성능 저하를 일으킴
    - Lock: 마찬가지로 충돌이 적은 상황에서 락의 획득/해제 비용을 감당할 이유가 없음

### Lua Script: 선착순 쿠폰 발급 이벤트의 쿠폰 재고 감소

- 한정된 자원에 대한 엄청난 접근이 발생하며 초고도 경합이 발생
- 쿠폰 발급을 위해서는 재고 조회(GET) → 검증(재고 > 0) → 재고 감소(DECR) 및 유저-재고 연결(SADD) 흐름으로의 로직 처리가 필요
- 아래와 같이 코드를 작성할 수 있음 (Java)
    
    ```java
    import org.springframework.data.redis.core.StringRedisTemplate;
    import org.springframework.data.redis.core.script.DefaultRedisScript;
    import org.springframework.stereotype.Service;
    
    import java.util.Arrays;
    import java.util.List;
    
    @Service
    public class CouponService {
    
        private final StringRedisTemplate redisTemplate;
        private final DefaultRedisScript<Long> couponScript;
    
        public CouponService(StringRedisTemplate redisTemplate) {
            this.redisTemplate = redisTemplate;
            
            // Lua 스크립트 정의: 재고(KEYS[1]) 확인 후 감소, 유저(ARGV[1])를 Set(KEYS[2])에 추가
            String script = "local stock = tonumber(redis.call('GET', KEYS[1])) " +
                            "if stock > 0 then " +
                            "   local added = redis.call('SADD', KEYS[2], ARGV[1]) " +
                            "   if added == 1 then " + // 중복 발급 방지
                            "       redis.call('DECR', KEYS[1]) " +
                            "       return 1 " + // 발급 성공
                            "   else " +
                            "       return -1 " + // 이미 발급받은 유저
                            "   end " +
                            "else " +
                            "   return 0 " + // 재고 소진
                            "end";
            
            this.couponScript = new DefaultRedisScript<>(script, Long.class);
        }
    
        public String issueCoupon(String couponId, String userId) {
            List<String> keys = Arrays.asList("coupon_stock:" + couponId, "coupon_users:" + couponId);
            
            // 스크립트 실행 (Redis 서버 내부에서 C언어급 속도로 한 번에 처리됨)
            Long result = redisTemplate.execute(couponScript, keys, userId);
    
            if (result == 1) return "쿠폰 발급 성공";
            if (result == -1) return "이미 발급받으셨습니다.";
            return "선착순 마감되었습니다.";
        }
    }
    ```
    
- Redis에서는 아래와 같은 명령이 실행됨
    
    ```bash
    EVAL "local stock = tonumber(redis.call('GET', KEYS[1])) if stock > 0 then ..." 2 coupon_stock:123 coupon_users:123 user_1001
    ```
    
- 위 스크립트를 통해 Redis 엔진 내에서는 아래와 같은 명령이 일괄 실행됨
    
    ```bash
    GET coupon_stock:123
    SADD coupon_users:123 user_1001
    # SADD의 결과가 1(성공)이면 이어서 실행
    DECR coupon_stock:123
    ```
    
- 왜 Lua Script를 사용할까?
    - Transaction: 고경합에 의해 수많은 트랜잭션 실패가 발생하게 되며, 이들의 재시도로 인해 애플리케이션 서버(레디스 클라이언트) 측의 자원이 고갈됨 (retry storm)
    - Lock: 트래픽 수만큼의 요청이 락을 얻기 위해 대기하게 되고, 타임아웃/커넥션 고갈로 인해 서버에 부하가 발생함

### Distributed Lock: 외부 PG사(결제 대행사) 연동을 통한 결제 승인 및 DB 주문 상태 업데이트

- 레디스가 특정 공유자원의 정합성 보장을 위한 락 용도로 사용되는 케이스
- 아래와 같이 코드를 작성할 수 있음 (java)
    
    ```java
    import org.redisson.api.RLock;
    import org.redisson.api.RedissonClient;
    import org.springframework.stereotype.Service;
    
    import java.util.concurrent.TimeUnit;
    
    @Service
    public class PaymentService {
    
        private final RedissonClient redissonClient;
        private final PgApiService pgApiService; // 외부 통신 서비스 (가정)
        private final OrderRepository orderRepository; // JPA Repository (가정)
    
        public PaymentService(RedissonClient redissonClient, PgApiService pgApiService, OrderRepository orderRepository) {
            this.redissonClient = redissonClient;
            this.pgApiService = pgApiService;
            this.orderRepository = orderRepository;
        }
    
        public void processPayment(String orderId, String userId, int amount) {
            String lockKey = "lock:payment:order:" + orderId;
            RLock lock = redissonClient.getLock(lockKey);
    
            try {
                // 락 획득 시도 (최대 5초 대기, 획득 후 10초 지나면 자동 해제)
                boolean isLocked = lock.tryLock(5, 10, TimeUnit.SECONDS);
                
                if (!isLocked) {
                    throw new RuntimeException("현재 결제가 진행 중이거나 처리량이 많습니다. 잠시 후 다시 시도해주세요.");
                }
    
                // --- 여기부터는 오직 1개의 스레드만 진입 가능한 안전 구역(Critical Section) ---
                
                // 1. DB에서 주문 상태 확인 (이미 결제되었는지 검증)
                Order order = orderRepository.findById(orderId).orElseThrow();
                if (order.isPaid()) {
                    throw new RuntimeException("이미 결제된 주문입니다.");
                }
    
                // 2. 외부 PG사 결제 API 호출 (시간이 꽤 소요되는 작업)
                pgApiService.approvePayment(orderId, userId, amount);
    
                // 3. DB에 결제 완료 상태 업데이트
                order.setPaid(true);
                orderRepository.save(order);
                
                // -------------------------------------------------------------------
    
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
                throw new RuntimeException("결제 락 획득 중 오류가 발생했습니다.", e);
            } finally {
                // 로직이 끝나면 반드시 락을 해제 (현재 스레드가 락을 보유하고 있을 때만 해제)
                if (lock.isLocked() && lock.isHeldByCurrentThread()) {
                    lock.unlock();
                }
            }
        }
    }
    ```
    
    - tryLock의 핵심은 최대 대기 시간을 명시하고, 획득하는 락의 TTL도 명시하는 것 (데드락, 대기에 의한 심각한 성능 저하 예방)
    - `try/finally` 블록을 활용해 어떤 예외가 발생하더라도 락이 반드시 해제(`unlock`)되도록 보장해야 함
- Redis에서는 아래와 같은 명령이 실행됨
    
    ```bash
    # 락 획득 (By Lua Script)
    EXISTS lock:payment:order:123
    
    # (락이 없다면)
    HSET lock:payment:order:123 UUID:threadId 1  # 락 획득 및 진입 횟수 1 기록
    PEXPIRE lock:payment:order:123 10000         # 데드락 방지를 위한 TTL(10초) 설정
    
    # 락이 이미 존재하여 획득에 실패한 경우
    SUBSCRIBE redisson_lock__channel:{lock:payment:order:123}
    
    # 락 해제 (By Lua Script)
    HEXISTS lock:payment:order:123 UUID:threadId
    # (자신이 소유한 락이 맞다면)
    HINCRBY lock:payment:order:123 UUID:threadId -1 # 진입 횟수 차감
    # (차감 결과 0이 되면 완전 해제)
    DEL lock:payment:order:123
    PUBLISH redisson_lock__channel:{lock:payment:order:123} 0  # "락 풀렸으니 다음 사람 가져가라"는 메시지 발행
    ```
    
- 왜 Distributed Lock을 사용할까?
    - Transaction, Lua Script: 이 기술들은 레디스 내부 데이터의 정합성 보장을 위한 것으로, 해당 사례처럼 외부 시스템(외부 API, RDBMS)의 정합성 보장을 위해 사용하는 것은 불충분

### 정리하자면…

- 동기화해야 할 로직이 **Redis 안에서만** 일어날 때
    - 충돌이 적다면 **Transaction**
    - 충돌이 많다면 **Lua Script**
- 동기화해야 할 로직에 **외부 통신이나 복잡한 DB 트랜잭션**이 포함되어 있다면 **Distributed Lock**

## 출처

[Transaction](https://redis.io/docs/latest/develop/using-commands/transactions/)

[Lua Script](https://redis.io/docs/latest/develop/programmability/)

[Lock](https://redis.io/glossary/redis-lock/)
