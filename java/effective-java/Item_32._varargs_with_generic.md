# Item 32. 제네릭과 가변인수를 함께 쓸 때는 주의하라

## varargs (가변인수)

```java
public static void main(String[] args) {
    varargs("hello", "world");
}

public static void varargs(String... hello) {
    Arrays.stream(hello).forEach(System.out::println);
}
```

- Java 5에서 추가된 문법
- 메서드에 넘기는 인수의 개수를 클라이언트가 결정하도록 함

## varargs의 동작 방식

- 가변인수를 호출하면 내부적으로 가변인수를 담기 위한 배열이 생성
- 제네릭은 실체화 불가 타입이기 때문에 런타임에 타입 정보가 소거되는데, 배열은 하위 클래스 배열의 할당을 허용하기 때문에 `제네릭이 보장하는 타입 안정성의 근간이 흔들리게 되어` 이러한 이유로 제네릭 배열은 선언이 불가 (Item 28)
    - 하지만 가변인수에 제네릭 파라미터를 던지는 것은 허용하는데, 이는 실무에서의 유용성 때문에 설계자가 모순을 수용하고 허용한 것

## 제네릭과 가변인수를 함께 사용하는 법

- 위와 같은 이유로 제네릭과 가변인수를 잘못 혼용하면 제네릭의 타입 안정성을 깨트리고 힙 오염(heap pollution)을 일으키는 결과를 야기할 수 있음
- **가변인수를 담는 제네릭 배열에 `아무것도 저장하지 않고` `배열의 참조를 외부에 노출하지 않으면` 타입 안정성을 보장할 수 있음**
- 타입 안정성을 보장했다면 클라이언트에게 이를 알리기 위해 `@SafeVarargs` 어노테이션을 붙여 제공할 수 있음
