# Dirty Checking

### 정의

* Entity 기반으로 동작하는 ORM에서 객체의 상태 변화를 검사하여 데이터베이스에 반영하는 것
* 영속성(Persistence) 컨텍스트가 관리하는 Entity에만 적용된다.
  * Entity의 영속성은 다음과 같다.
    * DB에 반영되기 전 처음 생성된 Entity (비영속)
    * detach된 Entity (준영속)
    * DB에 반영된 Entity (영속)

### Flow

1. Entity 조회 시 해당 엔티티의 상태를 스냅샷으로 만든다.
2. 이 스냅샷을 Transaction이 끝나는 시점에 해당 Entity의 상태와 비교하여 변화가 있다면 DB에 update query를 전달한다.

### Update Logic

* 기본적으로 모든 필드의 update가 수행된다.
  * 이렇게 하면 항상 동일한 query를 적용할 수 있어 Boot 실행 시점에 미리 query를 만들어 둘 수 있고, 재사용할 수 있기 때문
* 만약 일부만 update하고 싶다면 `@DynamicUpdate`를 이용하면 된다.
