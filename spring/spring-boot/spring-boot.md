# 🍃 Spring Boot

## 도입 배경

스프링을 통해 웹 애플리케이션을 개발하고자 한다면 많은 설정을 해야 한다.
모듈의 버전 관리, JDBC 연결 관리, 기본적으로 필요한 여러 빈의 등록 등이 이에 해당한다.

이 과정을 자동적으로 처리해주는 프레임워크가 스프링부트이다. 또한, 스프링부트는 내장 톰캣 서버를 포함하기 때문에 톰캣을 설치하지 않아도 동작하며, war가 아닌 jar로 패키징할 수 있다.

[Spring Initializr](https://start.spring.io/)를 이용해 설정한 프로젝트 파일을 이용할 수도 있다. 

## 필요한 모듈

### 웹 개발을 위한 `spring-boot-starter-web`

스프링부트로 웹 개발을 하기 위해 필요한 의존을 설정한다.

spring-webmvc, JSON, Validator, 내장 톰캣 등을 포함하고, spring-mvc를 위한 구성 요소(DispatcherServlet, DefaultServlet, Jackson 등)에 대한 설정을 자동적으로 생성한다.

### DB 연동을 위한 `spring-boot-starter-{jdbc, data-jpa, ...}`

데이터베이스 연동을 위한 의존을 설정한다.

프로퍼티 파일(application.properties)에 datasource를 설정함으로써 DB를 연동할 수 있다.

jdbc만을 사용하는 경우 `spring-boot-starter-jdbc`를,
JPA를 사용하는 경우 `spring-boot-starter-data-jpa`를 추가하면 된다.
