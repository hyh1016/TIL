# Spring Event

## 강결합의 문제점

- 결합도란? 관련 없는 기능끼리 의존하는 정도
- 강결합이란? 결합도가 높은 상태를 말함
- 강결합이 발생하면, 관련 없는 로직의 수정에 영향을 자주 받게 됨 (변경의 영향이 넓어짐)
    - 이는 가독성을 떨어트리고, 불필요한 side-effect를 가져올 수 있음
    - 또한 재사용성을 떨어트림. 기능 단위로 묶어두면 여러 모듈에서 재사용이 가능

## Spring Event

- 강결합을 분리할 수 있는 도구 중 하나
- 특정 이벤트를 발행하고, 이를 리스닝하는 리스너에서 이벤트 발행을 감지해 부가 로직을 수행

### 직접 호출 (의존성 주입)

```java
@Service
public class A {

	private final B b;

	public A(B b) {
		this.b = b;
	}

	public void methodA() {
		b.methodB();
	}

}

@Service
public class B {

	public void methodB() {
		// ...
	}

}
```

- A와 관련 없는 기능인 B를 수행하기 위해 B 타입 객체를 주입받아 동작을 호출하고 있음
- 만약 관련 없는 기능인 C, D, E 등이 추후 도입된다면 이러한 부가 기능에 의해 A 클래스에 수정이 일어나고 A 클래스의 길이가 점점 길어지게 됨
- 이를 개선하기 위한 것이 Spring Event

### 이벤트 발행 - @EventListener

```java
@Service
public class A {

	private final ApplicationEventPublisher eventPublisher;

	public void methodA() {
		eventPublisher.publishEvent(new CustomEvent(args));
	}

}

@Service
public class B {

	@EventListener
	public void methodB(CustomEvent event) {
		// ...
	}

}
```

- A는 B의 존재를 알 필요가 없으며, 그냥 자신의 행동에 대한 이벤트를 발행하기만 하면 됨
- B는 A에서 발행한 이벤트를 리스닝하며 수행해야 할 로직을 수행
- 추후 C, D, E가 추가되더라도 이벤트 리스너만 추가되며 A 클래스에 변동 없음
- 주의할 점 - Spring 4.2 이전 버전이면 `ApplicationListener` 인터페이스를 구현해야 리스너로 등록할 수 있고, 이벤트 또한 `ApplicationEvent` 클래스를 상속해야 함

### 이벤트 발행 - @TransactionalEventListener

```java
@Service
public class A {

	private final ApplicationEventPublisher eventPublisher;

	@Transactional
	public void methodA() {
		// 뭔가 엔티티 제어 작업 ...
		eventPublisher.publishEvent(new CustomEvent(args));
	}

}

@Service
public class B {

	@TransactionalEventListener(phase = TransactionPhase.AFTER_COMMIT)
	public void methodB(CustomEvent event) {
		// ...
	}

}
```

- A가 트랜잭션을 이용하는 작업이라면 트랜잭션의 시점에 따라 이벤트를 리스닝할 `@TransactionalEventListener`를 사용할 수 있음
- 커밋 이전, 커밋 이후, 롤백 이후 등 세부 시점 제어가 가능
- 주의사항 - 만약 AFTER_COMMIT 옵션을 사용하는데 리스너 내에도 트랜잭션이 필요하다면, 트랜잭션의 전파 범위를 REQUEST_NEW(새 트랜잭션 스코프 생성)으로 설정해주어야 한다. 이벤트 리스너는 `@Async`가 없으면(동일 스레드에서 실행하고자 한다면) 이벤트 발행 위치와 같은 트랜잭션을 공유하고자 하는데, 리스너의 동작 시점이 커밋 이후이므로 같은 트랜잭션을 이용할 수 없어 에러가 발생하기 때문

## 주의 사항

### EventListener는 default 설정으로는 `동기`

- 이벤트 발행자와 동일 트랜잭션을 공유하며 동기로 동작
- 비동기로 동작하도록 변경하고 싶으면 Spring `@Async`와 함께 사용해야 함

### 예외 처리에 주의

- 예외는 발행자에게 전파되지 않음
- 예외를 잡아 처리하고 싶다면, 전역적 예외 핸들러를 만들어 멀티캐스터에 등록해줘야 함

## Reference

https://mangkyu.tistory.com/292
