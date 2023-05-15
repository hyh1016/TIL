# 🍃 Spring vs Spring Boot

## Spring의 불편함

1. Tomcat에 의존성을 가짐. 서비스의 실행을 위해서는 WAS(Servlet Container) 역할을 해 줄 apache tomcat을 설치하고 tomcat 내에서 애플리케이션을 구동해야 함
2. 여러 라이브러리들을 import하다보니 버전 관리가 어려워지고, configuration을 구성하는 것이 어려워짐

## Springboot의 강점

1. `spring-boot-starter-web`를 사용하면 내장 톰캣이 설정되어 별도의 tomcat 서버를 설치하지 않고 build 결과물을 실행하는 것만으로도 웹 서버를 띄울 수 있음
2. 여러 라이브러리들을 import해야 하는 복잡함 해소를 위해 `springboot-starter-*` 패키지가 등장
    - 필요한 라이브러리들의 묶음
3. 버전 관리 어려움을 해소하기 위해 `springboot-starter-*` 패키지들은 springboot 버전에 맞게 자동으로 버전 관리가 됨
    - 부트 버전만 명시해주면 됨
4. `springboot-starter-*` 패키지들은 auto-configure 수행하여 기본적 환경설정을 수행해 줌
    - db 설정, session 설정 등에 필요한 환경 변수들을 기본값으로 설정하고, 이 변수들을 통해 생성되어야 하는 Bean들을 default로 생성하는 코드들
    - 그러나 양날의 검일 수 있음 (auto-configure에 의해 원하지 않는 방향으로 동작할 수 있음)

## Reference

[https://velog.io/@courage331/Spring-과-Spring-Boot-차이](https://velog.io/@courage331/Spring-%EA%B3%BC-Spring-Boot-%EC%B0%A8%EC%9D%B4)

[https://thxwelchs.github.io/EmbeddedTomcat과Tomcat의차이](https://thxwelchs.github.io/EmbeddedTomcat%EA%B3%BCTomcat%EC%9D%98%EC%B0%A8%EC%9D%B4/)
