# Chain of Responsibility Pattern

## Chain of Responsibility Pattern (책임 연쇄 패턴)

![Chain-Pattern](imgs/chain-of-responsibility-pattern-\(0\).png)

특정 요청을 처리할 책임을 갖는 여러 클래스를 체인 형태로 연결하고, 요청이 들어왔을 때 다음과 같이 동작한다.

1. 자신이 처리할 수 있는 요청이라면 처리
2. 자신이 처리할 수 없는 요청이라면 상위 객체에게 처리를 넘김

### 구성 요소

* `Sender(Client)` - 요청을 보내는 객체
* `Receiver(Handler)` - 요청을 받아 처리하는 객체. 추상화된 것으로 구체적인 Handler로 분류된다.

### 특징

* 요청을 보내는 Sender는 해당 요청을 어떤 객체가 처리할지 알 필요가 없다. 따라서, 요청 객체와 처리 객체 간 `결합도가 줄어든다`.
* 처리 객체가 동적으로 삽입, 삭제될 수 있다. (Linked List처럼) 때문에 책임 배정이 융통적이고 객체 간 책임 분산이 유연하게 이루어질 수 있다.
* 그러나 연결이 처리된다는 확신이 없다. 연결고리 내 모든 핸들러가 요청을 처리할 수 없을 수도 있기 때문이다.
