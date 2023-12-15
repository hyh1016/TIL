# [우이콘2020] 수십억건에서 Querydsl 사용하기

[[우아콘2020] 수십억건에서 QUERYDSL 사용하기](https://youtu.be/zMAX7g6rO_Y)

무려 3년 전의 테크 컨퍼런스 자료이지만 Querydsl은 상대적으로 사용법이 비약적으로 변화하지 않았으며(심지어 2021년 이후로 새 릴리즈도 없음), 현재에도 참고할 좋은 팁이 많은 자료라고 느껴 정리해보았다.

## Querydsl 사용 팁

### extends / implements 사용하지 않기

```java
@RequiredArgsConstructor
@Repository
public class CustomEntityRepository {
	private final JPAQueryFactory queryFactory;

	// ...
}
```

- 별도 클래스를 상속, 인터페이스를 구현하지 않고도 Querydsl을 사용할 수 있음
- 유튜브 동영상 댓글에도 언급된 내용이지만 위와 같은 방식을 이용하면 repository 계층을 이용하는 주체에서는 JPA 리포지토리와 Querydsl JPA 리포지토리를 별도 빈으로 주입받게 된다는 단점이 존재
- 배민에서 위와 같은 단점을 수용하고도 별도 리포지토리를 운영하는 방식을 택했던 이유는 Querydsl JPA 리포지토리를 일반적인 JPA 리포지토리와 달리 `엔티티 당 리포지토리`가 아니라 `비즈니스 로직에 중점을 맞춘 리포지토리`로 운영했기 때문
- 추상화를 중요시 할지, 상속/구현으로부터의 자율성을 중요시할지는 서비스 특성에 맞춰 선택하는 것이 좋아보임

### 동적쿼리는 BooleanExpression

- Querydsl의 강점 중 한 가지는 특정 분기에 따라 condition을 쿼리에 추가할 수도, 그렇지 않을 수도 있다는 것
- `BooleanBuilder`를 사용하는 경우 분기문이 많아져 코드 흐름을 이해하기 어려워지고 최종 쿼리를 예측하기도 어려워짐
- `BooleanExpression`을 사용해 별도 메서드로 분리하면 가독성도 좋아지고 재사용도 가능

## select 성능 개선

### exists 메서드 사용 금지

- 단순히 데이터의 존재 여부만을 판별할 때에는 count보다 exist가 훨씬 효율적
    - count는 총 개수를 알기 위해 부합하는 데이터를 발견해도 모든 데이터를 탐색하지만, exist는 존재 여부만을 알기 위해 부합하는 데이터를 발견하면 그 즉시 탐색을 멈춤
- 하지만 querydsl의 exists 메서드는 실제로는 `count() > 0`으로 동작
- exist 쿼리와 동일한 성능을 누리고 싶으면, `limit 1` 조건을 걸어 조회
    
    ```java
    Integer fetchOne = queryFactory
    														.selectOne()
    														.from(entity)
    														.where(condition)
    														.fetchFirst(); // limit 1
    
    return fetchOne != null;
    ```
    
    실제 쿼리는 아래와 같이 나감
    
    ```java
    select 1
    from entity
    where condition
    limit 1
    ```
    

### Cross Join 회피

- 묵시적 join을 하면 cross join에 의한 cartesian product(곱집합) 발생 가능
- 따라서 명시적 join을 이용해야 함
- 이는 Querydsl의 이슈가 아닌 `Hibernate` 자체의 이슈로 JPQL을 사용할 때에도 주의해야 함

### Entity보다 Dto로 조회하는 것을 우선

- 엔티티로 조회할시 영속성 컨텍스트에 의해 관리되는 `캐시`, `모든 컬럼 조회`에 의한 불필요한 데이터 로드, `N+1 문제` 등 다양한 성능 이슈가 발생할 수 있음
- 실시간으로 Entity의 변경 감지가 필요한 상황이라면 엔티티 조회를 해야 하지만, 그렇지 않은 경우 성능 효율을 확보하고 부작용(side-effect)을 최소화하기 위해 dto로 조회하는 편이 좋음
- 엔티티로 조회할시 기본적으로 필드명을 명시하지 않는 한 전체 컬럼이 조회되는데, 대용량 데이터인 경우 이러한 조회도 성능 이슈로 이어질 수 있기 때문에 `사용하지 않는 컬럼이거나 이미 알고 있는 값으로 대체 가능한 컬럼은 조회하지 않는 것이 좋음`
- 엔티티 조회시 일대일 관계인 연관 엔티티를 함께 조회한다면 N+1이 발생하게 됨
    - 일대일 관계 엔티티는 Lazy Loading이 불가하기 때문에 반드시 발생
    - 하나의 쿼리를 의도하고 짠 코드에 의해 100배, 1000배의 쿼리가 수행되는 무시무시한 일이 벌어질 수 있음
    - 연관 엔티티의 저장을 위한 조회라면, 연관 엔티티와 명시적 join을 하고 id 값만 꺼내오는 방식으로 대체가 가능

### distinct 사용 시 조회 컬럼 최소화에 더 주의

- distinct는 조회 대상인 모든 컬럼을 기준으로 동등성 여부를 판별
- 따라서 조회 대상 컬럼이 많아질수록 조회에 더 많은 시간을 소요하게 됨

### 커버링 인덱스

- 커버링 인덱스란, `쿼리를 충족시키는 데에 필요한 모든 컬럼을 갖고 있는 인덱스`
- 즉, 쿼리를 구성하는 컬럼(select, where, order by, group by 내에 사용된 컬럼) 전체가 인덱스에 포함된 상태를 말함
- 서브쿼리 비효율성을 커버링 인덱스를 활용한 2번의 쿼리로 분리하여 개선할 수 있음
    - 서브쿼리는 비효율적이기도 하지만 `JPQL에서 지원되지 않음`
        - JPQL에서 지원되지 않는다는 것은 곧 Querydsl JPA에서도 지원되지 않는다는 뜻
    - 먼저 PK를 커버링 인덱스로 필요한 id를 모두 조회하고, where in 절을 통해 필요한 컬럼들을 모두 조회