# Java 21 - Record, Switch 개선

## Java 21?

- 2021년 출시된 Java 17 이후 2년만에 출시된 Java의 4번째 LTS(Long Term Support) 버전
- 주요 변화는 다음과 같다.
    - [Sequenced Collections](./Java21_Sequenced_Collections.md)
    - [Virtual Thread](./Java21_Virtual_Thread.md)
    - **Record, Switch 개선**
- 이 글에서는 Record, Switch 개선에 대해 다룬다.

## Record 패턴 추가

### Java 14에서 추가된 record

- 데이터의 저장에 특화된 특수 클래스이다.
    
    ```java
    record RecordName(Type field...) {
    	// method...
    }
    ```
    

### Java 16에서 추가된 패턴 변수

- 아래와 같이 `instanceof` 연산자를 사용할 때 바로 형변환된 객체를 얻을 수 있도록 하는 문법
    
    ```java
    // 패턴 변수가 도입되기 이전
    if (obj instanceof String) {
    	String s = (String) obj;
    }
    
    // 패턴 변수가 도입된 후
    if (obj instanceof String s) {
    	
    }
    ```
    

### Java 21에 도입된 record 패턴

- 이제 레코드의 각 구성 요소를 패턴 변수로 할당할 수 있다.
    
    ```java
    record Point(int x, int y) {}
    
    if (point instanceof Point(int x, int y) {
    	System.out.println("x=" + x + ", y=" + y);
    }
    ```
    
- 레코드가 중첩된 경우 패턴도 중첩해서 할당할 수 있다.
    
    ```java
    record ColorPoint(int x, int y, Color color) {}
    
    record Color(String name, String hexCode) {}
    
    // 중첩 할당도 가능
    if (colorPoint instanceof ColorPoint(int x, int y, Color(String name, String hexCode)) {
    	System.out.println("x=" + x + ", y=" + y);
    	System.out.println("color name=" + name + ", color code=" + hexCode);
    }
    ```
    
- Generic 레코드인 경우 타입 변수에 따라 할당하는 것도 가능하다.
    
    ```java
    record MyPair<T1, T2>(T1 first, T2 second) {}
    
    if (pair instanceof MyPair(String first, Integer second)) {
    	System.out.println("Pair<String, Integer>");
    } else if (pair instanceof MyPair(Integer first, String second)) {
    	System.out.println("Pair<Integer, String>");
    } // ...
    ```
    

## Switch 개선

### null인 case의 처리 가능

- 기존에는 switch에 전달되는 값이 null인 경우 `NullPointerException` 발생
- Java 21에서는 `case null`이 추가되어 null인 경우의 처리를 추가할 수 있도록 함

### case 문에서 타입 패턴 매칭 가능

- 전달된 인자가 어떤 타입이냐에 따른 분기 처리가 가능해짐
    
    ```java
    // Java 21 이전
    if (obj instanceof Integer i) {
    	
    } else if (obj instanceof String s) {
    
    } else if ...
    
    // Java 21의 Switch 타입 패턴 매칭 사용
    switch (obj) {
    	case null -> ...
    	case Integer i -> ...
    	case String s -> ...
    	case Point(int x, int y) -> ... // 레코드 패턴
    	default -> ...
    }
    ```
    

### when 절을 통해 패턴에 조건을 추가할 수 있음

- 동일 타입 패턴에 매칭되어도 특정 조건에 따라 다른 처리가 이루어질 수 있도록 할 수 있음
    
    ```java
    static void printYesOrNo(String input) {
        switch (input) {
            case null -> { }
            case String s
            when s.equalsIgnoreCase("YES") -> {
                System.out.println("YESSSSS~~~");
            }
            case String s
            when s.equalsIgnoreCase("NO") -> {
                System.out.println("NOOOOO!!!");
            }
            case String s -> {
                System.out.println("Sorry?");
            }
        }
    }
    ```
    
- 더 유연하게 타입별/조건별 처리가 가능

## 출처

[최범균 - Java 21 주요 특징 - record 패턴, switch 패턴 매칭](https://youtu.be/8rVhPMEr2zQ)

[JEP 440](https://openjdk.org/jeps/440)

[JEP 441](https://openjdk.org/jeps/441)
