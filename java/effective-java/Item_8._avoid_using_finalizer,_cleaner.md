# Item 8. finalizer와 cleaner의 사용을 피하라

## 소멸자

- 생성자가 리소스를 메모리에 할당하기 위해 존재한다면, 소멸자는 사용되지 않는 리소스를 회수해 메모리를 확보하기 위해 존재
- C, C++과 같은 언어에서는 리소스가 알아서 회수되지 않기 때문에 소멸자(destructor)가 존재하는 것이 보편적
- 그러나 Java는 가비지 컬렉터가 알아서 참조되지 않는 리소스를 회수하기 때문에, 소멸자를 통해 객체를 회수하는 것은 위험

### Java에서 명시적으로 소멸자를 호출하는 것의 위험

- Java에는 2개의 소멸자 finalizer, cleaner가 존재
- 소멸자의 정확한 실행 시점을 예측할 수 없음 (GC 구현 로직에 따라 다름)
- 소멸자가 반드시 실행된다고 보장할 수 없음
- GC의 효율을 저하시켜 프로그램 성능 저하를 유발

## Java에서 리소스를 명시적으로 회수하려면?

- 파일, 스레드와 같이 명시적으로 종료해야 할 리소스를 포함한 객체의 경우

### AutoCloseable, try-with-resource

- `AutoCloseable` 인터페이스를 상속한 뒤 close 메서드를 오버라이딩해 이 메서드 내에서 해당 객체가 회수될 때 수행되어야 할 동작들을 정의
- 이 close 메서드는 외부에서 `**try-with-resource`를 통해 해당 객체를 생성하고 닫음이 보장된다면** 반드시 호출됨

### 클라이언트에서 잘못된 호출을 하는 경우

```java
public class Item8 implements AutoCloseable {

    @Override
    public void close() throws Exception {
        System.out.println("종료");
    }

    public static void main(String[] args) {
        try {
            Item8 item8 = new Item8();
            System.out.println("무언가 실행");
            throw new Exception("일부러 예외 던지기");
        } catch (Exception e) {
            e.printStackTrace();
            throw new RuntimeException("또 예외 던지기");
        }
    }
}
```

- 위의 경우 main 메서드가 처리되지 않은 예외에 의해 비정상적 종료되고 있음
- 실행 결과 close() 메서드 내 로그가 찍히지 않음을 확인할 수 있음
- 즉, item8 객체가 정상적으로 소멸되지 않고 프로그램이 종료됨

### 클라이언트에서 올바르게 호출하는 경우

```java
public class Item8 implements AutoCloseable {

    @Override
    public void close() throws Exception {
        System.out.println("종료");
    }

    public static void main(String[] args) {
        try (Item8 item8 = new Item8()) {
            System.out.println("무언가 실행");
            throw new Exception("일부러 예외 던지기");
        } catch (Exception e) {
            e.printStackTrace();
            throw new RuntimeException("또 예외 던지기");
        }
    }
}
```

- 위와 같이 try-with-resource를 통해 item 객체를 생성하는 경우, 프로그램이 비정상적으로 종료됨에도 close 메서드가 호출됨을 확인할 수 있음

### 클라이언트가 올바르게 사용하지 못한다면?

- 이러한 경우를 대비하여 cleaner를 이용해 명시적으로 회수하도록 구현할 수 있음
- 하지만 이는 단순히 안전망으로만 사용하고, 클라이언트가 try-with-resource를 사용하도록 하는 것이 가장 좋은 구현법
