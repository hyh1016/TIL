# Item 34. int 상수 대신 열거 타입을 사용하라

## 열거 타입 지원 전 상수 묶음을 표현한 방법 - 정수 열거 패턴

```java
public static final int MERCURY = 0;
public static final int VENUS = 1;
public static final int EARTH = 2;
...
```

### 정수 열거 패턴의 단점

- 타입 안전을 보장할 방법이 없음 (갑자기 String이 끼어들어도 어쩔 수 없음)
- 상수의 값이 바뀌면 클라이언트 코드(이를 사용하는 코드)도 다시 컴파일해야 함
- 단순히 숫자에 불과하므로 문자열(MERCURY)을 출력하기 어려움

## 열거 타입 (Enum)

- Java 1.5부터 추가된 상수 묶음을 나타내기 위한 특수 클래스
- 단순히 숫자를 나타내는 타 언어(C, C++ 등)의 enum과 달리, Java의 열거 타입은 `완전한 형태의 클래스`
    - 필드와 메서드를 가지며, 참조 타입의 객체로 존재

### 열거 타입의 내부 구현

```java
public enum Week {
	MONDAY("M", ...),
	TUESDAY("T", ...),
	...
}
```

위와 같은 열거 타입은 클래스로 변환하면 아래와 같음

```java
public class Week {
	private static final Week MONDAY = new Week("M", ...);
	private static final Week TUESDAY = new Week("T", ...);
	...
}
```

이 특수 클래스는 다음의 특징을 가짐

- 외부에서 접근 가능한 생성자를 제공하지 않음
- 각 필드에 할당되는 인스턴스들은 단 하나씩만 존재함(싱글턴)이 보장됨

열거 타입도 결국 클래스이기 때문에, 아래와 같은 클래스의 특징 또한 가짐

- 임의의 필드/메서드를 추가할 수 있음
    - 열거 타입 클래스는 Object의 메서드들을 잘 오버라이딩하고 있음
- 임의의 인터페이스를 구현할 수 있음
    - 열거 타입 클래스는 Comparable, Serializable을 구현하고 있음

## 열거 타입 잘 사용하기

### switch를 사용하는 대신 각 상수가 추상 메서드를 구현하도록 하기

다음과 같이 계산기 열거 타입의 기능을 구현할 수 있음

```java
enum Operation {
    PLUS,
    MINUS,
    TIMES,
    DIVIDE;

    public double apply(double x, double y) {
        return switch (this) {
            case PLUS -> x + y;
            case MINUS -> x - y;
            case TIMES -> x * y;
            case DIVIDE -> x / y;
        };
				throw new AssertionError("알 수 없는 연산: " + this);
    }
}
```

- 새로운 상수가 추가될 때마다 switch문에 연산을 추가해주어야 하지만 깜박할 수도 있음
- 향상된 switch문 등장 이전에는 throw문이 도달 가능 여부와 상관 없이 컴파일이 가능했음
    - 향상된 switch문을 사용하면 도달 불가능한 경우(switch문에 모든 가능한 상수의 case문이 존재하는 경우)에는 컴파일 에러가 발생

열거 타입 또한 클래스이기 때문에 `추상 메서드`를 선언하는 것도 가능

```java
enum Operation {
    PLUS {
        @Override
        public double apply(double x, double y) {
            return x + y;
        }
    },
    MINUS {
        @Override
        public double apply(double x, double y) {
            return x - y;
        }
    },
    TIMES {
        @Override
        public double apply(double x, double y) {
            return x * y;
        }
    },
    DIVIDE {
        @Override
        public double apply(double x, double y) {
            return x / y;
        }
    };

    public abstract double apply(double x, double y);
}
```

- 추상 메서드를 선언하는 경우 각 상수가 이 메서드를 오버라이딩하도록 강제되므로 빼먹을 일이 없음
- 대신 각 상수의 초기화 이전 시점에 메서드가 정의되므로 각 상수는 서로를 호출할 수 없음. 만약 이러한 기능이 필요하다면 일반 메서드로 구현하고 switch를 통해 분기 처리해야 함

### fromString 메서드를 구현하기

fromString 메서드란, 아래와 같이 상수의 특정 필드를 통해 상수 객체를 획득하는 메서드를 말함

```java
enum Operation {
    PLUS("+"),
    MINUS("-"),
    TIMES("*"),
    DIVIDE("/");

    private final String symbol;
    private static final Map<String, Operation> stringToEnum =
            Stream.of(values()).collect(Collectors.toMap(Operation::getSymbol, e -> e));

    Operation(String symbol) {
        this.symbol = symbol;
    }

    public String getSymbol() {
        return symbol;
    }

    public Optional<Operation> fromString(String symbol) {
        return Optional.ofNullable(stringToEnum.get(symbol));
    }
}
```

- ⭐ 미리 values() 기반으로 symbol과 이 symbol을 갖는 상수를 key, value로 하는 맵을 선언해둠으로써 fromString 메서드의 호출 시점마다 반복문을 순회할 필요도, 새 Stream 객체를 생성할 필요도 없게 함
- ⭐ Optional로 반환함으로써 symbol에 매칭되는 상수가 없을 수도 있음을 클라이언트에 암시할 수 있으며, 이에 대한 null처리를 클라이언트에게 위임함

## 열거 타입은 언제 사용?

- 모든 상수 집합을 나타내는데에 최대한 열거 타입을 사용하는 것이 좋음
- 열거 타입은 가독성을 증진시키고, 오탈자를 예방하고, 상수 내부 값의 변경에 클라이언트가 대응할 필요가 없도록 한다는 점에서 구현 및 유지보수를 위한 훌륭한 도구임
