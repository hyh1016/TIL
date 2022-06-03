## Prototype Pattern (프로토타입 패턴)

거의 동일한 객체를 여러 개 생성하고자 할 때, 이를 일일이 생성하는 것은 다음과 같은 문제를 갖는다.

- Client가 구체적인 것(생성하고자 하는 ConcreteClass)에 접근하게 된다.
    - 이를 위해 Client는 모든 구체적 클래스에 대해 알고 있어야 하며, 구체적 클래스가 추가될 땜마다 Client 또한 수정되어야 한다.
- 객체의 타입이 컴파일 타임에 결정된다.
    - 객체의 타입이 정적으로 결정되므로 융통성 있게 작동시키기 어렵다.

이러한 문제점을 해결하기 위해 사용하는 패턴이 바로 프로토타입 패턴(Prototype Pattern)이다.

프로토타입은 다음과 같이 동작한다.

- 각 구체적 클래스가 clone 메소드를 포함하는 Prototype 인터페이스(또는 추상 클래스)를 구현하도록 한다.
    - 즉, 구체적 클래스에게 자기 자신을 복제할 책임을 맡김으로써 Client가 구체적 클래스를 알지 않아도 복제할 수 있도록 한다.
- 객체의 타입을 런타임에 결정할 수 있도록 한다.

### 구성 요소

![Prototype-Pattern](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/5804ed04-05f0-4456-a68b-9f960db2882c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220603%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220603T022703Z&X-Amz-Expires=86400&X-Amz-Signature=15877e22178176a76327defe2238f13274d25da70d5b915e93caa212fec75241&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

- Client: 추상적인 객체만 참조하며 clone 함수를 이용해 복제된 객체를 획득한다.
- Prototype: 클론 메소드가 선언된 인터페이스 또는 추상 클래스
- ConcretePrototype: 자기 자신을 복제하는 clone 메소드를 구현하는 클래스

### 특징

- clone은 이름규칙이기 때문에 메소드명을 임의로 변경하지 않는 것이 좋다. (변경하더라도 반드시 비슷한 맥락을 띄어 프로토타입 패턴을 사용했음을 알 수 있도록 해야 함)
- 팩토리 메소드 패턴, 추상 팩토리 패턴과 함께 사용되어 팩토리가 각 객체를 복제하여 제공할 수 있도록 할 수도 있다.
