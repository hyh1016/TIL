# REST

## REST (Representational State Transfer)

**분산 하이퍼미디어 시스템(ex: 웹)을 위한 소프트웨어 프로그램 아키텍처의 한 형식**

로이 필드의 “어떻게 Web에 영향을 주지 않는 방향으로 HTTP를 개선할 수 있을까?” 에서 시작된 아키텍처 스타일로, 제공될 데이터에 대한 모든 정보를 표현함으로써 다양한 플랫폼에서 일관적으로 이를 이용할 수 있도록 하여 종속성을 분리하는 것이 목적

## REST의 아키텍처 스타일

### 1. Client-Server 구조

- 자원을 요청하는 Client, 자원을 제공하는 Server로 구성됨
- 클라이언트와 서버 간 의존성을 줄여 독립적 발전이 가능하도록 함
- 서로가 어떤 언어로 개발되든 어떤 아키텍처를 사용하든 API 형식만 유지된다면 영향을 받지 않음

### 2. Stateless

- HTTP의 Stateless 특성에 기반하여 REST도 Stateless를 준수
- 클라이언트의 요청 정보를 서버에 저장하지 않고, 이전/이후 요청에 영향을 미치지 않도록 함
- 서버의 부담을 줄이고, 서버가 확장에 용이하도록 함

### 3. Cache

- 응답 데이터의 캐싱 가능 여부, 캐시 생성을 위한 데이터 등을 제공해야 함
- 이를 위해 `Cache-Control`, `E-Tag`, `Last-Modified` 등의 태그가 사용됨

### 4. Uniform Interface ⭐

- 리소스에 대한 제어를 일관적 인터페이스로 수행
    - `인터페이스`의 목적? **“구현과의 종속성을 분리”**
- 특정 언어/기술(구현)에 종속되지 않고, HTTP 표준 규약을 따르는 모든 플랫폼에서 이용 가능해야 함

### 5. Layered System

### 6. Code-On-Demand (Optional)

## Uniform Interface의 제약 조건

### 1. Resource-Based

- URI를 통해 리소스를 식별할 수 있어야 함

### 2. Manipulation Of Resources Through Representations

- HTTP 표준 메서드를 통해 요구하는 행위를 설명할 수 있어야 함
- GET(조회), POST(생성), PUT(수정), DELETE(삭제)

### **3. Self-Descriptive Message**

- 목적지 Host 헤더, 표준 MIME Type 헤더 등을 통해 자기 설명적 메시지를 제공해야 함
- 클라이언트가 이를 통해 애플리케이션에서 다루는 데이터 구조에 대한 추가 정보를 알 필요 없이 데이터의 타입을 결정지을 수 있도록 해야 함

### **4. H**ypermedia **A**s **T**he **E**ngine **o**f **A**pplication **S**tate

- 앞글자를 따서 `HATEOAS` 라고 부름
- 클라이언트를 리소스의 링크 간 전이 구조에서 분리해야 함
- 링크를 통한 애플리케이션의 상태 전이가 가능해야 함

## HTML과 JSON의 RESTful

- 1번과 2번은 양 쪽 모두 쉽게 만족 가능 (URL만 잘 설계하고 HTTP 메서드만 잘 사용하면 됨)

### HTML은 대부분 RESTful함

- HTML은 각 태그들의 역할이 HTML 명세에 잘 설명되어 있으므로 Self-Descriptive 만족
- HTML은 a 태그(링크 태그)를 통해 다른 리소스로 전이가 가능하므로 HATEOAS 만족

### JSON은 대부분 RESTful하지 않음

- JSON은 JSON 명세에 JSON의 구조와 이에 따른 파싱 방법만이 설명되어 있을 뿐 JSON을 구성하는 key/value는 상황에 따라 다름. 따라서, 제공되는 key/value에 대한 문서 또는 문서로의 경로를 제공하는 게 아니고서야 Self-Descriptive 라고 볼 수 없음
- JSON은 대부분 다른 상태로의 전이를 위한 리소스를 제공하지 않으므로 HATEOAS를 만족하지 않음

## Reference

[REST - What exactly is meant by Uniform Interface?](https://stackoverflow.com/a/26049761)

[Day1, 2-2.  그런 REST API로 괜찮은가](https://www.youtube.com/watch?v=RP_f5dMoHFc)
