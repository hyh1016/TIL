# Item 5. 자원을 직접 명시하지 말고 의존 객체 주입을 사용하라

## 다른 클래스의 인스턴스가 필요한 클래스의 구현

요리사 라는 클래스가 있다고 하자. 요리사는 성공적으로 요리를 완성하기 위해 여러 조리도구에 의존한다. 먼저, 요리사가 오븐을 이용해 요리를 한다고 가정하자.

## 리소스를 직접 명시

### 구현 방법

1. static 불변 객체로 소유
    
    ```java
    class Cook {
        private static final Oven oven = new Oven();
    
        public Food cooking() {
            Food food = new Food();
            oven.bake(food);
            return food;
        }
    }
    ```
    
2. 필드로 소유하고 싱글턴으로 구현
    
    ```java
    class Cook {
    		private static final Cook cook = new Cook();
        private final Oven oven = new Oven();
    
        private Cook () {}
        
        public static Cook getInstance() {
            return cook;
        }
    
        public Food cooking() {
            Food food = new Food();
            oven.bake(food);
            return food;
        }
    }
    ```
    

### 위 구현 방법의 문제점

- 오븐이 두 개 이상 필요할 수도 있음
    - 사용하는 오븐을 교체하는 changeOven 메서드를 지원한다고 하면, 멀티스레드 환경에서 thread-safe를 위반하여 문제를 발생시킬 수 있다.
- Oven 클래스를 필요로 하는 클래스가 Cook 이외에도 여러 개 존재한다고 하자. 갑자기 Oven 클래스의 구현체를 SamsungOven 클래스로 바꿔야 할 일이 생긴다면, 기존에 Oven 클래스를 소유한 모든 클래스를 수정해야 함

## 의존 객체 주입을 사용

```java
class Cook {
    private final Oven oven;

    public Cook(Oven oven) {
        this.oven = Objects.requireNonNull(oven);
    }

    public Food cooking() {
        Food food = new Food();
        oven.bake(food);
        return food;
    }
}
```

- Cook 인스턴스를 생성할 때 생성자에 사용할 Oven 인스턴스를 넘겨주는 방식

### 장점

- 불변성 유지 가능 (Cook 생성할 때 초기화된 이후로 변화 필요 없음)
    - Thread-safe 보장 가능
- Cook에서 사용할 Oven 구현체가 변경된다고 해도, Cook 클래스에 변경이 필요하지 않음
    - Cook은 어떤 Oven 인스턴스가 넘어오는지 상관하지 않기 때문
- 테스트에 용이
    - Mocking 테스트를 수행할 때, 의존하는 객체를 실제 객체가 아닌 Mock 객체를 넘겨주면 쉽게 테스트할 타겟을 분리할 수 있음

### 단점

- 의존하는 객체가 매우 많아지면, 생성자가 복잡해질 것이므로 코드가 복잡해질 수 있다. 예를 들어 요리사가 오븐 이외에도 열 개 정도의 요리 도구를 더 사용한다면 요리사 인스턴스를 생성할 때마다 생성자를 통해 10개가 넘는 파라미터를 전달받아야 하게 된다.
    - 최근에는 이러한 복잡성을 해결하기 위해 이를 보조하는 프레임워크(Spring 등)가 제공되므로 개발자가 이 문제를 직접 해결할 필요가 없다.
