# Item 22. 인터페이스는 타입을 정의하는 용도로만 사용하라

## 인터페이스의 목적

- 인터페이스는 `타입`으로 사용될 수 있음
- 인터페이스를 타입으로 갖는 변수는 이를 구현한 클래스의 인스턴스를 참조할 수 있음
- 인터페이스의 목적은 위와 같이 사용하여 `해당 인스턴스로 무엇을 할(do)수 있는지` 클라이언트에 알려주는 것

## 인터페이스 안티패턴

### 상수 인터페이스

- 인터페이스를 static final 필드로 채우는 것
    
    ```java
    public interface Constants {
    		static final int CONST1 = 10;
    		static final double CONST2 = 3.14159265;
    		...
    }
    ```
    

### 상수 인터페이스의 문제점

- 이를 구현하는 모든 클래스의 네임스페이스를 오염
    - 구현하는 순간 정의한 static final 함수들을 포함하게 되므로
- 아래와 같이 구현한 클래스에서도 인터페이스에 정의한 상수를 사용할 수 있음
    
    ```java
    public class StaticFinalExample {
    
        public static void main(String[] args) {
            System.out.println(ConstClass.CONST1); // 10
            System.out.println(ConstClass.CONST2); // 3.141592
        }
    
    }
    
    interface Constants {
        static final int CONST1 = 10;
        static final double CONST2 = 3.141592;
    }
    
    class ConstClass implements Constants {
    		...
    }
    ```
    

### 상수 인터페이스를 대체할 수 있는 것

1. 특정 클래스/인터페이스와 강하게 연관된 상수라면 해당 클래스/인터페이스에 추가
2. 나열할 수 있는 상수 목록이라면 `열거형(Enum)`으로 선언
3. 위의 1, 2번에 해당하지 않는 상수들이라면 유틸리티 클래스(인스턴스화가 불가능한 클래스) 내 상수로 선언
