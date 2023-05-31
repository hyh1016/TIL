# Item 1. 생성자 대신 정적 팩토리 메서드를 고려하라

## 생성자보다는 static factory method를 통해 객체를 생성하기

```java
public static Item1 valueOf(int value) {
    return new Item1();
}
```

### static factory method란?

- factory method란, 자기 자신 또는 그 하위의 클래스를 반환하는 메서드
- static factory method를 이용하면 인스턴스 생성 없이 메서드를 호출해 해당 클래스(또는 하위 클래스)의 인스턴스를 획득할 수 있음

### 장점

1. 함수명을 마음대로 작성할 수 있어, 함수명을 통해 해당 함수의 동작을 설명할 수 있음
2. 반드시 항상 새 객체를 생성할 필요가 없음
    - 객체를 싱글톤으로 유지할 수도 있음
    - 캐싱해둔 객체를 반환하는 것도 가능 (참고: Wrapper의 동작 원리)
3. 반환 타입의 하위 타입 객체를 반환할 수도 있음
    - 사용자는 실제로 어떤 타입이 반환되는지 알 필요가 없음
    - 구체 타입에 의존하지 않으므로, 중간에 구현이 바뀌어도 외부에 변화를 주지 않음
4. static factory method의 작성 시점에 반환 클래스가 존재하지 않아도 됨
    - JDBC의 동작 원리도 이를 이용한 것

### 단점

1. 상속을 이용하게 되므로 public/protected 접근 제어자를 사용해야 함
2. constructor에 비해 존재 여부를 인지하기 어려움
    - constructor는 구조가 정해져있고, Javadoc에서 별도 구획으로 관리됨
    - static factory method는 다른 메서드와 동일하게 관리되므로, 이 메서드가 static factory method인지 확신할 수 없음
        - 이를 보완하기 위해 static factory method를 위한 naming convention이 존재