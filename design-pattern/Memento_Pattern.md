# 📜 Memento Pattern

## Memento Pattern (메멘토 패턴)

어떤 프로그램들에서는 `객체가 상태를 가지며`, `프로그램이 수행되며 객체의 상태가 계속 변화하고`, `이전 상태로의 복원을 위해 이 상태 정보를 저장`해야 할 수도 있다. 주로 게임 프로그램 등이 그러하다.

이 때 상태 정보를 다른 데이터와 함께 한 클래스에 저장한다면, 다음의 문제점이 발생한다.

1. 클래스가 거대해져 SRP를 위배하게 된다.
2. 상태 정보는 자주 변화한다. 이는 변화하지 않는 데이터에도 지속적으로 영향을 미치게 된다.

이러한 문제를 해결하기 위한 패턴이 바로 `메멘토 패턴`이다.

메멘토 패턴은 상태 정보를 별도의 클래스로 분리하여 관리한다. 이 클래스로부터 생성된 객체를 Memento 객체라고 부르며, Memento 객체에 대한 생성 및 접근 권한은 상태의 원 소유자 클래스만이 가진다. 즉, 외부에서는 두 가지 클래스가 마치 하나의 클래스인 것처럼 동작한다.

### 구성

![Untitled](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/fe5177e8-edd8-4710-b260-65d431855781/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220603%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220603T065816Z&X-Amz-Expires=86400&X-Amz-Signature=ec354540748f991e798ba64c3f250eb415f9c3eaabe1d43758458023362c3de4&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

- `Originator` - Memento 객체를 `생성`하고, 특정 상태로 되돌아가고자 할 때 이를 `이용`한다.
- `Memento` - Originator 객체의 상태 정보를 저장한다.
- `CareTaker` - Memento 객체들을 `보관`하거나 `관리`할 수 있다. 생성, 내부 정보(상태) 접근은 불가하다.

### 특징

- 메멘토를 통해 이루고자 하는 가장 중요한 원칙은 SRP이다. 외부에서는 두 클래스가 하나인 것처럼 보임에도 이렇게 클래스를 분리하는 이유는 책임을 분리하여 불필요한 코드 변경을 막고 코드 가독성을 높이기 위함이다.
- 커맨드 패턴(Command Pattern)에서 되돌리기 연산을 수행하기 위해 해당 패턴을 이용할 수 있다.
- 반복자 패턴(Iterator Pattern)에서 Iterator의 상태 정보를 만들기 위해 해당 패턴을 이용할 수 있다.
- 플라이웨이트 패턴과 비교해보면 좋다. 플라이웨이트 패턴은 공통적 부분을 관리하는 클래스를 별도로 분리하여 중복된 데이터를 줄여 메모리 낭비를 줄이기 위함이라면, 메멘토 패턴은 상태 정보를 별도로 분리하여 너무 많은 책임을 분리하고 상태를 저장, 추적하기 위함이다.
