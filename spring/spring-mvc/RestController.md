# 🍃 RestController

## 정의

REST 형식에 맞게 구현된 컨트롤러

view 대신 JSON 데이터를 반환한다.

## @RestController

응답 데이터를 알맞은 형식으로 변환하여 반환하는 컨트롤러

@Controller와 @ResponseBody를 함께 사용하는 것과 같다.

## Jackson

JSON과 문자열 간 변환을 처리하는 라이브러리

### JsonIgnore

JSON 응답에 포함시키지 않을 대상(필드)을 지정하는 어노테이션

예를 들어, 비밀번호와 같은 정보는 응답 데이터에 포함되면 안 되므로 다음과 같이 지정해주어야 한다.

```java
@JsonIgore
private String password;
```

### JsonFormat

특정 대상(필드)에 대한 날짜 형식의 변환을 처리하는 어노테이션

아래와 같이 사용한다.

```java
@JsonFormat(pattern = "yyyyMMddHH")
private LocalDateTime createdAt;
```
