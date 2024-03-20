# Embedded Tomcat (내장 톰캣)

## Tomcat?

- 아파치 재단에서 개발 및 운영 중인 서블릿 컨테이너(Servlet Container)이자 WAS
- 서블릿 컨테이너란, 서블릿의 생명주기를 관리하는 컨테이너를 말함

## Spring Boot Embedded Tomcat

- 원래 Spring 기반 웹 애플리케이션은 `war`라는 확장자의 빌드 산출물로 만들어 tomcat을 통해 실행해야 함
- 그런데 spring boot 기반의 웹 애플리케이션은 jar 산출물로도 실행이 가능함
- 이게 어떻게 가능할까? 바로 spring boot에는 `내장 톰캣`이 존재하기 때문
- 아래는 spring-boot-starter-web의 dependency tree. 내장 톰캣에 대한 의존성이 존재함
    
    ```java
    \--- org.springframework.boot:spring-boot-starter-web -> 3.2.3
         +--- org.springframework.boot:spring-boot-starter-tomcat:3.2.3
         |    +--- jakarta.annotation:jakarta.annotation-api:2.1.1
         |    +--- org.apache.tomcat.embed:tomcat-embed-core:10.1.19
    ```
    

### Default Tomcat Thread Pool 설정

- spring boot 기준 기본 thread pool 설정은 아래와 같음
    - max thread pool size는 200 - 최대 200개의 스레드가 생성됨
    - core thread pool size는 10 - idle 상태인 경우 10개의 스레드가 유지됨
    - waiting queue size는 100 - 최대 100개까지의 요청이 스레드가 없는 경우 큐에서 대기 가능
    - max connection은 8192 - 동시 수용 가능한 요청자의 수는 8192
- 서버의 스펙, 서비스의 특성 등을 잘 고려하여 위의 값들을 튜닝할 수 있어야 함