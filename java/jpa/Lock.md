# Lock

## JPA의 낙관적 락 (Optimistic Lock)

### 정의

- 낙관적 락이란, 충돌이 발생하지 않는다고 낙관적으로 가정하고, 충돌이 발생하면 그 때 해결하는 방법
- 충돌이 거의 발생하지 않는 환경에서 사용하면 효율적
- **버전 관리 방식**을 이용. 수정 시점에 조회한 것과 버전이 다르면 예외를 발생시키며 롤백 수행
- 낙관적 락의 버전은 **JPA가 관리 및 제공**

### 사용 방법

```java
@Version
private int version;
```

- 엔티티에 버전 관리를 위한 필드를 추가하고 `@Version` 어노테이션을 명시
- 데이터 갱신 시도 시 버전 값이 다르면 `OptimisticLockException` 발생

## JPA의 비관적 락 (Pessimistic Lock)

### 정의

- 비관적 락이란, 충돌이 발생한다고 비관적으로 가정하고, 충돌을 미리 예방하기 위해 락을 거는 방법
- 충돌이 자주 발생하는 환경에서 사용
    - 충돌이 자주 발생하는 환경에서 낙관적 락을 사용하는 것은 오히려 잦은 충돌 후 재시도를 유발하기 때문에 좋지 않을 수 있음
    - 대신, 데드락이 발생하지 않도록 주의해야
- **데이터베이스가 제공하는 락 기능을 사용** (ex: SELECT FOR UPDATE)

### 사용

```java
em.find(Member.class, 1L, LockModeType.PESSIMISTIC_WRITE);
```

```java
// spring data jpa
public interface MemberRepository extends JpaRepository<Member, Long> {
	
	@Lock(LockModeType.PESSIMISTIC_WRITE)
	@Query("SELECT m FROM Member m WHERE m.id = :id)
	Member findByIdWithLock(@Param("id") long id);
	
}
```

- 조회 시점에 LockModeType을 이용해 레코드 락을 걸면 됨

## 두 번의 갱신 분실 문제(second lost updates problem)

- A 트랜잭션과 B 트랜잭션이 같은 데이터를 수정할 때, 먼저 수정한 것과 나중에 수정한 것 중 무엇을 반영할 것인가의 문제
- 최초 커밋을 인정 - 나중에 수정을 시도한 것에서 오류를 발생
- 나중의 커밋을 인정 - 마지막 수정자의 내용으로 덮어씌움
- 낙관적 락은 나중의 것에서 버전 충돌로 인한 오류가 발생하므로 최초 커밋을 인정하는 것에 해당
- 비관적 락은 애당초 최초의 것이 수정 중이면 나중의 것이 이 자원을 읽어오는 것부터 락에 의해 막히게 됨