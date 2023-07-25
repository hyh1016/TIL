# Factory Method Pattern (팩토리 메소드 패턴)

## Factory Method Pattern (팩토리 메소드 패턴)

### 정의

보통 한 클래스가 여러 개의 서브 타입으로 나뉘는 경우, 우리는 아래와 같이 상속 or 인터페이스를 이용해 이를 구현한다.

![Factory-Pattern](imgs/factory-method-pattern-\(0\).png)

그러나 이를 이용하려는 클래스 내부에는 서브타입을 할당하기 위해 반드시 다음과 같은(서브타입을 인스턴스화하는) 코드가 존재하게 된다.

```java
Animal animal;
if (input == "Dog") animal = new Dog();
else if (input == "Cat") animal = new Cat();
else if (input == "Panda") animal = new Panda();
```

이 코드는 확장성이 나쁘다. Animal에 새로운 서브 타입이 추가/제거될 때마다 위의 코드도 수정해야 하기 때문이다.

그러나 아마도 이는 위의 코드가 포함된 (Client와 같은) 클래스의 책임은 아닐 것이다. 따라서, **인스턴스를 결정하고 생성, 반환할 책임을 다른 클래스로 분리(위임)하는 패턴**이 바로 `팩토리 패턴`이다.

### 클래스 다이어그램

![Factory-Method-Class-Diagram](imgs/factory-method-pattern-\(1\).png)

### 구성 요소

* `Creator` - Product를 생성하기 위한 클래스를 추상화한 것. 기존에 Product의 서브타입을 생성하던 객체가 이에 의존하게 되어 구체적인 것이 아닌 추상적인 것에 의존하도록 설계를 변경한다.
* `ConcreteCreator` - ConcreteProduct들을 생성하는 클래스
* `Product` - 생성해야 할 서브타입들을 추상화한 것 (위 예제의 Animal)
* `ConcreteProduct(1,2,3)` - 서브타입들 (위 예제의 Dog, Cat, Panda)
