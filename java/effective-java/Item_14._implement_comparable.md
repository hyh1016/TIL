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
    - 여기서 `“작다”`는 오름차순으로 정렬했을 때 앞에 온다는 것을 의미
- 이를 구현한 클래스의 인스턴스 x, y에 대하여 `x.compareTo(y) == -y.compareTo(x)`를 만족
- 이를 구현한 클래스의 인스턴스 x, y에 대하여 추이성을 보장
    - 즉, `x.compareTo(y) > 0 && y.compareTo(z) 이면 x.compareTo(z)`를 만족
- 이를 구현한 클래스의 인스턴스 x, y에 대하여 `x.compareTo(y) == 0이면 x.compareTo(z)의 절대값과 y.compareTo(z)의 절대값이 같음`을 만족
- 권장 사항이지만 `x.compareTo(y) == 0이면 x.equals(y)`
    - 즉, 순서가 같은 클래스는 동일한 것으로 취급되는 것이어야 함
    - 일부 Collections에서 동치성 비교를 위해 equals가 아닌 compareTo를 사용하는 경우가 있기 때문에 이를 준수하지 않으면 문제를 야기할 수 있음
    - 따라서, 이를 지키지 않는다면 별도로 명시하는 것이 좋음

## compareTo 구현 방법

### 정석적인 구현 방법

```java
public class Item14 implements Comparable<Item14> {

    private int field1;
    private long field2;
    private String field3;

    // 1, 2, 3 순으로 중요도를 갖는다고 가정
    @Override
    public int compareTo(Item14 o) {
        int result = Integer.compare(field1, o.field1);
        if (result == 0) {
            result = Long.compare(field2, o.field2);
						if (result == 0) {
                result = field3.compareTo(o.field3);
            }
        }
        return result;
    }
    
}
```

- equals와 유사하게, 중요한 필드부터 비교를 수행
- 중요한 필드의 비교 결과가 0이라면 다음으로 중요한 필드를 비교
- primitive type을 비교할 때에는 Wrapper 클래스에서 제공하는 비교 연산 메서드를 호출
- reference type을 비교할 때에는 비교 연산 메서드가 정의된 경우 이를 재귀적으로 호출

### 간결한 구현 방법

```java
import java.util.Comparator;

public class Item14 implements Comparable<Item14> {

    private int field1;
    private long field2;
    private String field3;
    private static final Comparator<Item14> COMPARATOR = Comparator
            .comparingInt((Item14 item14) -> item14.field1)
            .thenComparingLong(item14 -> item14.field2)
            .thenComparing(item14 -> item14.field3);

    @Override
    public int compareTo(Item14 o) {
        return COMPARATOR.compare(this, o);
    }

}
```

- 정석적인 구현 방식은 코드 블럭이 중첩되어 가독성이 저하된다는 문제가 존재
- 위와 같이 메서드 체이닝 방식으로 정적 Comparator 구현체를 생성하여 이를 호출하는 방식으로 compareTo 메서드를 구현하는 것이 가능
- 정석적인 구현 방법에 비해 약간의 성능 저하는 있음
- 첫 번째 비교 메서드에서는 컴파일러의 타입 추론을 위해 타입을 명시해 주어야 함

## 값의 차를 반환하는 구현법을 지양할 것

- compareTo는 순서에 따라 양수, 0, 음수를 반환하는 것이기 때문에 값의 차를 비교하기 위해 뺄셈 연산 등을 이용해 이를 구현하는 경우가 많음
- 그러나 이 방식은 `오버플로우`의 위험이 있고, 부동소수점 연산인 경우 정확한 결과값이 나오지 않을 수도 있음
    - 부등호(<, >)연산 또한 마찬가지로 오류를 유발할 위험이 있으므로 사용을 지양
- 따라서, 이러한 숫자 값의 비교 결과를 반환하고자 할 때에는 Integer, Long 등에서 제공하는 compare 메서드와 같이 Wrapper가 지원하는 compare를 사용하는 것이 좋음
