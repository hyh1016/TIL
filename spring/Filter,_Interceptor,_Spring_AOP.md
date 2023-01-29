# 🍃 Filter, Interceptor, (Spring) AOP

## Filter

- Dispatcher Servlet에 request가 전달되기 전/후에 실행될 로직을 정의할 수 있는 객체
- chaining 형태로 순서대로 적용된다.
- 반환 타입은 void로, 다음 Filter Chain을 호출하지 않으면 전달이 종료된다. chain을 호출하지 않고 response의 status code를 설정함으로써 유효하지 않은 요청을 사전에 차단할 수 있다.
- chaining의 파라미터로는 request, response가 전달된다.
    - 따라서, Filter에서는 request, response 객체 자체를 조작(다른 것으로 바꿔치기 등)할 수 있다.
- ⭐ 필터는 웹 컨테이너가 관리하는 것이지만, `DelegatingFilterProxy`의 등장 이후, 또 스프링 부트가 내장 톰캣을 포함하기 시작한 이후로 빈으로 등록될 수 있게 되었다.
    - `DelegatingFilterProxy`는 내부적으로 빈으로 등록된 실제 필터의 로직을 호출하는 프록시 필터이다.
    - 스프링 부트가 내장 톰캣을 포함한 이후로 웹 컨테이너 역시 스프링 컨테이너의 관리 영역이 되었고, 이후로는 `DelegatingFilterProxy` 없이도 필터를 빈으로 등록할 수 있게 되었다.

## Interceptor

- Dispatcher Servlet이 Controller에 요청을 전달하기 전/후, 뷰가 모두 로드된 후 실행될 로직을 정의할 수 있는 객체
- Dispatcher Servlet에 의해 순차적으로 호출된다.
- 반환 타입은 boolean으로, true를 반환하면 요청이 이어지고, false를 반환하면 중단된다.
    - 때문에 Filter와 달리 request, response 객체 자체를 조작할 수는 없다.
    - 대신 그 내부의 값을 조작하는 것은 가능하다.
- Filter가 Bean으로 등록될 수 있기 이전에는, 다른 Bean의 로직을 호출해야 할 때 Interceptor를 사용했으나, 그 이후로는 둘 중 무엇을 사용하든 상관이 없어졌다. 때문에 유효하지 않은 요청을 쳐 내는 용도로는 거의 Filter를 사용하는 편이다.
    - Filter가 더 앞단에서 걸러주기 때문이다.

## Spring AOP

- AOP는 횡단 관심(Aspect) 지향 프로그래밍의 약자로, 관심사 단위로 로직을 분리하는 프로그래밍 방식이다.
    - 사실상 Filter와 Interceptor의 의도를 내포하는 개념이다.
    - Filter, Interceptor는 request, response의 처리와 관련된 관심사를 다루는 기술이라고 볼 수 있다.
- AOP 자체는 메소드, 필드, 생성자 등 여러 레벨에 적용될 수 있으나, Spring AOP는 메소드 레벨의 적용만 가능하도록 제한한다.
    - 이는 Spring이 IoC Container에 의해 Dependency Injection 방식으로 객체(Bean)들을 관리하는 프레임워크이기 때문이다.
- 또한, AOP의 로직을 호출하기 위해 프록시 방식을 이용한다.
    - 프록시 방식이란, CGLIB 기반으로 프록시 객체를 생성하고 해당 프록시 객체에서 AOP의 Advice 로직을 수행하기 전 또는 이후에 본 객체(타겟 객체라고 부름)의 메소드를 호출하는 방식을 말한다.