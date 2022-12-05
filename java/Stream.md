# 🌫 Stream

## 스트림 (Stream)

### 정의

- 다양한 데이터 소스(컬렉션, 배열 등)를 표준화된 방법으로 다루기 위한 것 (Like Iterator)
- 일단 Stream으로 만들고 나면 모든 데이터 소스에 같은 방식으로(일괄적으로) 로직을 적용할 수 있다.

### 기능 (중간 연산과 최종 연산)

- **중간 연산**
    - 연산 결과가 Stream인 연산
    - 여러 번 적용 가능
- **최종 연산**
    - 연산 결과가 Stream이 아닌 연산
        - void이거나, List를 반환하거나 등등
    - ⭐ Stream의 요소를 `소비`하기 때문에, 단 한 번만 적용 가능
        - Like Iterator

### 특징

- 원본을 변경하지 않고, 새로운 데이터를 반환 (read-only)
- Stream 자체는 최종연산에 의해 변동 가능
    - Iterator처럼 동작
- 최종 연산 전까지 중간 연산이 수행되지 않음
- 멀티쓰레드를 통한 병렬 처리가 가능
    - 함수형 프로그래밍의 기원 - 큰 작업(빅데이터) 처리에 용이
    
    ```java
    // 모든 문자열 길이 합
    int sum = strStream
    						.**parallel()**
    						.mapToInt(s -> s.length())
    						.sum();
    ```
    
- 기본형 스트림을 지원하여 오토박싱/언박싱 비효율 제거
    - Stream<Integer> 대신 IntStream
    - `IntStream`, `LongStream`, `DoubleStream` 등 Primitive Type에 대한 Stream 지원
    - 기본형 스트림은 숫자와 관련된 메소드들을 일반 Stream보다 더 많이 제공 (sum, count, average 등)

## 스트림 생성

### Collection

- stream() 메소드를 이용
    
    ```java
    Stream<E> stream()
    ```
    

### Array

- of 메소드 이용하거나 Arrays의 stream 메소드 이용
    
    ```java
    // 가변 인자
    Stream<T> Stream.of(T... values)
    
    // 배열
    Stream<T> Stream.of(T[] values)
    Stream<T> Arrays.stream(T[] values)
    
    // 일부 요소만 포함
    Stream<T> Arrays.stream(T[] values, int start, int end)
    
    // 기본형 배열 스트림
    IntStream IntStream.of(int[] values)
    ```
    

### 난수 스트림

- 기본형 자료형의 무한/유한 개 난수를 포함
- Random 인스턴스의 메소드를 이용
    
    ```java
    // begin ~ end 사이의 수를 무한 개 포함
    IntStream ints(int begin, int end)
    DoubleStream doubles(double begin, double end)
    
    // 요소 수를 유한 개로 제한
    IntStream ints(long streamSize, int begin, int end)
    DoubleStream doubles(long streamSize, double begin, double end)
    ```
    

### 정수 스트림

- 기본형 자료형의 특정 범위 정수를 포함
- 각 기본형 스트림의 `range` 메소드를 이용
    
    ```java
    IntStream IntStream.range(int begin, int end)
    ```
    
    - 범위는 begin ≤ element < end
    - end를 포함하고 싶다면 `rangeClosed`를 사용

### 람다식 스트림

- 람다식의 결과값을 요소로 포함
- 무한 스트림 (limit을 통해 잘라 사용해야 함)
- **iterate**
    - 이전 요소를 seed로 다음 요소를 계산
    
    ```java
    static <T> Stream<T> iterate(T seed, UnaryOperator<T> f)
    
    // example [0, 2, 4, 6, ... n, n+2]
    Stream<Integer> evenStream = Stream.iterate(0, n->n+2);
    
    ```
    
- **generate**
    - 주어진 람다식을 기반으로 요소를 포함
    
    ```java
    static <T> Stream<T> generate(Supplier<T> s)
    
    // example [1, 1, 1, ... 1, 1]
    Stream<Integer> oneStream = Stream.generate(()->1);
    ```
    

### 파일 스트림

- 파일을 요소로 포함
- 파일 자체를 요소로 포함
    
    ```java
    Stream<Path> Files.list(Path dir)
    ```
    
- 파일 내용을 라인 단위로 요소로 포함
    
    ```java
    Stream<String> Files.lines(Path path)
    Stream<String> Files.lines(Path path, Charset cs)
    Stream<String> lines() // BufferedReader의 메소드
    ```
