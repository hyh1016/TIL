# JPA Entity의 생명주기

## Entity란?

- 데이터를 표현하는 POJO
- 엔티티 클래스는 데이터베이스의 테이블과 매핑됨
- 엔티티 인스턴스는 테이블의 하나의 row와 매핑됨
- 엔티티 내 필드는 테이블의 하나의 column과 매핑됨

## Entity의 상태

### 비영속 (new/transient)

- 객체는 있지만, 영속성 컨텍스트에 저장된 적이 없는 상태

### 영속 (managed)

- 영속성 컨텍스트에 저장된 상태
- 영속성 컨텍스트의 관리를 받음
    - 1차 캐시
    - Dirty Checking
    - Lazy Loading

### 준영속 (detached)

- 영속성 컨텍스트에 저장되었다가 분리된 상태
- detach에 의한 개별 분리 또는 영속성 컨텍스트의 완전한 초기화(clear) 또는 종료(close)에 의해 영속 상태의 엔티티가 준영속 상태로 전환되게 됨

### 삭제 (removed)

- 데이터베이스에서의 삭제가 요청된 상태
- 커밋 수행 시 해당 엔티티와 매핑되는 row가 제거됨

## Entity의 상태 전환

### 비영속 → 영속

```java
public void persist(Object entity);
```

- persist는 비영속 상태 엔티티의 영속화를 수행하며, 비영속 상태 엔티티만 처리할 수 있음
- 준영속/영속 상태의 엔티티가 인자로 주어지면 `EntityExistsException`을 던짐

### 비영속/준영속 → 영속

```java
public <T> T merge(T entity);
```

- merge는 주어진 엔티티를 영속성 컨텍스트에 등록함
- 비영속이든, 준영속이든, 심지어 영속 상태든 모두 처리 가능

### 영속 → 준영속

```java
public void detach(Object entity);
```

- 영속성 컨텍스트로부터 엔티티를 제거

### 영속 → 삭제

```java
public void remove(Object entity);
```

- 영속 엔티티를 삭제 (DB로부터 제거)
- 영속 상태 엔티티만 처리 가능
- 영속성 컨텍스트에 없는 엔티티(준영속/비영속)가 주어지면 `IllegalArgumentException`을 던짐

## Spring Data JPA의 save

```java
	@Transactional
	@Override
	public <S extends T> S save(S entity) {

		Assert.notNull(entity, "Entity must not be null");

		if (entityInformation.isNew(entity)) {
			em.persist(entity);
			return entity;
		} else {
			return em.merge(entity);
		}
	}
```

- isNew(entity)가 참이면 비영속 상태라는 뜻이므로 persist로 영속화
- 그렇지 않다면 준영속 또는 영속 상태일 것이므로 merge로 영속화
