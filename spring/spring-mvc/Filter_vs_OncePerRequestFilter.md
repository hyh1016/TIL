# Filter vs OncePerRequestFilter

## Filter

### 정의

요청이 Dispatcher Servlet에 전달되어 Spring Container에 진입하기 전/후에 수행되어야 할 로직을 처리할 수 있는 기술

### Filter의 중복 실행 - forward

- forward의 경우 서버가 내부의 다른 리소스로 요청을 전달하는 동작을 말함
- 이 과정에서 서버의 1번 URL으로 온 요청에서 2번 URL을 호출
- 동일 HTTP Request-Response 사이클 내에서 일어나는 동작임에도, URL 호출이 2번 일어나기 때문에 filter가 2번 호출될 수 있음
- forward는 대표적 사례일 뿐, 클라이언트의 단일 요청에도 필터가 여러 번 호출될 수 있는 많은 사례들이 존재

## OncePerRequestFilter

### 정의

Filter의 중복 실행 문제를 예방하고자 만들어진 Filter의 구현체(추상 클래스)

### 구현

핵심은 아래 코드 라인

```java
boolean hasAlreadyFilteredAttribute = request.getAttribute(alreadyFilteredAttributeName) != null;
```

즉, ServletRequest의 attribute로 해당 필터가 이미 실행되었는지 여부를 저장하고, 이 값을 확인해 이미 실행되지 않았을 경우에만 필터 로직을 수행
