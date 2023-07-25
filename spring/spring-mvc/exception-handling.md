# Exception Handling

## 컨트롤러 내에서의 예외 처리

`@ExceptionHandler` 어노테이션을 이용한다. 해당 어노테이션의 파라미터로 전달된 예외가 발생하면 해당 handler를 실행한다.

```java

import org.springframework.beans.TypeMismatchException;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

@Controller
public class HelloController {

		... 중략

    @ExceptionHandler(TypeMismatchException.class)
    public String handleTypeMismatchException() {
        return "예외 처리 페이지";
    }

}
```

## 공통 예외 처리

컨트롤러 내부에서가 아닌 특정 패키지 등을 대상으로 공통적인 예외 처리를 수행할 수도 있다.

이를 위해 `@ControllerAdvice` 어노테이션을 이용한다.

```java
package com.example;

import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;

@ControllerAdvice("example")
public class CommonExceptionHandler {

    @ExceptionHandler(RuntimeException.class)
    public String handleRuntimeException() {
        return "예외 처리 페이지";
    }

}
```

위의 예시는 특정 패키지인 example 및 하위 패키지에 해당 예외 처리 코드를 적용한 것과 같다.

패키지 이외에도 `@ControllerAdvice` 어노테이션은 다음과 같은 대상에 지정할 수 있다.

1.  특정 패키지 및 하위 패키지 내의 컨트롤러

    ```java
    @ControllerAdvice(String[])
    ```
2.  특정 어노테이션이 적용된 컨트롤러

    ```java
    @ControllerAdvice(Class<? extends Annotation>[])
    ```
3.  특정 타입 또는 하위 타입의 컨트롤러

    ```java
    @ControllerAdvice(Class<?>[])
    ```

## 적용 우선 순위

컨트롤러 내부에 `@ExceptionHandler` 메서드 중 해당 Exception을 처리할 수 있는 메서드가 있는지 먼저 탐색한다.

없다면 `@ControllerAdvice` 내에서 탐색한다.

즉, `@ExceptionHandler` → `@ControllerAdvice` 순서이다.
