# Item 39. 명명 패턴보다는 어노테이션을 사용하라

## 명명 패턴

- 이름 규칙을 지정하고, 해당 이름 규칙을 준수할 때에만 특정 로직이 동작하도록 하는 것
- JUnit이 3까지 이 명명 패턴을 이용해 동작했음
    - 메서드명이 test로 시작하는 경우에만 테스트 메서드로 간주

### 명명 패턴의 단점

- 오타가 나면 안 됨
- 올바르게 사용될 것이라고 보장할 방법이 없음
    - 메서드가 아닌 클래스에 사용해도 경고 메시지를 출력하거나 하는 방식으로 잘못된 사용을 알릴 수 없음
- 따라서 명명 패턴 대신 어노테이션을 사용하는 것이 좋으며, JUnit도 4버전부터는 테스트 메서드 여부를 명명 패턴 기반이 아닌 어노테이션 기반으로 결정함

## 어노테이션

- 한글로 주석(부가 정보를 알리기 위한 도구)이며, 이름처럼 해당 코드에 대해 설명하고, 설명한대로 동작할 것을 강제하거나 특정 동작을 하도록 만들 수 있도록 하는 도구

### 마커 어노테이션

- 어노테이션 자체는 아무런 동작을 수행하지 않으며 단순히 대상을 마킹(marking)하는 어노테이션
- 이 어노테이션이 마킹한 곳에서 특정 로직을 수행하게 할 `처리기`를 따로 선언해야 함
    - `isAnnotationPreset(AnnotationClass.class)` 메서드를 통해 해당 어노테이션의 존재 여부 판별 가능

### 마커 어노테이션에 매개변수 전달하기

- 어노테이션 클래스 내에 멤버 변수를 선언해 어노테이션 호출부에서 이를 넘겨줄 수 있음
- 기본적으로 넘겨주는 값은 value 라는 멤버 변수명으로 받음
- 예시 - 모든 예외를 매개변수로 받을 수 있는 어노테이션
    
    ```java
    @Retention(RetentionPolicy.RUNTIME)
    @Target(ElementType.METHOD)
    public @interface MyAnnotation {
    
        Class<? extends Throwable> value();
    
    }
    ```
    
    ```java
    // use
    @MyAnnotation(IllegalArgumentException.class)
    public void myMethod() {
    	// ...
    }
    ```
    
- 여러 개의 매개변수를 받고자 한다면 아래와 같이 배열로 선언하면 됨
    
    ```java
    @Retention(RetentionPolicy.RUNTIME)
    @Target(ElementType.METHOD)
    public @interface MyAnnotation {
    
        Class<? extends Throwable>[] value();
    
    }
    ```
    
    ```java
    // use
    @MyAnnotation({IllegalArgumentException.class, NullPointerException.class})
    public void myMethod() {
    	// ...
    }
    ```
    
    - 하나를 전달할 때에는 동일하게 사용하며, 여러 개를 전달할 때에는 위와 같이 인자들을 중괄호로 감싸고 쉼표로 구분해 전달하면 됨
