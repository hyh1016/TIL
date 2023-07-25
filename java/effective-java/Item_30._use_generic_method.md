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
