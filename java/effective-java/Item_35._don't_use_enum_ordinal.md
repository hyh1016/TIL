# Item 35. ordinal 메서드 대신 인스턴스 필드를 사용하라

## Enum의 ordinal()

```java
enum Fruit {
    APPLE, // 0
    ORANGE, // 1
    STRAWBERRY; // 2
}
```

- 해당 상수가 열거 타입에서 몇 번째 위치인지 반환하는 메서드
- 사용을 매우매우매우! 지양하는 것이 좋음
    - 위치를 반환한다는 것은 곧 `위치가 달라지면 달라지는 값`이라는 뜻
    - 중간에 특정 상수가 끼어들면 뒤의 상수들의 ordinal 값은 모두 바뀜

## 열거 타입 상수에 연결된 값은 직접 필드에 저장

```java
enum Fruit {
    APPLE(1),
    ORANGE(2),
    STRAWBERRY(3);

    private final int number;

    Fruit(int number) {
        this.number = number;
    }
}
```

## 그럼 언제 ordinal 메서드를 사용?

- Enum의 API 문서에는 ordinal 메서드에 대해 `대부분 프로그래머는 이 메서드를 사용할 일이 없으며, EnumSet과 EnumMap과 같은 열거 타입 기반 자료구조에 사용하기 위해 설계되었다`고 말함
- 즉, 열거 타입 기반의 범용적 자료구조를 설계하는 일이 아니라면 사용하지 말자
