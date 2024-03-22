# JPA Entity Lifecycle Event

## JPA Entity Lifecycle

- JPA의 엔티티에도 생명주기에 따라 발행되는 이벤트들이 존재
- 이러한 이벤트들은 어노테이션 형태로 지원됨
    - `@PrePersist` - 영속 상태로 전환되기 전에 호출
    - `@PostPersist` - 영속 상태로 전환된 후 호출
    - `@PreLoad` - 영속성 컨텍스트에 로드된 후 호출
    - `@PreUpdate` - 수정이 발생하기 전에 호출
    - `@PostUpdate` - 수정이 발생한 후 호출
    - `@PreRemove` - 엔티티가 제거되기 전에 호출
    - `@PostRemove` - 엔티티가 제거된 후 호출

## 사용 방법

### Entity에 메서드 선언

```java
@Entity
public class MyEntity {

	@Id
	@GeneratedValue
	private long id;
	
	private String name;
	
	@PrePersist
	public void prePersist() {
		// 엔티티 영속화 이전에 수행될 로직
	}
	
	@PostPersist
	public void postPersist() {
		// 엔티티 영속화 이후 수행될 로직
	}

}
```

- 어노테이션이 지정된 콜백 메서드를 등록하면 엔티티 상태에 변화가 일어날 때 알맞은 콜백 로직이 수행됨
- 반환값은 void여야 함
- 위와 같이 사용하는 경우, 엔티티 내에 선언된 메서드이므로 this를 통해 내부 필드에 접근 가능

### 별도 클래스에 선언 후 EventListeners로 등록

```java
 public class MyJpaEventListener {
 
		@PrePersist
		public void prePersist(MyEntity myEntity) {
			// 엔티티 영속화 이전에 수행될 로직
		}
		
		@PostPersist
		public void postPersist(MyEntity myEntity) {
			// 엔티티 영속화 이후 수행될 로직
		}
	 
 }
```

```java
@Entity
@EntityListeners(MyJpaEventListener.class)
public class MyEntity {

	@Id
	@GeneratedValue
	private long id;
	
	private String name;

}
```

- 여러 엔티티에서 공통적으로 등록하는 콜백 메서드의 경우 위와 같이 별도 커스텀 리스너를 만들어 재사용이 가능
- 인자로 엔티티를 주입받아 내부 필드 값에 접근 가능
- 주의할 점은, 이 경우 spring boot application 클래스 또는 jpa configuration 클래스에 `@EnableJpaAuditing` 어노테이션을 지정해줘야 함

## 유의 사항

### 콜백 메서드에서 예외 발생 시

- 이벤트를 받아 처리하는 콜백 메서드에서 예외가 발생하면 **트랜잭션은 롤백됨**
- 왜냐하면, 동일 스레드 동일 트랜잭션 스코프 내에서 호출되는 로직이기 때문
    - 즉, 이벤트의 호출 시점은 Pre~의 경우 트랜잭션 스코프를 연 뒤이며, Post~의 경우 닫기 전임

## Reference

[JPA Entity Lifecycle Events | Baeldung](https://www.baeldung.com/jpa-entity-lifecycle-events)
