# Entity Manager

## Entity Manager

- JPA 기능을 제공하는 객체
- 내부에 DataSource(Database Connection)를 소유
- 애플리케이션 레벨의 가상 데이터베이스로 볼 수 있음
- Thread-safe하지 **않음**. 여러 스레드가 하나의 Entity Manager 객체를 공유하면 안 됨
- EntityManager와 달리 EntityManagerFactory는 생성 비용이 큰 객체로 애플리케이션 전체에서 단 한 번만 생성하고 공유해서 사용해야 함 (Singleton)

## Persistence Context (영속성 컨텍스트)

- 엔티티 매니저가 내부적으로 관리하는 엔티티 상태 보관소
- 엔티티 또한 객체이고, 기능이 수행되며 내부 값이 변경됨
- 영속성 컨텍스트는 엔티티의 최초 등록 시점의 상태를 **스냅샷**으로 저장하고, 데이터베이스에 반영하는 시점과 스냅샷을 비교해 쿼리를 실행함

### 엔티티 생명주기

- 영속성 컨텍스트를 기준으로 엔티티는 4가지 상태를 가질 수 있음
    1. 비영속(new/transient) - 아직 영속성 컨텍스트에 저장된 적 없음
    2. 영속(managed) - 영속성 컨텍스트에 저장되어 있음
    3. 준영속(detached) - 영속성 컨텍스트에 저장되었다가 분리됨
    4. 삭제(removed) - 엔티티가 삭제됨
- 식별자가 없다면 비영속 상태로 볼 수 있고, 식별자가 있다면 영속성 컨텍스트의 관리를 받는지 여부에 따라 영속과 준영속으로 나뉨. 삭제 상태는 DB에 반영될 때 delete 쿼리가 실행되는 상태를 말함

### 영속성 컨텍스트가 지원하는 기능

1. **1차 캐시**
    - 영속성 컨텍스트는 캐시의 역할을 함. 특정 엔티티를 조회하려고 할 때 1차 캐시에 해당 엔티티가 있다면 DB를 조회하지 않고 해당 엔티티를 반환함
    - 캐시 키는 식별자, 캐시 값은 엔티티 그 자체
2. **동일성 보장**
    - 영속성 컨텍스트에서는 같은 식별자를 가진 엔티티를 조회하면 항상 같은 객체를 반환함
3. **쓰기 지연**
    - 트랜잭션의 원자성에 기반한 기능으로, 모든 쓰기(insert/update/delete) 쿼리들을 트랜잭션의 커밋 시점에 수행되도록 함
    - 영속성 컨텍스트에 담기는 변경들이 트랜잭션 범위 안에서 이루어지기 때문에, 전부 반영하거나 롤백하거나 둘 중 하나이기 때문에 효율성을 위해 커밋 시점에 한 번에 반영하는 것
    - 유의할 점 - commit == 쓰기 지연 수행이 아님. 정확히는 커밋 이전에 수행하는 flush가 쓰기 지연 쿼리 수행을 유발하는 동작임. 커밋 시점이 아니더라도 flush를 호출해 지연된 쓰기 쿼리들을 실행할 수 있음
    - 유의할 점 - IDENTITY 식별자 전략을 사용하는 엔티티의 insert 시점에는 쓰기 지연 없이 바로 쿼리가 발생함. 기본 키 값을 획득하기 위함
4. **변경 감지**
    - 쓰기 쿼리가 수행될 시점에 엔티티의 스냅샷과 현재 상태를 비교해 변경을 반영하기 위한 쿼리들을 수행함
    - 변경 감지 또한 flush 시점에 수행
5. **지연 로딩**
    - 연관 관계인 엔티티를 일단 프록시로 가져왔다가 사용하는 시점에 조회 쿼리를 통해 로딩해오는 전략
