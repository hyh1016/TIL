# Find by EntityManager vs JPQL select query

## EntityManager의 find

```java
User user = em.find(User.class, 1L);
```

- 엔티티의 식별자로 엔티티를 조회
- 단일 데이터 조회를 위해 사용됨
- 영속성 컨텍스트에 있는지 먼저 확인하고, 없으면 DB에 쿼리를 수행해 데이터를 가져옴
    - 영속성 컨텍스트 → DB

## JPQL의 Select

```java
List<User> userList = em.createQuery("SELECT u FROM User u").getResultList();
```

- JPQL이라는 쿼리 언어를 통해 엔티티를 조회
- 단일 조회, 다중 데이터 조회 모두 가능하며 복잡한 쿼리(조인, 그룹화, 집계 등) 실행도 가능
- **DB에 쿼리를 수행해 데이터를 가져오고, 영속성 컨텍스트에 있으면 조회한 결과를 버림**
    - DB → 영속성 컨텍스트
    - 영속성 컨텍스트에 존재 시 이 데이터를 우선시함
    - **왜 그렇게 동작하는가?**
        - 일단 JPQL으로부터 어떤 식별자를 갖는 엔티티를 조회할 것인지 결정하기 어려움
            - find 메서드처럼 조회할 식별자가 명시되어 있는 것이 아니기 때문
        - 따라서 식별자 기반으로 데이터를 찾는 영속성 컨텍스트에서 조회할 엔티티의 캐시가 있는지 판단하기 어려움
        - 그러므로 일단 DB에서 찾고, 찾았으면 식별자를 알 수 있으니 이들을 식별자로 영속성 컨텍스트에 존재하는지 확인해 있는 것들은 버리는 것
            - 조회한 것보다 기존의 것을 우선시하는 이유는, 기존의 것에 변경이 있다면 이 변경을 트랜잭션 커밋 시 반영해줘야 하기 때문
            - 조회해온 것으로 덮어씌우면, 변경 내용이 유실되므로

## 궁금증

### Querydsl의 select는 어떻게 동작?

- Querydsl은 JPQL Builder임
- 따라서, 결론적으로 JPQL 조회문과 동일하게 동작 (DB → 영속성 컨텍스트 순서로 조회 후 영속성 컨텍스트에 있는 조회 결과들은 폐기)

### Spring Data JPA의 findById, findAll은 어떻게 동작?

- **findById**
    - em.find와 동일하게 동작
    - 따라서, 영속성 컨텍스트 → DB 순으로 조회
- **findAll**
    - JPQL select와 동일하게 동작
    - 따라서, DB → 영속성 컨텍스트 순으로 조회
