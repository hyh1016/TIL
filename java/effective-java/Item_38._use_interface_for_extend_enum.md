# Item 38. 확장할 수 있는 열거 타입이 필요하면 인터페이스를 사용하라

## 열거 타입을 확장하고자 할 때

- 연산 코드를 열거 상수로 나타내고 연산을 수행하는 메서드를 제공하고자 할 때, 더 다양한 연산 코드를 지원하는 열거형 클래스를 생성하고 싶을 수 있음
- 하지만 열거 타입은 상속(extends)이 불가능하기 때문에 확장할 수 없음
- 이 경우 특정 인터페이스를 구현하게 함으로써 확장과 같은 효과를 낼 수는 있음

### 예시 - 연산 가능을 나타내는 Operation 인터페이스와 기본 열거형 구현체

```java
interface Operation {
    int apply(int a, int b);
}
```

```java
enum BaseOperation implements Operation {
    PLUS("+") {
        public int apply(int a, int b) {
            return a + b;
        }
    },
    MINUS("-") {
        public int apply(int a, int b) {
            return a - b;
        }
    };

    private final String symbol;

    BaseOperation(String symbol) {
        this.symbol = symbol;
    }

    @Override
    public String toString() {
        return symbol;
    }
}
```

- 위와 같이 덧셈, 뺄셈을 기본 연산으로 하는 열거 타입이 정의되어 있을 때, 곱셈과 나눗셈을 확장한 열거 타입을 정의하고자 한다면 아래와 같이 정의하면 됨

```java
enum ExtendOperation implements Operation {
    TIMES("*") {
        public int apply(int a, int b) {
            return a * b;
        }
    },
    DIVIDE("/") {
        public int apply(int a, int b) {
            return a / b;
        }
    };

    private final String symbol;

    ExtendOperation(String symbol) {
        this.symbol = symbol;
    }

    @Override
    public String toString() {
        return symbol;
    }
}
```

- 위의 두 가지 열거 타입(기본, 확장)은 같은 인터페이스를 구현하므로 해당 인터페이스로 변수를 받으면 언제든 서로를 대체할 수 있음

### 열거형 구현체의 사용 예시

```java
public static void main(String[] args) {
    printResult(BaseOperation.class); // 덧셈, 뺄셈에 대한 결과
    printResult(ExtendOperation.class); // 곱셈, 나눗셈 대한 결과
}

public static <T extends Enum<T> & Operation> void printResult(Class<T> operations) {
    for (Operation op : operations.getEnumConstants()) {
        System.out.printf("%s %s %s = %s%n", 1, op, 2, op.apply(1, 2));
    }
}
```

- 매개 인자로 주어지는 클래스 객체는 열거형이며(Enum<T>), Operation의 구현체여야 함

## 인터페이스를 구현하는 열거 타입의 단점

- 열거 타입끼리 구현을 상속할 수 없음
- 상태(각 열거 타입 내 멤버 변수)값에 의존하지 않을 수 있는 메서드라면 interface의 default 메서드로 선언하는 방법이 있지만, 의존한다면 중복 선언하는 수밖에 없음
    - 중복량이 많아진다면 이를 처리하는 도우미 클래스/도우미 정적 메서드의 도입을 고려해보는 것이 좋음
