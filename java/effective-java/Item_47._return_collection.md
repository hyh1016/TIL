# Item 47. 반환 타입으로는 스트림보다 컬렉션이 낫다

## 일련의 원소를 반환하는 메서드의 반환 타입

- 기본은 `컬렉션 인터페이스` (List, Set 등)
- 성능에 민감하거나 primitive type을 다루는 경우에만 특별히 `배열` 이용
- Java 8 이후로 도입된 Stream은?

### Stream이 도입됐지만 반환 타입으로는 컬렉션/배열이 좋음

- Stream은 Iterable 인터페이스의 기능을 모두 포함하지만 `반복 불가`
    - 왜냐하면, Iterable을 extend하지 않기 때문
- 즉, Stream과 Iterable은 서로를 얻어내기 위해 별도의 어댑터(Adaptor)가 필요
- 따라서, 클라이언트가 둘 중 어떤 것을 필요로하는지 모르는 API 작성자 입장에서는 **두 가지를 모두 손쉽게 획득할 수 있는 Collection 또는 그 하위 타입을 반환 타입으로 사용**하는 것이 최선
    - 배열 역시 Arrays.asList()와 Stream.of를 통해 Iterable과 Stream을 쉽게 얻을 수 있음
