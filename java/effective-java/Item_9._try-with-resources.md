# try-finally보다는 try-with-resources를 사용하라

## try-finally

```java
try {
		return br.readLine();
} finally {
		br.close();
}
```

- finally 내부의 명령은 반드시 실행됨
- 보통 close 메서드를 호출해 명시적으로 회수해야 하는 리소스를 회수하기 위해 해당 문법을 사용

### 문제점

- 리소스의 수가 많고, 순차적으로 연결/해제하는 리소스라면 코드가 지저분해짐
    - try-finally 문이 중첩되기 때문
- ⭐ finally 문 내부에서 close 메서드를 호출하지 않으면 자원이 제대로 회수되지 않아 메모리 누수가 발생할 수 있음
    - 즉, 프로그래머의 실수 등의 요인으로 close의 호출이 보장되지 않을 수 있음

## try-with-resources

- Java 7부터 사용 가능한 문법
- 앞선 try-finally의 경우 close의 호출이 보장되지 않아 memory leak이 발생할 수 있다는 치명적 문제점이 존재
    - 이에 대한 해결책으로 등장한 것이 try-with-resources 문법

### 구현

```java
public class Item9 {
    public static void main(String[] args) {
        try (MyResource resource = new MyResource()) {
            resource.execute();
        };
    }
}

class MyResource implements AutoCloseable {
    @Override
    public void close() throws Exception {
        // 자원을 회수하는 로직
    }
}
```

- try-with-resources를 통해 생성될 리소스는 반드시 `AutoCloseable` 인터페이스를 구현하고 close 메서드를 오버라이딩해야 함

### 장점

- 리소스가 많아져도 try 괄호 내에서 순차적으로 초기화하면 됨
    - try 문을 중첩할 필요가 없어 코드 가독성 증진
- 프로그래머가 명시적으로 close 메서드를 호출할 필요가 없음
    - 리소스 회수를 실수로 빠트릴 일이 없음
    - close 메서드가 반드시 실행됨이 보장