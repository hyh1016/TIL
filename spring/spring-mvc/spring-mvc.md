# 🍃 Spring MVC

## 정의

스프링이 지원하는 웹 MVC 프레임워크

Model, View, Controller로 역할을 분담하는 MVC 디자인패턴을 이용한다.

## 핵심 구성 요소 (동작 흐름)

### DispatcherServlet

기존에는 동적 서버를 운영하기 위해 각각의 매핑 정보가 모두 Servlet으로 작성되어야 했다. 그러나 Servlet이 많아질 수록 관리하기 힘들어졌기 때문에, 단 하나의 서블릿을 두고 이 서블릿이 요청을 받아 POJO 컨트롤러와 매칭되도록 운영하게 되었다. 이 단 하나의 서블릿을 DispatcherServlet이라고 한다.

### HandlerMapping

DispatcherServlet은 직접 매칭을 수행하지 않고 이에 대한 처리를 HandlerMapping이라는 객체(빈)에게 위임한다. HandlerMapping은 내부적으로 Controller 정보를 담은 테이블을 가지고 있으며, 이로부터 해당하는 Controller를 찾아 DispatcherServlet에게 반환한다.

### HandlerAdapter

HandlerMapping이 찾아 반환한 Controller 객체를 처리하는 빈이다. 이 빈은 Controller 내에서 알맞은 메서드를 호출해 요청을 처리한 뒤 결과값(ModelAndView)을 DispatcherServlet에게 반환한다.

### ViewResolver

ModelAndView 객체를 받아 보여줄 View를 생성하여 반환하는 빈이다.
