# Item 30. 이왕이면 제네릭 메서드를 사용하라

## 제네릭 메서드

```java
public static <E> Set<E> union(Set<E> s1, Set<E> s3) {
		Set<E> result = new HashSet<>(s1);
		result.addAll(s2);
		return result;
}
```

- 메서드의 접근 제어자와 반환 타입 사이에 타입 매개변수를 위치시키면 메서드를 제네릭 메서드로 만들 수 있음
- 제네릭 메서드의 타입은 `메서드 호출 시점에` 정해짐

### 제네릭 메서드의 장점

`재귀적 타입 한정`을 통해 타입 매개변수의 타입 범위를 한정지음으로써 특정 기능을 사용할 수 있게 만들 수 있음

```java
public static <E extends Comparable<E>> E max(List<E> list) {
    if (list.isEmpty()) {
        throw new IllegalArgumentException("리스트가 비어 있음");
    }
    
    E maxValue = list.get(0);
    for (var e : list) {
        if (maxValue.compareTo(e) < 0) {
            maxValue = e;
        }
    }
    return maxValue;
}
```

- 위의 메서드는 타입 매개변수를 Comarable을 구현하는 클래스로 한정함으로써 compareTo 메서드를 이용할 수 있도록 함
