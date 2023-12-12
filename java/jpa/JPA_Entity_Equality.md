# JPA Entity Equality

## Object의 equals

- 기본적으로 equals는 두 객체를 ==로 비교한 결과를 반환
- 즉, 같은 주소값을 갖는 참조형 객체인지를 확인

## Override equals, hashCode of JPA Entity

- JPA Entity는 일반적으로 `식별을 위한 필드값`이 같으면 같다고 판단
- 따라서 아래 두 가지 중 하나(또는 모두)를 기반으로 equals를 재구성하면 됨
    - 데이터베이스 키 (@Id 어노테이션이 부여된 필드로, primiary key)
    - 비즈니스 키(애플리케이션에서 객체 간 식별을 위해 암묵적으로 key로 간주하는 필드)
- 반드시 위의 두 값으로 비교해야 할 필요는 없지만, **양방향 참조 관계가 있는 Entity인 경우 양방향 참조를 일으키는 엔티티가 equals의 판단 대상에 포함하지 않도록 주의해야 함**
    - 상호 참조를 유발해 `스택 오버플로우` 에러를 일으킬 수 있기 때문

## Spring Data JPA의 equals, hashCode 재정의하기 (feat. hibernate)

아래와 같은 식별자 필드를 갖는 엔티티라고 가정

```java
@Id
private long id;
```

equals, hashCode를 아래와 같이 override할 수 있음

```java
@Override
public final boolean equals(Object object) {
	// 주소값이 같다면 같음
  if (this == object) return true;

	// 비교 대상이 null이거나 서로의 (실제 객체의) 타입이 다르면 무조건 다름
  if (object == null || Hibernate.getClass(this) != Hibernate.getClass(object)) return false;

	// 같은 타입이며, id 값이 같은 경우
  var that = (ImageGeneratePresetInfo) object;
  return id > 0 && Objects.equals(id, that.id);
}

@Override
public final int hashCode() {
  return id;
}
```

- `Hibernate.getClass(Object o)`
    - 프록시 객체인 경우 실제 객체를 꺼내 반환하는 메서드
    - 영속 여부에 따라 다르게 동작하지 않도록 프록시 객체인 경우 실제 객체를 꺼내 비교하기 위해 사용됨
    - 프록시 클래스의 initialization을 수행하는 side-effect가 존재함에 주의해야 함
