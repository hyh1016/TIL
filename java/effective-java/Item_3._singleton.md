# Item 3. private 생성자나 열거 타입으로 싱글턴임을 보증하라

## 싱글턴(Singleton) 클래스

- 인스턴스를 단 한 개만 생성할 수 있는 클래스
- 생성자를 private(또는 protected)으로 선언해 외부에서 호출하지 못하도록 함으로써 인스턴스 생성을 제어

## 싱글턴 클래스의 생성 방법

### public static field

```java
public class Item3 {
    public static final Item3 item3 = new Item3();

    private Item3() { }
}
```

- 외부에서는 public field를 직접 호출할 수 있으나 생성자를 호출해 새 인스턴스를 만들 수는 없음
- 하지만 반드시 싱글턴이 보장되는 것은 아님 (아래 참조)

### static factory method

```java
public class Item3 {
    private static final Item3 item3 = new Item3();

    private Item3() { }

    public static Item3 getInstance() {
        return item3;
    }
}
```

- public static field 방식은 필드 자체에 의존하기 때문에 싱글턴이 아니게 변경하면 외부 코드에 영향이 갈 수 있다는 문제가 존재
    - static factory method 방식은 변경해도 외부에서는 필드가 아닌 getInstance 메서드를 호출할 뿐이므로 내부 구현 변경에 영향을 받지 않음
- 해당 방식은 Generic 과 함께 사용하여 Generic singleton factory를 구현할 수 있다는 장점도 존재
- 즉, 1번 방식보다 좀 더 확장성에 좋은 방법에 해당
- 하지만 마찬가지로 반드시 싱글턴이 보장되는 것은 아님 (아래 참조)

### 위의 두 가지 방식의 문제점

- 위의 두 방식은 2가지 상황에서 싱글턴이 깨질 수 있음
    1. 리플렉션(Reflection)을 통해 private 생성자를 호출해 인스턴스를 획득하는 경우
    2. 직렬화/역직렬화 과정에서 새 인스턴스가 생기는 경우
- 1번의 경우 이미 인스턴스가 존재하는데 private 생성자가 호출된 경우 예외를 던지도록 함으로써 예방 가능
- 2번의 경우 모든 field를 Transient로 선언하고 readResolve 메서드를 구현하여 예방 가능

### Enum type

```java
enum Item3 {
    FIELD1,
    FIELD2,
    FIELD3
}
```

- Enum은 위의 2가지 방법과 달리 어떤 상황에서도 싱글턴이 보장된다는 이점이 있음
    - 따라서 반드시 싱글턴이 보장되어야 하는 경우 enum을 이용하는 것이 좋음
- 단, 싱글턴으로 선언하려는 클래스가 다른 클래스를 상속해야 하는 경우에는 해당 방식을 이용할 수 없음