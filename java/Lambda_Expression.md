# Lambda Expression

## Java의 람다 (표현)식

- 람다 표현식이란? 함수(method)를 식(expression)으로 표현한 것
- Java는 jdk1.8(java 8)부터 함수형 기능 일부 지원
- 다음과 같이 사용
    
    ```java
    // 일반
    int add(int a, int b) {
    	return a+b;
    }
    
    // 함수형
    (a, b) -> {
    	return a+b;
    }
    
    // 축약 표현
    (a, b) -> a + b
    
    ```
    
    - 메소드 이름, 반환타입 정보가 제거됨
    - 반환값만 있는 경우 중괄호, return 문 제거하고 축약 표현 사용 가능
    - 매개변수가 하나면 소괄호도 생략 가능 (대신 타입 정보 없어야 함)
- Java의 람다식은 `익명 함수`가 아니라 `익명 객체`
    
    왜? Java에서 함수는 반드시 클래스 내부에 메소드로 존재해야 하므로
    
    ```java
    // 람다식
    (a, b) -> a > b ? a : b
    
    // 컴파일 시 취급 (익명 객체)
    new Object() {
    	int max(int a, int b) {
    		return a > b ? a : b;
    	}
    }
    ```
    
- 람다식을 이용하기 위해서는 `함수형 인터페이스`가 필요함

## 함수형 인터페이스

- 람다식을 다루기 위해 선언하는 인터페이스
- (람다식으로 선언될) **단 하나의 메소드**만 갖는다.
- `@FunctionalInterface` 어노테이션을 이용한다. (메타 어노테이션 부분 참조)
- 예시1) max 람다식을 위한 함수형 인터페이스
    
    ```java
    public class LambdaExample {
    
        public static void main(String[] args) {
            MaxFunc maxFunc = (a, b) -> a > b ? a : b;
            System.out.println(maxFunc.max(3, 5)); // 5
        }
    
    }
    
    interface MaxFunc {
    		// 람다식에 부여하는 이름인 것
        int max(int a, int b);
    
    }
    ```
    
- 예시2) 정렬 조건을 지정하는 Comparator의 동작 방식
    
    ```java
    // in Collections.java
    public static <T> void sort(List<T> list, Comparator<? super T> c) {
        list.sort(c);
    }
    ```
    
    ```java
    // 3, 1, 7 들어있는 리스트 선언 후 정렬
    List<Integer> list = new LinkedList<>();
    list.add(3);
    list.add(1);
    list.add(7);
    
    // 기존의 방식 (익명 클래스 선언)
    Collections.sort(list, new Comparator<Integer>() {
        @Override
        public int compare(Integer a, Integer b) {
            return a.compareTo(b); // 오름차순
        }
    });
    
    // 람다식을 이용
    Collections.sort(list, (a, b) -> a.compareTo(b));
    ```
    
    - Comparator 또한 단 하나의 메소드 `compare` 만 가지는 함수형 인터페이스이다.

## java.util.function

- 자주 사용되는 함수형 인터페이스들을 제공하는 패키지
- 이들은 모두 람다식이 할당될 수 있음

### 자주 사용하는 인터페이스들

- Runnable
    - 스레드를 만들기 위한 인터페이스
    - `void run()` 함수만 지원
- Supplier<T>
    - 공급자 역할을 하는 인터페이스
    - `T get()` 메소드 지원
        - 매개변수(입력값)는 없고, 반환값은 존재
- Consumer<T>
    - 소비자 역할을 하는 인터페이스
    - `void accept(T t)` 메소드 지원
        - 매개변수는 있고, 반환값은 없음
- Function<T, R>
    - 함수 자체의 역할을 하는 인터페이스
    - `R apply(T t)` 메소드 지원
        - 매개변수(t), 반환값(r) 모두 하나씩 존재
- Predicate<T>
    - 조건식을 표현하는데 사용
    - 람다식의 결과(반환값)가 boolean이어야 함
    - `boolean test(T t)` 메소드 지원
    - 사실 Predicate는 test 이외에도 다음과 같은 default 메소드를 제공함
        - `Predicate<T> negate()`
            - boolean 결과에 NOT 연산을 한 Predicate 반환
        - `Predicate<T> and(Predicate p)`
            - 다른 것과 and 연산한 Predicate 반환
        - `Predicate<T> or(Predicate p)`
            - 다른 것과 or 연산한 Predicate 반환
        - `static Predicate<T> isEqual(Object o)`
            - 주어진 객체와 같은지를 판별하는 Predicate 반환
            - static 함수임에 주의
            - `boolean result = Predicate.isEqual(str1).test(str2);`

### 매개변수가 2개

- BiConsumer<T, U>
    - `void accept(T t, U u)`
- BiPredicate<T, U>
    - `boolean test(T t, U u)`
- BiFunction<T, U, R>
    - `R apply(T t, U u)`

### 매개변수 타입과 반환 타입이 일치

- UnaryOperator<T>
    - `T apply(T t)`
- BinaryOperator<T>
    - `T apply(T t, T t)`

### 메소드 참조 (::)

- 하나의 메소드만 호출하는 람다식은 `메소드 참조`로 축약 표현 가능
- static 메소드 또는 해당 인스턴스의 메소드를 참조(호출)
    - ClassName::method
- 생성자 참조
    - ClassName::new
