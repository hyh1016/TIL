# Projection

## Entity, Column, Tuple Projection

### Entity

```java
User user = queryFactory
    .select(user)
    .from(user)
    .where(user.id.eq(1))
    .fetchOne();
```

- 엔티티 자체를 조회하는 경우 해당 엔티티 타입을 반환함
- select, from을 각각 쓰는 대신 selectFrom 메서드를 사용할 수 있음

### Column

```java
String name = queryFactory
    .select(user.name)
    .from(user)
    .where(user.id.eq(1))
    .fetchOne();
```

- 단일 컬럼을 조회하는 경우 엔티티 클래스 내 해당 컬럼의 타입을 반환함

### Tuple

```java
Tuple tuple = queryFactory
    .select(user.name, user.age)
    .from(user)
    .where(user.id.eq(1))
    .fetchOne();

String name = tuple.get(user.name);
Integer age = tuple.get(user.age);
```

- 다중 컬럼을 조회하는 경우 Tuple이라는 querydsl JPA에서 지원하는 객체로 반환함
- Map과 같이 get을 통해 해당하는 컬럼의 데이터를 꺼내 쓸 수 있음

## Custom Projection

원하는 타입을 반환하도록 하고 싶을 때 사용할 수 있는 방식으로, 주로 조회 결과를 dto에 매핑시키기 위해 사용됨

```java
UserDto userDto = queryFactory
	.select(Projections.bean(UserDto.class,
		user.name,
		user.age))
	.from(user)
	.where(user.id.eq(1))
	.fetchOne();
```

- Projections 클래스의 동일 목적의 호출 가능한 static method는 `bean`, `fields`, `constructor` 3가지
- 각각은 아래와 같은 특징을 가짐

### bean

- 매개변수 없는 생성자로 객체를 생성하고, setter를 통해 값을 주입함
- 즉, bean은 Java bean을 의미
- Java bean 객체를 받고자 할 때 편하지만, setter가 있어야 한다는 단점이 존재 (불변성 보장 불가)

### fields

- 리플렉션을 통해 필드에 값을 주입함
- 별도 setter가 필요 없지만, 리플렉션을 사용할 수 없는 환경이라면 사용할 수 없는 주입 방식

### constructor

- 모든 인자를 초기화하는 생성자 기반으로 값을 주입함
- 불변성을 보장할 수 있으나, 생성자와 동일하게 동작하기 때문에 인자 전달 순서를 맞춰줘야 한다는 불편함이 있음

### @QueryProjection

```java
public class UserDto {
	private String name;
	private int age;
	
	@QueryProjection
	public UserDto(String name, int age) {
		this.name = name;
		this.age = age;
	}
}
```

```java
UserDto userDto = queryFactory
	.select(new QUserDto(user.name, user.age))
	.from(user)
	.where(user.id.eq(1))
	.fetchOne();
```

- Custom Projection의 본질적 문제는, 컴파일 타임에 누락된 필드를 인지할 수 없다는 것
- @QueryProjection을 통해 dto에 대한 Q Class를 생성하여, Custom Projection에서도 컴파일 타임에 필드 누락을 인지할 수 있음
- 하지만 기존에 Querydsl 의존성이 필요 없던 dto에 불필요하게 의존성이 추가되어 나중에 Querydsl을 제거하기 어려워진다는 단점이 존재
