# Item 2. 생성자에 매개변수가 많다면 빌더를 고려하라

## 필드가 많은 클래스의 생성자가 갖는 문제점

- 매개변수의 순서에 의존하기 때문에 Human Error가 발생할 위험이 있음
- 특히 타입이 같은 field가 여러 개 존재한다면 그 위험은 더 커짐
- 매개변수의 구분 문제는 `자바 빈즈(Java Beans) 패턴`을 통해 해결할 수 있음

## 자바 빈즈 패턴

- 기본 생성자(No Args Constructor)를 통해 인스턴스를 생성하고, setter 메서드를 통해 field 값을 설정하는 패턴
- 자바 빈즈 패턴은 위의 생성자 방식처럼 매개변수를 헷갈릴 일은 없지만 다음의 문제점을 가짐
    - 메서드(setter)를 여러 번 호출하게 됨
    - 최종 객체가 완성될 때까지 일관성(Consistency)이 깨짐
        - Thread-safe를 보장할 수 없음
    - 클래스가 불변(Immutable)으로 만들 수 없음
        - 어디서든 setter를 호출해 field의 값을 바꿀 수 있음

## 빌더 패턴

```java
Item2 item2 = Item2.builder()
                .field1(1)
                .field2("hello")
                .field3(10L)
                .build();
```

- 빌더라는 별도 객체를 통해 `Method chaining` 방식으로 setter 메서드를 field 값들을 설정하고 최종적으로 객체를 반환하는 메서드(build)를 호출해 객체를 획득하도록 하는 패턴
    - Method chaining이란, 특정 객체를 반환하는 메서드를 만들고 호출한 메서드로부터 반환된 객체의 메서드를 호출하는 것을 반복하는 것
        - 빌더의 경우 빌더의 setter 메서드들은 모두 builder를 반환해 chaining 형식으로 메서드를 호출할 수 있음

### 빌더 패턴의 장점

- 빌더는 생성 시점에만 setter가 호출되므로 불변성을 유지할 수 있음
- 빌더는 최종적으로 build가 호출될 때까지 객체가 생성되지 않으므로 Thread-safe 보장 가능

### 빌더 패턴 구현 방법

```java
public class Item2 {

    private final int field1;
    private final String field2;
    private final long field3;

    private Item2(Builder builder) {
        this.field1 = builder.field1;
        this.field2 = builder.field2;
        this.field3 = builder.field3;
    }

    public static Builder builder() {
        return new Builder();
    }

    static class Builder {
        private int field1;
        private String field2;
        private long field3;

        public Builder field1(int field1) {
            this.field1 = field1;
            return this;
        }

        public Builder field2(String field2) {
            this.field2 = field2;
            return this;
        }

        public Builder field3(long field3) {
            this.field3 = field3;
            return this;
        }

        public Item2 build() {
            return new Item2(this);
        }
    }

    public static void main(String[] args) {
        Item2 item2 = Item2.builder()
                .field1(1)
                .field2("hello")
                .field3(10L)
                .build();
        System.out.println("field1: " + item2.field1);
        System.out.println("field2: " + item2.field2);
        System.out.println("field3: " + item2.field3);
    }

}
```

- 빌더를 통해 얻고자 하는 클래스(이하 타겟 클래스)의 내부에 static class로 빌더를 정의
- 빌더 클래스 내부에는 자기 자신(빌더)을 반환하는 setter 메서드를 정의
    - 메서드 체이닝을 위함
- 타겟 클래스에는 빌더를 파라미터로 전달받는 생성자가 존재
    - 빌더의 필드들을 타겟 클래스의 필드로 할당
- 빌더에는 타겟 클래스의 생성자를 호출하는 build 메서드를 정의
    - 타겟 클래스에 자기 자신을 매개변수로 전달

## Memo

- 필드 수가 많고, 타입이 같은 필드가 여러 개일 때 사용하면 좋음
- 위와 같은 상황에 생성자를 이용하면, 매개변수의 순서를 잘못 설정할 수 있음
- 위와 같은 경우 런타임 에러 위험성을 가지므로 매개변수의 순서를 헷갈리지 않도록 하는 것은 매우 중요