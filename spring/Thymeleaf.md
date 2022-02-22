# 🗨 Thymeleaf

## 정의

spring과 함께 주로 사용되는 `템플릿 엔진`

spring-mvc의 컨트롤러에서 생성한 Model의 attribute가 context에 담겨 전달된다.

이 attribute들을 다양한 방식으로 이용할 수 있다.

## 사용법

### 변수 식: ${식}

```java
<span th:text="${변수명}">디폴트변수값</span>
```

변수가 객체인 경우 `객체명.필드명` 으로 필드에 접근할 수 있다.

내부적으로는 **필드에 직접 접근하는 것이 아니라 getter를 호출하는 것**이다. (member.id → member.getId())

### 메시지 식: #{식}

```java
<span th:text="#{member.register}">메시지</span>
```

```java
// message.properties
member.register=test message
```

외부 메시지 자원(ex: properties)에서 값(문자열)을 읽어와 출력한다.

### 링크 식: @{식}

```java
<a href="#" th:href="@{/member}">링크</a>
```

상대 경로(웹 애플리케이션의 컨텍스트) 기준으로 링크를 생성한다.

링크 내에 변수를 사용하고자 한다면 다음과 같이 설정할 수 있다.

```java
<a href="#" th:href="@{/member/{memberId}(memberId=${member.id})}">링크</a>
```

### 객체 표현식: *{필드}

```java
<div th:object="${member}">
	<span th:text="*{id}">memberId</span>
	<span th:text="*{name}">memberName</span>
</div>
```