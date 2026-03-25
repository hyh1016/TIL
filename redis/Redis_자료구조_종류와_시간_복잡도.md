# Redis 자료구조 종류와 시간 복잡도

## Redis의 주요 자료구조

### String

#### 정의

```bash
> SET user:1 "Alice"
OK

> GET user:1
"Alice"
```

- 가장 기본적인 key-vaule 자료구조
- **숫자**, 텍스트, 직렬화된 객체 등을 저장하는 데에 사용
    - INTEGER/NUMBER 같은 숫자 자료구조가 따로 없음
    - 대신 문자열 자료구조에 숫자를 저장할 수 있고 숫자 연산이 가능
        - 왜 이렇게 할까?
            - 인터페이스 단순화를 위함으로, 성능 이슈가 걱정되었으나 Redis 내부적으로 숫자로 표현 가능한 값이면 정수 형태로 압축하여 저장한다고 함
- **주요 Command:** `SET`, `GET`, `INCR`, `DECR`, `MSET`, `MGET`, `APPEND`, `STRLEN`

#### 사용처

- 캐싱 — 세션, HTML 문서, API 응답 등
- 카운터(INCR/DECR을 통한 증감 조작) — 좋아요, 조회수, 재고
- Rate Limiter (Fixed window)
- Feature Flag
- Distributed Lock

#### 시간 복잡도

- 단건 저장 및 조회: O(1)
- 다중 조회: O(N)

### Lists

#### 정의

```bash
> LPUSH mylist "apple"
(integer) 1

> RPUSH mylist "banana"
(integer) 2

> LRANGE mylist 0 -1   # 0부터 -1(마지막)까지 전체 조회
1) "apple"
2) "banana"
```

- 입력된 순서를 유지하는 연결 리스트(Linked List)
- 양 끝에 추가하거나 삭제(Pop)할 수 있어 리스트이자 스택, 큐처럼 활용이 가능
- 리스트의 왼쪽(`LPUSH`)이나 오른쪽(`RPUSH`)에 데이터를 밀어 넣고, 범위로 조회(`LRANGE`)
- **주요 Command:** `LPUSH`, `RPUSH`, `LPOP`, `RPOP`, `LRANGE`, `LINDEX`, `LTRIM`, `LLEN`

#### **사용처**

- 메시지 큐(Queue) — 대기열, 최근 검색어, 최근 방문 페이지 등의 타임라인
- 작업 스택(Stack)

#### 시간 복잡도

- 양 끝 삽입/삭제: O(1)
- 인덱스 접근: O(N)
- 범위 조회: O(N)

### Sets

#### 정의

```bash
> SADD post:100:likes "user:1" "user:2" # 유저 2명이 좋아요 클릭
(integer) 2

> SADD post:100:likes "user:1"          # 이미 존재하는 유저는 무시됨 (중복 불가)
(integer) 0

> SISMEMBER post:100:likes "user:2"     # user:2가 좋아요를 눌렀는지 확인
(integer) 1

> SMEMBERS post:100:likes               # 좋아요 누른 모든 유저 조회
1) "user:1"
2) "user:2"
```

- 순서가 없고 중복을 허용하지 않는 데이터 집합
- 교집합, 합집합, 차집합 등 집합 연산에 최적화
- 중복 없는 집합에 요소를 추가(`SADD`)하고, 전체 요소를 확인(`SMEMBERS`)
- **주요 Command:** `SADD`, `SREM`, `SISMEMBER`, `SMEMBERS`, `SINTER`, `SUNION`, `SDIFF`, `SCARD`

#### 사용처

- 고유 방문자(UV) 수 계산
- 태그 시스템
- 친구 추천(교집합/합집합 계산)

#### 시간 복잡도

- 추가/삭제/확인(SADD, SREM, SISMEMBER): O(1)
- 전체 조회(SMEMBERS), 집합 연산: O(N)

### Hashes

#### 정의

```bash
> HSET user:200 name "Bob" age "30" # 한 번에 여러 필드 저장
(integer) 2

> HGET user:200 name                # 특정 필드만 조회
"Bob"

> HINCRBY user:200 age 1            # 나이 1 증가
(integer) 31

> HGETALL user:200                  # 객체 전체 정보 조회
1) "name"
2) "Bob"
3) "age"
4) "31"
```

- 하나의 Key 안에 여러 개의 Field-Value 쌍을 가지는 구조
- 객체(Object)나 관계형 DB의 행(Row)을 표현하기 좋음
- **주요 Command:** `HSET`, `HGET`, `HMSET`, `HMGET`, `HGETALL`, `HDEL`, `HINCRBY`, `HKEYS`, `HVALS`

#### 사용처

- 사용자 프로필 데이터(이름, 나이, 이메일 등) 저장
- 상품의 속성 정보 등 객체(Object) 형태의 데이터 표현

#### 시간 복잡도

- 단일 필드 조작(HSET, HGET): O(1)
- 전체 필드 조회(HGETALL): O(N)

### Sorted Sets (ZSet)

#### 정의

```bash
> ZADD game:rank 1500 "PlayerA" 2000 "PlayerB" 1200 "PlayerC"
(integer) 3

> ZINCRBY game:rank 100 "PlayerA" # PlayerA의 점수를 100점 증가 (1600점 됨)
"1600"

> ZREVRANGE game:rank 0 2 WITHSCORES # 점수가 높은 순으로(1~3위) 점수와 함께 조회
1) "PlayerB"
2) "2000"
3) "PlayerA"
4) "1600"
5) "PlayerC"
6) "1200"
```

- Set과 유사하나 각 요소가 스코어(Score)라는 실수 값을 가지며 스코어를 기준으로 정렬되어 저장
- **주요 Command:** `ZADD`, `ZRANGE`, `ZREVRANGE`, `ZRANK`, `ZREVRANK`, `ZSCORE`, `ZINCRBY`, `ZREM`

#### 사용처

- 게임/서비스의 실시간 리더보드 (랭킹 시스템)
- 우선순위 대기열 (Priority Queue)
- Rate Limiter (Sliding Window)

#### 시간 복잡도

- 추가/삭제/업데이트(ZADD, ZREM): O(log N)
- 순위 기반 조회(ZRANGE): O(log N + M)

#### 왜 이런 시간복잡도가 나올까?

- Sorted Set은 데이터가 임계치 이하일 때는 ListPack, 이상일 때는 HashTable과 Skip List 라는 2개 자료구조로 데이터를 관리함
    - Skip List? 정렬된 양방향 연결 리스트(Linked List)를 기반으로 하되, 여러 층(Level)의 '고속도로'를 추가로 얹은 자료구조
- Skip List 사용 기준 조회 시 스코어 탐색 동작이 이진 탐색 트리(BST)와 유사하게 동작하기 때문에 약 O(logN)
- 추가/업데이트 시에는 해시 테이블에서 키를 찾아 바로 업데이트 하므로 O(1)
- 순위 기반 범위 조회 시에는 M개 데이터 조회 시 첫 번째 데이터 찾으면(O(logN)) 이후 데이터는 포인터 따라 M번 이동 하면서 찾으면 되기 때문에 O(logN + M)
- 집합 내 요소 수가 임계치(기본값: 128) 이하인 경우 이러한 관리 방식보다 ListPack(데이터 일렬 저장) 방식으로 조회하는게 더 효율적이어서 이렇게 설계됨 (ListPack의 조회 시간복잡도: O(N))

### Bitmaps

#### 정의

```bash
> SETBIT login:20260317 101 1 # 유저 ID 101번이 오늘 로그인함(1로 설정)
(integer) 0

> SETBIT login:20260317 250 1 # 유저 ID 250번 로그인
(integer) 0

> GETBIT login:20260317 101 # 유저 101번의 로그인 여부 확인
(integer) 1

> BITCOUNT login:20260317 # 오늘 로그인한 총 유저(비트가 1인) 수 계산
(integer) 2
```

- String 자료구조를 비트 단위로 다루는 논리적 자료구조
- 비트 플래그 형태로 사용
- 메모리 효율이 극도로 높음
- **주요 Command:** `SETBIT`, `GETBIT`, `BITCOUNT`, `BITOP`, `BITPOS`

#### 사용처

- 일간 활성 사용자(DAU, Daily Active Users) 체크
- 출석 체크 시스템
- Feature flag

#### 시간 복잡도

- 단일 비트 조작(SETBIT, GETBIT): O(1)
- 비트 카운트(BITCOUNT): O(N)

### HyperLogLogs

#### 정의

```bash
> PFADD visit:20260317 "ip:192.168.0.1" "ip:10.0.0.1" "ip:192.168.0.1"
(integer) 1 # 중복된 IP는 무시됨

> PFCOUNT visit:20260317 # 고유 방문자 수 추정치 확인
(integer) 2
```

- 대용량 데이터에서 고유한(Unique) 항목의 개수를 추정(Estimate)하는 확률형 자료구조
- 데이터가 아무리 많아도 최대 12KB의 메모리만 사용
- 표준 오차는 약 0.81%
- **주요 Command:** `PFADD`, `PFCOUNT`, `PFMERGE`

#### 사용처

- 대규모 트래픽 웹사이트의 전체 고유 방문자 수 계산
- 대규모 검색 엔진의 고유 검색어 수 추정

#### 시간 복잡도

- 추가 및 개수 추정(PFADD, PFCOUNT): O(1)

### Geospatial

#### 정의

```bash
> GEOADD seoul:stations 126.9780 37.5665 "CityHall" 127.0276 37.4979 "Gangnam"
(integer) 2

> GEODIST seoul:stations "CityHall" "Gangnam" km # 두 역 사이의 거리를 km 단위로 계산
"8.8256"

> GEOSEARCH seoul:stations FROMLONLAT 126.97 37.56 BYRADIUS 5 km # 지정 좌표 기준 5km 반경 내 검색
1) "CityHall"
```

- 위도(Latitude)와 경도(Longitude)를 저장
- 위치 기반 쿼리를 수행할 수 있음
- 내부적으로는 Sorted Set(ZSet)을 사용
- **주요 Command:** `GEOADD`, `GEODIST`, `GEOHASH`, `GEOPOS`, `GEOSEARCH`

#### 사용처

- 범위 탐색 — 특정 반경 내의 상점/친구 찾기
- 거리 계산 — 배달 앱의 라이더 위치 추적 및 거리 계산

#### 시간 복잡도

- 위치 추가(GEOADD): O(log N)
- 거리 계산(GEODIST): O(1) ~ O(log N)
- 반경 검색(GEOSEARCH): O(N + log M)

### Streams

#### 정의

```bash
> XADD telemetry * temp 25.4 humidity 60 # *를 사용하면 타임스탬프 기반 고유 ID 자동 생성
"1710685000000-0"

> XREAD COUNT 1 STREAMS telemetry 0-0 # 0-0(처음)부터 최대 1개의 메시지 읽기
1) 1) "telemetry"
   2) 1) 1) "1710685000000-0"
         2) 1) "temp"
            2) "25.4"
            3) "humidity"
            4) "60"
```

- Append-Only 방식의 로그(Log) 자료구조
- 메시지가 여러 소비자에게 신뢰 가능하게 브로드캐스팅되는 것을 보장
    - like Kafka
    - 카프카처럼 Consumer Group 기능도 제공
- **주요 Command:** `XADD`, `XREAD`, `XRANGE`, `XGROUP`, `XREADGROUP`, `XACK`, `XLEN`

#### 사용처

- 이벤트 브로커 (메시지 브로커)
- 대규모 로그 수집
- 이벤트 소싱

#### 시간 복잡도

- 데이터 추가(XADD): O(1)
- 데이터 읽기(XREAD): O(N)

#### vs Kafka

- 이미 카프카라는 아주 잘 만들어진, 동일한 역할을 수행하는 도구가 있음에도 왜 레디스는 이 Streams라는 걸 추가했을까?
- 우선 Redis pub/sub은 데이터 유실 위험이 있어 전달을 보장하고 싶다면 이걸 쓰면 안 됨
- Kafka는 초기 구축 비용이 방대함. 단순한 스트리밍 기능이 필요한 경우 배보다 배꼽이 커질 수 있음
- 또한, Kafka는 어찌됐든 디스크 기반임. Redis는 메모리 기반이므로 더 빠름

## 왜 이런 자료구조를 제공할까?

- **복잡한 연산은 Redis 서버에서 하기 위함 (극한의 성능 최적화)**
- 내부적으로는 데이터 사이즈 또는 요소 개수에 따라 사용하는 자료구조를 동적으로 바꾸기도 함 (Sorted Set 케이스)
