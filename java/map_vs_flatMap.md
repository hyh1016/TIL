# map vs flatMap

## Java Stream API

- map과 flatMap은 모두 stream api의 일종
- 두 가지 모두 map의 역할을 수행하는 메서드라는 점에서는 동일
    - map의 역할: 스트림 내 요소들에 특정 연산을 적용한 결과 스트림을 반환
- 그러나 flatMap은 flatten의 속성을 가지는 map 연산 메서드

## map

```java
int[][] numbers = new int[][]{
        {1, 11}, {2, 22}, {3, 33}, {4, 44}
};

// 1. map
System.out.println(Arrays.stream(numbers).map(Arrays::stream).toList().size()); // 4
```

- 위와 같은 map 연산은 반환값으로 numbers 이차원 배열의 구성요소인 {1, 11}, {2, 22}, {3, 33}, {4, 44}의 스트림을 각각 반환
- 따라서 결과 List는 위의 4가지 array 요소를 담고 있는 리스트로 size가 4

## flatMap

```java
int[][] numbers = new int[][]{
        {1, 11}, {2, 22}, {3, 33}, {4, 44}
};

// 2. flatMap
System.out.println(Arrays.stream(numbers).flatMapToInt(Arrays::stream).boxed().toList().size()); // 8
```

- 위와 같은 flatMap 연산은 반환값으로 배열의 구성요소를 단일 요소들의 스트림으로 변환하여 반환
- 즉, 1, 11이 스트림으로 반환되고 2, 22가 스트림으로 반환되어 그 뒤에 연결되고 이러한 과정이 반복됨
- 따라서 결과는 1, 11, 2, 22, 3, 33, 4, 44가 wrapping되어 담겨져있는 List<Integer> 타입의 리스트로 size가 8
