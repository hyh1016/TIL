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

- preHandle: 컨트롤러 실행 전 호출되는 메서드
- postHandle: 컨트롤러 실행 후, 뷰 실행 전 호출되는 메서드
- afterCompletion: 뷰 실행 후 호출되는 메서드
