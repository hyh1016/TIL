# JPA의 Bulk Update

## Dirty Checking을 통한 update

아래와 같이 엔티티 리스트를 조회 (아래 코드 이전에 영속성 컨텍스트는 비어있다고 가정)

```java
List<Entity> entityList = entityRepository.findAll();
for (Entity entity: entityList) {
	entity.setField(field);
}
```

원하는 쿼리는 아래와 같음

```java
update
	entity
set
	field = ?
where
	id in (?, ?, ? ...)
```

그러나 실제로는 아래와 같은 쿼리가 `리스트 size만큼` 발생

```java
select
	field1,
	field2,
	...
from
	entity
where
	id = ?
update
	entity
set
	field1 = ?,
	field2 = ?,
	...
where
	id = ?
```

### 결론

즉, Dirty Checking을 이용해 업데이트를 하게 되면 단일 엔티티에 대한 조회, 업데이트가 각각 이루어짐

## Bulk Update

위와 같은 동작 방식은 조회하는 엔티티의 수가 늘어날 수록 실행되는 쿼리 수가 늘어나므로 대용량 데이터를 업데이트하려고 할 때 매우 비효율적으로 동작

아래와 같은 방식으로 일괄 업데이트를 수행할 수 있음

### 1. @Modifying

JPA Repository에 커스텀 쿼리를 만드는 방법

```java
public interface EntityRepository extends JpaRepository<Entity, Long> {

	@Modifying
	@Query("UPDATE Entity e SET e.field = :field WHERE e.id = :id")
	int updateField(long id, String field);

}
```

- 영속성 컨텍스트를 거치지 않고 DB에 다이렉트 업데이트를 해버리기 때문에 해당 메서드를 호출한 뒤 기존 엔티티의 변경 여부를 확인하면 변경되지 않은 것처럼 보임
    - 실제 DB 데이터는 변경되었으나 영속성 컨텍스트의 캐시가 갱신되지 않기 때문
- 따라서, 해당 방법으로 bulk update를 수행한 후 엔티티를 이용해야 한다면 Modifying 어노테이션의 clearAutomatically 옵션을 true로 설정해줘야 함 (default: false)

### 2. Querydsl

```java
public long updateField(List<Long> idList, String field) {
	return jpaQueryFactory
						.update(entity)
						.set(entity.field, field)
						.where(entity.id.in(idList))
						.execute();
}
```