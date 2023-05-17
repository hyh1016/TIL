# 🎈 Argument Resolver

## Controller의 Parameter로 전달되는 Argument들은 어떻게 생성되는가?

- 분명 Dispatcher Servlet이 받는 것은 Http Request일 뿐이다. 그렇다면 이로부터 Controller에서 요구하는 파라미터 값들(java의 primitive type value 또는 object들)은 어떻게 생성되는 걸까?
- 이를 수행해주는 것이 바로 Argument Resolver
- 특정 타입의 파라미터, 특정 어노테이션이 사용된 파라미터 등에 알맞은 Argument Resolver가 동작하여 Argument를 세팅해 줌

## Argument Resolver

- Dispatcher Servlet은 요청을 수신하면 이를 처리할 컨트롤러를 찾기 위한 동작을 먼저 수행
- 처리할 컨트롤러를 찾았을 때, 컨트롤러의 파라미터로 전달될 데이터들을 세팅하기 위해 호출되는 것이 바로 `Argument Resolver`
- 대표적인 예시로 `@RequestParam`, `@RequestBody`, `@ModelAttribute`와 같은 것들이 있음
    - 각각 사용하는 Resolver가 다르고, Resolver 내에서 사용하는 Message Converter가 다르기 때문에 Argument의 생성 로직도 다름

## Custom Argument Resolver

- 위에서 언급한 대표적 3가지 argument 세팅 방법 `@RequestParam`, `@RequestBody`, `@ModelAttribute`는 각각 HttpServletRequest로부터 다음의 데이터를 획득하기 위해 사용됨
    - `@RequestParam`
        - Query String으로 전달된 단일 파라미터
    - `@RequestBody`
        - Request Body에 포함된 데이터
    - `@ModelAttribute`
        - Form-Data로 전달된 데이터
- 이외의 데이터를 획득하기 위해서는 Custom Argument Resolver를 선언해 줄 필요가 있음

### 구현 방법

```java
public class CustomArgumentResolver implements HandlerMethodArgumentResolver {

    @Override
    public boolean supportsParameter(MethodParameter parameter) {
        return parameter.getParameterType().equals(ExpectedType.class);
    }

    @Override
    public Object resolveArgument(MethodParameter parameter, ModelAndViewContainer mavContainer, NativeWebRequest webRequest, WebDataBinderFactory binderFactory) throws Exception {
        return new ExpectedType();
    }
}
```

`HandlerMethodArgumentResolver` 인터페이스를 구현한 후 2가지 메소드를 오버라이딩

1. `supportsParameter`
    - 파라미터가 특정 조건을 만족하는지 여부(boolean)에 따라 해당 resolver를 적용할지를 결정
    - true를 반환하는 경우 `resolveArgument` 메소드가 실행됨
2. `resolveArgument`
    - 파라미터로 전달될 Argument를 생성하는 메소드
    - 반환값이 컨트롤러의 Argument로 세팅됨