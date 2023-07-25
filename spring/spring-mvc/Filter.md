# Filter

## 정의

디스패처 서블릿에 요청이 전달되기 전, 후로 수행되어야 할 로직을 처리하기 위한 객체

`웹 컨테이너(WAS 내부에서 서블릿을 관리하는 요소)`에 의해 관리된다. 때문에 다른 서블릿들과 마찬가지로 init, destroy 메서드를 가진다.

## 생명 주기

![spring-mvc-life-cycle](https://user-images.githubusercontent.com/59721541/154718308-3415c3c6-424d-4700-87c0-20cdebf95f44.png)

## 구현

필터는 다음의 인터페이스를 구현하여 사용할 수 있다.

```java
package javax.servlet;

public interface Filter {

	public void init(FilterConfig filterConfig) throws ServletException;

	public void doFilter ( ServletRequest request,
		ServletResponse response,
		FilterChain chain ) throws IOException, ServletException;

	public void destroy();

}
```

* init: 필터 객체를 초기화
* doFilter: 요청(request)이 디스패처 서블릿에 전달되기 전, 후로 실행될 로직을 정의할 수 있는 메서드
* destroy: 필터 객체를 소멸. 필터를 관리하는 웹 컨테이너가 수행
