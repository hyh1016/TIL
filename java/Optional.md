# Optional

## Optional

### 정의

*   (제네릭) T 타입 객체의 Wrapper Class

    ```java
    public final class Optional<T> {
    	private final T value;
    	...
    }
    ```

    * 모든 종류의 객체 저장 가능
    * null도 저장 가능하지만 저장하지 않는 것이 좋음
      * 애당초 Optional의 등장 계기가 null을 직접 다루는 것의 위험성(NullPointerException) 해결을 위함임
      * Optional을 통해 null을 간접적으로 다루기 위해 감쌈(Wrap)
    * 내부적으로 조건문 포함하는 함수 지원해 if 없이 null 체크 가능
      * null일 가능성이 있는 변수마다 if로 체크하면 코드가 지저분해짐

### 기능

1. 생성 메소드
   * `Optional<T> of(T t)`, `Optional<T> ofNullable(T t)`
     * of는 전달값이 null이면 `NullPointerException` 발생
     * Optional 자체가 null을 감싸기 위해 사용하는 것이므로 주로 `ofNullable` 사용이 바람직
   * `Optional<T> Optional.empty()`
     * Optional 내 value가 null인 Optional 객체 생성
2. 조회 메소드
   * `T get()`
     * 값 반환
     * value가 null이면 예외 발생
   * `T orElse(T t)`
     * 값 반환
     * 없으면 매개변수로 전달된 값 반환
   * `T orElseGet(Supplier<T> s)`
     * 값 반환
     * 없으면 전달된 람다식의 결과값 반환
   * `T orElseThrow(Exception e)`
     * 값 반환
     * 없으면 전달된 예외 발생
3. value의 null 여부에 따른 분기 메소드
   * `boolean isPresent()`
     * 있으면 true, 없으면 false
   * `void ifPresent(Consumer<T> c)`
     * 있으면 value에 전달된 람다식 적용

### 기본형 Optional

*   기본형 변수를 감싸는 Wrapper 클래스

    ```java
    public final class OptionalInt {

    	private final boolean isPresent;
    	private final int value;
    	...

    }
    ```

    * value는 최초로 0으로 초기화
    * value가 실제로 0일 때와 empty일 때를 구분하기 위해 isPresent라는 변수 존재
      * empty면 value == 0이고 isPresent == false
      * 0이면 value == 0이고 isPresent == true
* 다음의 것들이 존재
  * `OptionalInt`
  * `OptionalLong`
  * `OptionalDouble`
