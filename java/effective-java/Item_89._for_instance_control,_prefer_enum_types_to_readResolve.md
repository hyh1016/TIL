# Item 89. 인스턴스 수를 통제해야 한다면 readResolve 보다는 열거 타입을 사용하라

## 직렬화 가능한 클래스는 싱글턴을 유지하기 어려움

- 아래와 같은(Item 3 참조) 구현은 직렬화가 불가능할 때에는 싱글턴 보장이 가능하지만 직렬화 가능(implements Serializable)을 추가하는 순간 싱글턴이 아니게 됨
    
    ```java
    class OnlyOneClass {
        public static final OnlyOneClass INSTANCE = new OnlyOneClass();
    
        private OnlyOneClass() { }
    }
    ```
    
- 이는 readObject를 통한 역직렬화시 생성되는 객체는 항상 새 객체이기 때문
- readObject 대신 readResolve 기능을 이용하여 싱글턴을 보장할 수는 있음
    - readResolve: 역직렬화 `이후` 새로 생성된 객체를 인수로 호출되는 메서드로, 해당 메서드에서 반환한 객체 참조가 역직렬화의 최종 결과가 됨
- 주의할 점은 `어쨌든 readObject가 먼저 호출된다`는 것
    - Item 88에서 다룬 것과 같이 역직렬화 객체의 참조를 획득하는 등의 공격이 발생할 수 있음
    - 이를 예방하기 위해서는 모든 필드를 transient로 선언해야 함
- 하지만 아래와 같은 단점이 존재
    - 하나라도 transient를 빠트리면 공격이 발생할 수 있음
    - 어떤 상황에서든 싱글턴을 보장하도록 readResolve 메서드를 지원하는 것은 복잡한 일
- 그렇기 때문에 이러한 클래스는 `원소 하나짜리 열거 타입으로 대체`하는 것이 더 좋음
    - 열거 타입의 역직렬화의 싱글턴은 자바가 보장해주기 때문
- 하지만 컴파일 타임에 어떤 인스턴스들이 있는지 확정할 수 없어 열거 타입을 쓸 수 없는 상황이라면 어쩔 수 없이 readResolve를 사용해야 함
    - 이 경우 접근 제어자를 잘 설정해야 함
    - final인 경우 하위 클래스를 고려하지 않아도 되므로 반드시 private
    - protected/public인 경우 반드시 하위 클래스에서 정의해야 하며 그렇지 않으면 역직렬화 과정에서 ClassCastException이 발생할 수 있음
