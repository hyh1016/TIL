# save() vs saveAndFlush()

## save()

‘entity를 DB에 저장’을 수행하는 메서드

트랜잭션 중 저장된 데이터는 트랜잭션의 커밋과 함께 반영됨

### 쓰기 지연

JPA의 엔티티 매니저는 트랜잭션 내의 변화를 커밋 이전 시점까지는 영속성 컨텍스트의 쿼리 저장소에 모아두고, 커밋 시점에 실행함

따라서 save에 의해 생성된 insert, update 쿼리들은 커밋 시점까지 실행이 지연됨

트랜잭션 내부에서야 실제 DB가 아닌 영속성 컨텍스트의 엔티티를 참조하게 되므로 변경 사항이 반영된 엔티티를 다룰 수 있지만, 트랜잭션 외부(서로 다른 트랜잭션)에서는 다른 영속성 컨텍스트를 가지므로 변경 사항을 볼 수 없음 (READ_UNCOMMITTED 격리 수준 제외)

## saveAndFlush()

save와 flush를 함께 실행하는 메서드

`flush`란? 영속성 컨텍스트 내 데이터 변경 사항을 DB에 **즉시** 반영하는 일을 말함

### 언제 사용?

생각보다 사용할 일이 없음. JPA가 아닌 곳에서 트랜잭션 내 변화를 감지해야 할 때 사용

1. **프로시저**
    
    JPA에서 데이터를 변경하고 프로시저를 호출하는 경우 프로시저에서도 이 JPA 내 변경을 알고 작업해야 하므로 flush를 사용해 DB에 반영해주고 호출
    
2. **영속성 컨텍스트의 관리를 받지 못하는 쿼리를 수행할 때 (ex: 벌크 연산)**
    
    @Query + @Modifying 기반의 bulk 연산은 그 결과가 영속성 컨텍스트에 반영되지 않음
    
    따라서, 이러한 연산이 일어나는 시점에 flush를 통해 영속성 컨텍스트 내 데이터를 DB에 즉시 반영하고 영속성 컨텍스트를 비워주는 작업을 포함시켜줘야 함
    
    이는 아래와 같은 어노테이션으로 나타낼 수 있음
    
    `@Modifying(clearAutomatically = true, flushAutomatically = true)`
    

### 굳이 사용하지 않아도 될 때?

- 트랜잭션 커밋 시점에서는 flush가 자동 호출되므로 명시하지 않아도 됨
- JPQL 쿼리 호출 시에도 자동 호출됨
- auto-increment 컬럼이 있는 엔티티를 save할 때에도 자동 호출 됨 (sequence number 획득을 위함)

굳이 사용하지 않아도 될 때에는 사용하지 않는 편이 좋음. 어쨌든 즉시 반영이라는 단계가 추가되므로 일반적인 save보다는 효율성 면에서 좋지 않기 때문

### 주의할 점

아주 주의할 점! flush와 commit은 서로 다른 개념임!

DB에 즉시 반영이라는 것이, 해당 트랜잭션 범위 내에서 영속성 컨텍스트 내에만 존재하던 변경을 DB 내에 쓴다는 것이지 이 변경 사항을 커밋한다는 것이 아님

따라서, flush를 호출해도 트랜잭션 외부에서 변경 사항을 볼 수 있는 것은 save와 동일함

## 출처

- [JPA 사용 시 19가지 Tip](https://velog.io/@wisepine/JPA-%EC%82%AC%EC%9A%A9-%EC%8B%9C-19%EA%B0%80%EC%A7%80-Tip)
- [Difference Between save() and saveAndFlush() in Spring Data JPA](https://www.baeldung.com/spring-data-jpa-save-saveandflush)