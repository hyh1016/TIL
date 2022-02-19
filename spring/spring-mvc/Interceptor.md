# 🍃 Interceptor

## 정의

Dispatcher Servlet에 의해 Controller 내부 로직이 실행되기 전/후로 수행되어야 할 로직을 처리하기 위한 객체

스프링 컨테이너에 의해 관리된다.

## 생명 주기

![spring-mvc-life-cycle](https://user-images.githubusercontent.com/59721541/154718308-3415c3c6-424d-4700-87c0-20cdebf95f44.png)

## 구현

인터셉터는 다음의 인터페이스를 구현하여 사용할 수 있다.

```java
package org.springframework.web.servlet;

public interface HandlerInterceptor {

	default boolean preHandle(HttpServletRequest request,
		HttpServletResponse response,
		Object handler) throws Exception {
      return true;
	}

	default void postHandle(HttpServletRequest request,
		HttpServletResponse response, Object handler,
		@Nullable ModelAndView modelAndView) throws Exception {
	}

   default void afterCompletion(HttpServletRequest request,
		HttpServletResponse response, Object handler,
		@Nullable Exception ex) throws Exception {
	}

}
```

### preHandle

컨트롤러 실행 전 호출되는 메서드. 세 번째 파라미터인 handler는 웹 요청을 처리할 컨트롤러(핸들러) 객체에 해당한다. 해당 메서드에서 true가 반환되면 handler가 실행되고, false가 반환되면 실행되지 않는다.

해당 메서드는 컨트롤러 실행 전 컨트롤러에서 필요로 하는 정보를 생성하기 위해 사용한다.

### postHandle

컨트롤러 실행 후, 뷰 실행 전 호출되는 메서드. 컨트롤러(핸들러)가 정상적으로 실행된 후 추가 기능을 구현할 때 사용한다. 컨트롤러 실행 중 예외가 발생할 시 해당 메서드는 실행되지 않는다.

### afterCompletion

뷰 실행 후 호출되는 메서드. 컨트롤러 실행 중 예외가 발생할 시 해당 메서드의 네 번째 인자로 예외가 전달된다(예외가 없다면 null). 따라서 컨트롤러 실행 후 예외가 발생했을 때 이를 처리하기 위해(로깅, 실행 시간 기록 등) 해당 메서드를 사용한다.
