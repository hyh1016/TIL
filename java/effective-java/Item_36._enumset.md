# Item 36. 비트 필드 대신 EnumSet을 사용하라

## 비트 필드

```java
public class Text {
	public static final int BOLD = 1 << 0;
	public static final int ITALIC = 1 << 1;
	public static final int UNDERLINE = 1 << 2;
	public static final int STRIKETHROUGH = 1 << 3;
}
```

- 정수 열거 상수와 유사하게 static 정수 필드를 나열하되 비트 연산(&, |, ~, ^)을 적용한 결과를 이용하기 위해 각 상수에 서로 다른 2의 거듭제곱을 할당
- 각 정수가 각 비트의 자릿수를 나타내게 함으로써 0/1을 각 상수의 적용 여부로 해석할 수 있음

### 비트 필드의 문제점

- 단순 정수 상수보다도 해석하기 어려움 (비트 연산의 결과값을 계산해봐야 앎)
- 최대 몇 비트가 필요한지 API의 작성 시점에 미리 알 수 있어야 적절한 타입(int, long 등) 선택 가능
    - 32개보다 많은 상수가 필요하다면 int 대신 long을 이용해야 함
    - 그래서 long을 적용했는데 64개를 넘어선다면? 모든 필드의 자료형을 바꿔야 함…

## 비트 필드 대신 EnumSet 사용

### EnumSet

- 열거 타입의 데이터를 저장하는 집합 자료구조
- Set 인터페이스를 완벽히 구현
- 일반 집합과 동일한 기능을 수행하나, `열거 타입 상수에 대한 연산을 효율적으로 처리`
    - 내부적으로 비트 벡터로 구현되어 비트 연산을 수행

### EnumSet을 인자로 받는 메서드의 파라미터 타입을 Set으로 지정

```java
public void method(Set<MyEnum> myEnumSet) {
		// ...
}
```

- 어차피 EnumSet은 Set을 완전히 구현하므로 인자가 될 수 있음
- MyEnum으로 타입을 제한했으므로 어차피 MyEnum 집합만 받을 수 있음
    - 따라서 다른 Set의 구현체가 넘어가든 EnumSet이 넘어가든 원하는 동작을 수행할 것이라 기대 가능
    - 대신 EnumSet을 넘기는 것이 가장 효율적으로 동작하긴 할 것임
    - 하지만 클라이언트의 유연한 사용을 위해 자료형을 인터페이스(Set)로 지정해주는 것은 좋은 습관
