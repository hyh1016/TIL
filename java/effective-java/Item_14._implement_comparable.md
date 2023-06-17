# Item 14. Comparable을 구현할지 고려하라

## Comparable

```java
public interface Comparable<T> {
	public int compareTo(T o);
}
```

- 해당 인터페이스를 구현한 클래스에게 순서가 존재함을 나타내도록 하는 인터페이스
- `compareTo`를 기준으로 해당 클래스의 배열을 순서대로 정렬할 수 있음

## Comparable의 올바른 구현 방법 (규약)

- `compareTo` 메서드는 this가 주어진 객체 o보다 작으면 음의 정수를, 크면 양의 정수를 반환
    - this - o 를 수행한다고 보면 됨
- 이를 구현한 클래스의 인스턴스 x, y에 대하여 `x.compareTo(y) == -y.compareTo(x)`를 만족
- 이를 구현한 클래스의 인스턴스 x, y에 대하여 추이성을 보장
    - 즉, `x.compareTo(y) > 0 && y.compareTo(z) 이면 x.compareTo(z)`를 만족
- 이를 구현한 클래스의 인스턴스 x, y에 대하여 `x.compareTo(y) == 0이면 x.compareTo(z)의 절대값과 y.compareTo(z)의 절대값이 같음`을 만족
- 권장 사항이지만 `x.compareTo(y) == 0이면 x.equals(y)`
    - 즉, 순서가 같은 클래스는 동일한 것으로 취급되는 것이어야 함
    - 일부 Collections에서 동치성 비교를 위해 equals가 아닌 compareTo를 사용하는 경우가 있기 때문에 이를 준수하지 않으면 문제를 야기할 수 있음
    - 따라서, 이를 지키지 않는다면 별도로 명시하는 것이 좋음
