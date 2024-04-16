# Servlet container vs Spring container ?

## Servlet Container

### 정의

- Java의 서블릿(Servlet)을 관리하는 프로그램
- 대표적 예시로 Apache tomcat이 있음

### 하는 일

- HTTP 요청을 처리하기 위한 기능을 제공 (소켓 생성 - 특정 포트로의 TCP 연결을 리스닝)
- 서블릿의 생명주기를 관리 (생성, 호출, 소멸)
- 자원의 효율적 관리 (스레드, 세션 등)

### 존재 이유

- 서블릿 컨테이너가 존재함으로써 개발자는 HTTP 통신을 위한 로직, 서블릿의 관리 로직, Thread Pool이나 Connection Pool 등의 관리 로직으로부터 자유로워짐
- 이는 개발자가 애플리케이션 자체의 비즈니스 로직에 더 집중할 수 있도록 만듦

## Spring Container

### 정의

- Spring Bean을 관리하는 프로그램
- Spring Framework의 구성 요소 중 하나

### 하는 일

- Bean의 생명주기를 관리 (생성, 호출, 소멸)
- Bean 간 의존성 주입을 수행
- 애플리케이션의 설정 정보, 환경 변수 등을 중앙 집중 형식으로 관리할 수 있도록 함
    - 실제로 이러한 정보는 전부 ApplicationContext에서 관리되는데, 이 ApplicationContext는 BeanFactory의 하위 인터페이스이므로 Spring Container를 포함하는 것이라 볼 수 있음

### 존재 이유

- Spring 기반 애플리케이션의 초기화 및 설정 관리를 단순화
- 그 외에도 다양한 백엔드 특화 개발 관련 작업을 지원하기 위한 기능들을 제공

## Servlet Container vs Spring Container ?

- 두 개는 사실 전혀 다른 목적을 갖고 전혀 다른 기능을 제공
- Container 라는 네이밍에서의 목적만 같다고 봄
    - 무언가의 생명주기를 관리하고, 그와 연관된 기능이나 자원을 관리하여 개발자가 이러한 책임으로부터 자유로워질 수 있도록 함
    - 개발자가 이러한 책임으로부터 자유로워지면, 애플리케이션 자체의 비즈니스 로직에 더 집중할 수 있게 됨
