# Item 70. 복구할 수 있는 상황에는 검사 예외를, 프로그래밍 오류에는 런타임 예외를 사용하라

## 문제 상황을 알리는 타입 Throwable

### 1. Checked Exception (검사 예외)

```java
public class Exception extends Throwable { ... }
```

- 호출하는 쪽에서 반드시 처리해야 하는(처리가 강제되는) 예외
- `Exception` 클래스 또는 이를 상속하는 클래스가 Checked Exception에 해당
- 호출하는 쪽에서 `복구할 수 있다고 여겨지는` 오류라면 Checked Exception을 던져야 함

### 2. Unchecked Exception (비검사 예외, 런타임 예외)

```java
public class RuntimeException extends Exception { ... }
```

- 호출하는 쪽에서 처리하도록 강제되지 않는 예외
- `RuntimeException` 클래스 또는 이를 상속하는 클래스가 Unchecked Exception에 해당
- 복구가 불가능할 것으로 예상되는 오류라면 Unchecked Exception을 던지는 것이 좋음
    - 복구 가능 여부가 애매할 때에도 이에 해당

### 3. Error (에러)

```java
public class Error extends Throwable { ... }
```

- 프로그램이 더이상 실행될 수 없을 정도로 심각한 문제가 발생했을 때를 나타내기 위해 존재
- JVM 자원 부족, 불변식 깨짐 등이 이에 해당
- Error는 프로그래머가 직접 이를 상속한 클래스를 만드는 일도, throw 문으로 던지는 일도 없어야 함
    - 단 한 가지, `AssertionError`만 예외
        - 프로그램이 예상하지 못한 결과를 낼 때 명시적으로 발생시키는 에러
        - 프로그래머는 디버깅을 통해 이 에러를 발생시킨 원인을 찾아 코드를 수정함으로써 제거해야 함

## Throwable 자체를 상속하는 것은 나쁜 선택

- 예외 클래스의 존재 이유는 `예외를 일으킨 상황에 대한 정보를 코드 형태로 전달하기 위함`임
    - 어디로? 발생 시점으로부터 예외를 처리할 상위의 어딘가 지점으로
- Throwable은 이러한 동작을 위한 메서드를 제공하지 않기 때문에 Throwable을 상속하여 사용하는 경우 오류 메시지를 획득하기 위해 클래스 내부 구조를 분석해 `Parsing` 해야 함
    - 하지만 Throwable의 내부 구조는 JVM, 새 Java 릴리즈에 따라 얼마든지 변할 수 있음
    - 즉, 외부에 노출하지 않고자 했던 부분에 임의 의존하는 것이므로 깨지기 쉬운 코드가 됨
        - `이해 안 되는 대목. 메시지/스택트레이스를 획득하는 메서드는 모두 Throwable에서 제공하는데 어떤 부분이 제공되지 않는다고 하는 것인지?`

## Checked Exception은 예외 상황에서 벗어나기 위한 정보를 제공하는 메서드도 함께 제공해야 함

- `Item 75`에서 더 세부적으로 다룸

## 추가 개념 - Spring의 @Transactional

- Spring의 @Transactional은 (default 동작으로는) 내부에서 Checked Exception이 발생한 경우에는 롤백을 하지 않고, Unchecked Exception이 발생한 경우에는 롤백을 함
- 이 동작이 어색할 수 있으나, Item 70을 읽고나면 확실히 이유를 이해할 수 있음
- Checked Exception은 복구될 것으로 기대되는 예외임. 따라서, 해당 트랜잭션 범위 내에서 복구된 후 이후 과정이 정상적으로 이루어질 것이라 기대할 수 있기 때문에 롤백을 하지 않음
    - 즉, Java 레벨에서 검출 후 대처가 이루어지는 부분이지 DB 레벨에는 영향을 끼치지 않을 것이라 가정
- Unchecked Exception은 복구할 수 없는 오류라 판단하고, 이 오류에 의해 이후 과정이 정상적으로 수행되지 않을 것이라 기대해 롤백을 수행함
    - 즉, Java 레벨에서 중간에 동작이 끊기기 때문에 DB에 일부만 반영되지 않도록 하기 위해 롤백을 수행하는 것
