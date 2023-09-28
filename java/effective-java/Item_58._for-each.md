# Item 58. 전통적인 for 문보다는 for-each 문을 사용하라

## for-each(향상된 for문)

```java
List<String> wordList = Arrays.asList("hello", "world", "everyone");

// 기존 for 문
for (int i=0; i<wordList.size(); i++) {
	System.out.println(wordList.get(i));
}

// 향상된 for문 (for-each문)
for (String word : wordList) {
	System.out.println(word);
}
```

- 기존 for 문은 반복자, 인덱스 변수에 의해 가독성이 떨어지며 실수가 발생할 여지도 있음
- for-each 문은 가독성 면에서 기존 for문보다 뛰어나며, 성능적 결함도 없음

### for-each가 순회할 수 있는 객체

```java
public interface Iterable<E> {
	Iterator<E> iterator();
}
```

- `iterable` 을 구현하는 클래스는 모두 순회 가능

### for-each문을 사용할 수 없는 사례

- 컬렉션을 순회하며 원소를 추가/수정/삭제하는 경우 (컬렉션 자체가 변형되는 경우)
- 여러 컬렉션을 병렬로 순회해야 하는 경우
