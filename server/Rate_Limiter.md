# Rate Limiter (처리율 제한 장치)

## 정의
- 미리 정해진 허용량 만큼의 요청만 처리하고, 이후의 요청은 거부하는 기법
- 목적
    - 급격히 폭증하는 트래픽에 자원(CPU/Mem/Connection 등)이 고갈되어 서비스가 죽지 않도록 방어
    - 특정 사용자 별로 가능한 요청량을 제어 (비즈니스 목적 등)

## 구현 방법
### Token Bucket
- 버킷을 만들고, 주기적으로 정해진 양의 토큰을 채우며 사용
- 동작 예시
    - 요청이 들어왔을 때 토큰 상태 확인(GET) -> 리필양 계산(Compute) -> 토큰 차감하여 업데이트(SET) 수행
    - 리필양을 주기마다 계산하는 대신 효율성을 위해 요청 인입 시점에 계산하는 구현법을 많이 씀
- 장점
    - 일시적으로 트래픽이 급증해도 허용된 처리량만큼의 처리를 보장
    - 메모리 효율이 좋음
- 단점
    - 분산 환경에서의 구현 복잡도가 올라감
        - 한 트랜잭션에 조회와 업데이트가 포함되므로 여러 서버에서 동시에 실행되면 Race Condition 발생 가능
        - 이러한 상황을 막기 위해 원자성 보장을 위한 별도 처리가 필수
        - ex: 아래와 같은 Redis Lua Script를 수행
            ```Lua
            -- keys[1]: rate limit key (예: "rate_limit:user_123")
            -- argv[1]: 버킷 용량 (capacity)
            -- argv[2]: 초당 토큰 충전 속도 (refill rate)
            -- argv[3]: 현재 시간 (now)
            -- argv[4]: 요청 토큰 수 (1개)

            local key = KEYS[1]
            local capacity = tonumber(ARGV[1])
            local rate = tonumber(ARGV[2])
            local now = tonumber(ARGV[3])
            local requested = tonumber(ARGV[4])

            -- 1. 현재 상태 가져오기 (값이 없으면 초기화)
            local last_refilled = tonumber(redis.call("HGET", key, "last_refilled"))
            local tokens = tonumber(redis.call("HGET", key, "tokens"))

            if last_refilled == nil then
            last_refilled = now
            tokens = capacity
            end

            -- 2. 토큰 리필 계산 (시간 차이 * 리필 속도)
            local delta = math.max(0, now - last_refilled)
            local filled_tokens = math.min(capacity, tokens + (delta * rate))

            -- 3. 요청 처리 가능 여부 확인
            local allowed = false
            if filled_tokens >= requested then
            filled_tokens = filled_tokens - requested
            allowed = true
            
            -- 상태 업데이트 (원자적 실행)
            redis.call("HSET", key, "last_refilled", now, "tokens", filled_tokens)
            -- 키 만료 시간 설정 (메모리 관리, 버킷이 가득 차는 시간 정도)
            redis.call("EXPIRE", key, math.ceil(capacity / rate) * 2)
            end

            return allowed
            ```
### Fixed Window Counter
- 고정된 간격마다 요청 횟수를 카운팅
- 동작 예시
    - 초당 10회 처리율을 보장하고 싶다면, EXPIRE가 1초인 key 생성 후 Redis INCR을 통해 증가시키고 10이 될 때부터 요청 거부
- 장점
    - 구현이 매우 단순함 (분산 환경에서도 Redis INCR만 써도 구현이 가능)
    - 메모리 효율이 좋음
- 단점
    - Boundary Issue 발생 가능: 윈도우의 경계 지점에서 요청이 폭증하면 허용량의 2배 가까운 요청이 통과될 수 있음

### Sliding Window Counter
- 현재 윈도우의 요청 수, 이전 윈도우의 요청 수를 가중치에 따라 합산
- 동작 예시
    - 10:00에 80개, 10:01에 20개 카운터 값을 가지고 현재 시간은 10:01:15라면?
    - 80 * (45/60) + 20 = 80 으로 카운터를 계산
- 장점
    - 윈도우 경계 문제가 어느정도 완화
    - 메모리 효율이 좋음
- 단점
    - 균등 분포를 가정하므로, 특정 시점에 요청이 몰린 거면 정확한 결과값이 나오지 않음

### 나머지
- Leaky Bucket, Sliding Window Log 등의 방식도 있지만 위 알고리즘들에 비해 잘 사용하지 않음

## 언제 무엇을 사용?

- 정확도가 크게 중요하지 않고, 단순하게 구현하고 싶다면 Fixed Window
- 트래픽 버스트에 대응하고 싶다면 Tocket Bucket
- 트래픽 버스트에 대응하며, 성능 이점도 누리고 싶다면 복합 대안인 Sliding Window Counter
