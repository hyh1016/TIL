# Thread-safe Collection

## 멀티 스레드 환경에서 컬렉션을 사용하는 방법

- **Synchronized Collection**
    - Vector
    - Hashtable
    - Collections 클래스의 synchronized 정적 생성자

## Synchronized Collection (동기화 컬렉션)

### Vector

- 모든 메서드가 synchronized 기반으로 구현된 List
- 스레드 세이프하지만 동기화가 필요하지 않은 경우에도 동기화를 해 성능 저하 발생

### Hashtable

- 모든 메서드가 synchronized 기반으로 구현된 Map
- 스레드 세이프하지만 동기화가 필요하지 않은 경우에도 동기화를 해 성능 저하 발생

### Collections의 synchronized List/Map/Set

- JDK 1.2에 추가
- 내부적으로 mutex 객체를 소유하며 synchronized block을 통해 기존 List/Map/Set의 동작을 wrapping
- 모든 메서드에서 동일 mutex를 사용하기 때문에 한 객체에서 한 번에 하나의 메서드만 수행 가능
- 여러 연산을 하나의 원자적 단위로 묶어야 하는 경우에는 이들을 다시 synchronized로 묶어야 함

### Concurrent Collections

- JDK 1.5에 추가
- 동시성을 위한 `java.util.concurrent` 패키지 내 컬렉션들
- `CopyOnWriteArrayList`
    - 쓰기 발생 시 락을 걸고 새로운 배열을 만들어 기존 배열을 대체
        - 쓰기 동작은 배열 복사라는 고비용 작업을 수반하기 때문에 쓰기가 많은 데이터 저장에는 알맞지 않을 수 있음
    - 쓰기에 고비용 동기화를 적용하는 대신 읽기는 Lock 없이도 동기화를 제공해 읽기 성능을 높임
- `CopyOnWriteArraySet`
    - 내부 구현은 `CopyOnWriteArrayList`와 동일하나 중복 방지만 적용
    - 마찬가지로 쓰기에 동기화를 적용하고 쓰기 성능을 낮추는 대신 읽기 성능을 높임
- `ConcurrentHashMap`
    - 테이블의 Bucket을 기준으로 Lock 또는 CAS(Compare-And-Set)을 적용
        - 이미 데이터가 있는 버킷인 경우 해당 버킷에만 Lock을 걸고 쓰기를 수행
        - 빈 버킷인 경우 CAS 알고리즘을 통해 Lock 없이 쓰기를 수행
- `ConcurrentLinkedQueue`
    - 락 없이 동작하는 non-blocking 알고리즘을 사용
    - LinkedList 기반

## Reference

- https://steady-coding.tistory.com/575
