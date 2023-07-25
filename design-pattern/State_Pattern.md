# State Pattern

## State Pattern (상태 패턴)

어떤 객체가 상태 정보를 갖고, 상태에 따라 다른 동작을 수행한다고 하자. 그렇다면 객체 내에서 이를 처리하기 위해서는 아래와 같이 코드를 구현할 수 있다.

예) TCP Connection State에 따른 분기

```java
class TCPConnection {

	private String state;

	public void transmit() {
		if (state.equals("CLOSED") { ... }
		else if (state.equals("ESTABLISHED") { ... }
		else if (state.equals("LISTEN") { ... }
	}

}
```

그러나 이러한 코드는 지저분하고, 새로운 상태가 추가될 때마다 수정되어야 한다는 점에서 좋지 않은 구현이라고 할 수 있다. 이러한 분기를 해결하기 위해 사용하는 패턴이 `상태 패턴`이다.

상태 패턴은 각 상태를 데이터(field)가 아닌 상태 클래스로 나타낸다. 이들이 상태 인터페이스를 구현하도록 하여 기존의 분기문에서 상태 인터페이스 자료형의 객체로부터 메소드를 호출할 수 있도록 구현한다.

위의 TCP Connection 예제의 경우 상태 패턴을 적용하면 아래와 같이 설계할 수 있다.

![TCP-State](imgs/state-pattern-\(0\).png)

### 구성 요소

![State-Pattern](imgs/state-pattern-\(1\).png)

* `Context` - 현재 상태를 나타내는 상태 객체의 reference를 가지는 객체
* `State` - Context 객체의 상태에 따라 서로 다른 행위를 하는 함수들의 인터페이스를 정의
* `ConcreteState` - State 객체를 구현하며, Context의 상태에 따라 수행되는 행위들을 구현

### 특징

* 상태를 변경할 수 있는 권한(changeState)은 상태 정보를 갖는 객체와 상태 객체 그 자체 뿐이다.
* 상태 패턴을 이용하면 어떤 상태 객체의 메소드가 호출될지가 런타임에 결정될 수 있다는 장점이 있다.
* 각 상태 객체는 하나씩만 존재해도 되기 때문에 싱글톤 패턴을 활용할 수 있다.
