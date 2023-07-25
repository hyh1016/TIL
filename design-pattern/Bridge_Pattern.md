# Bridge Pattern

## Bridge Pattern (브리지 패턴)

![Bridge-Pattern](imgs/bridge-pattern-\(0\).png)

* `추상을 구현으로부터 분리`하여 독립적으로 변하게 하는 패턴
* 추상 클래스 `Abstraction`과 구현 인터페이스 `Implementor`는 포함 관계를 갖는데, 이 관계를 bridge라고 한다.
* 브리지 패턴은 주로 구현 단에서 변화가 잦을 때 사용한다.

### 구성

* 왼쪽에는 abstract class와 operation이 정의된다.
* 오른쪽에는 implement되는 여러 버전이 하나의 interface로 묶여 있다.

### Bridge & Adapter

브리지 패턴은 다음과 같이 어댑터 패턴과 함께 사용되는 경우가 많다.

![Bridge-Adapter](imgs/bridge-pattern-\(1\).png)

### 브리지 패턴 예시 - 도형(Shape)과 도형 그리기 도구(Drawing)

![Bridge-Example](imgs/bridge-pattern-\(2\).png)

위와 같이 설계하면 추상 계층에서는 구현 계층의 인스턴스 draw를 통해 draw 메서드를 호출하기만 하므로, draw가 내부적으로 어떤 변화가 일어나든 draw 메서드의 명칭에만 변함이 없다면 변화를 신경쓰지 않아도 된다.
