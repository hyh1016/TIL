# 도서명
### 우에노 센. 2015. [그림으로 배우는 HTTP & Network Basic](https://book.naver.com/bookdb/book_detail.nhn?bid=8657832)

# 목차
- [1장. HTTP의 탄생과 성장](#-1장-http의-탄생과-성장)
- [2장. HTTP Protocol의 구조](#-2장-http-protocol의-구조)
- [3장. 다양한 요청응답 동작](#-3장-다양한-요청응답-동작)
- [⭐ 4장. HTTP 상태 코드](#-4장-http-상태-코드)

# ✔ 1장. HTTP의 탄생과 성장

## [WWW (World Wide Web)](https://ko.wikipedia.org/wiki/%EC%9B%94%EB%93%9C_%EC%99%80%EC%9D%B4%EB%93%9C_%EC%9B%B9) 의 탄생

WWW는 Internet을 통해 접근 가능한 공용 웹 페이지의 상호 연결 **시스템**이다.

다음과 같은 기술들로 이루어진다.

- `HTML`: 문서 기술 언어
- `HTTP`: 문서 전송 프로토콜
- `URL`: 문서의 주소를 지정하는 방법

## HTTP를 이용한 서버 ↔ 클라이언트간 통신

### TCP/IP

단순히 TCP, IP만 가리키는 의미로보다는 전체 네트워크 계층을 가리키는 의미로 더 자주 사용됨.

### 계층별 역할

![그림1](https://user-images.githubusercontent.com/59721541/147726443-3359539d-48c9-4de7-88a6-a70ada668f57.png)

1. **애플리케이션 계층**
   - 어떤 프로토콜로 통신할지 결정
   - **HTTP, FTP, DNS** 등을 이용
2. **트랜스포트 계층**
   - 어떤 포트로 통신할지 결정 
   - **TCP**를 이용 (실시간성이 필요한 경우 UDP를 이용하기도)
   - 통신하기 쉽도록 메시지를 패킷 단위로 분해 (조각낸다는 의미에서 `Segmantation`이라고 부름)
       - 이후 일련 번호를 부여 **(순서 보장을 위함)**
   - `3 way handshaking`을 한다. **(데이터를 확실하게 보내기 위함)**
       - 연결을 시도하려는 A가 **SYN** packet을 보낸다.
       - 이를 받은 B가 **SYN/ACK** packet을 보낸다. (A가 이를 받을 시 A의 검증 완료)
       - 이를 받은 A가 **ACK** packet을 보낸다. (B가 이를 받을 시 B의 검증 완료)
3. **네트워크 계층**
    - 어떤 IP(HOST)로 통신할지 결정
   - **IP**를 이용
   - 라우팅을 통해 목적지로 전달
       - 라우터는 **자기 역할만 수행**한다.
       - 즉, **누가 자기에게 보냈는지**와 **자기가 어디로 보내야 할지**만 알고 있다.
4. **링크 계층**
   - 물리적 계층

## URI와 URL

### URI(Uniform Resource Identifier)

- `Uniform`: 통일된 서식의
- `Resource`: 식별 가능한 자료의
- `Identifier`: 식별자

### URL(Uniform Resource Locator)

- URI 중에서도 리소스의 `장소`를 나타내는 문자열 (그래서 Locator)
- 따라서 **URL ⊂ URI** 이다.

### ⭐ URL Format

![그림2](https://user-images.githubusercontent.com/59721541/147726587-f409a860-2fba-4589-9730-e62197aab1b2.png)

- **스키마: 어떤 프로토콜을 사용할 것인가?**
- 자격정보: 아이디와 패스워드를 지정 (옵션)
- **서버 주소: DNS명, IP 주소**
- 서버 포트: TCP에서 식별할 네트워크 포트 번호. (옵션)
    - 생략 시 default number가 부여.
    - **http는 80, https는 443**
- 계층적 파일 경로: 서버 상에서의 파일 경로 (옵션)
- 쿼리 문자열: 해당 리소스에 임의의 parameter를 넘겨주기 위해 사용 (옵션)
- 프래그먼트 (식별자): 해당 리소스의 서브 리소스를 가리키기 위해 사용 (옵션)

---

# ✔ 2장. HTTP Protocol의 구조

## 클라이언트와 서버

- HTTP 통신에서는 반드시 **Client(리퀘스트를 송신)** 와 **Server(리퀘스트에 대한 리스폰스를 송신)** 가 존재해야 한다.

## Request Message의 구성

- Request Message는 다음과 같이 구성된다.
    ```
    GET /foo/bar HTTP/1.1
    Host: example.com
    Connection: keep-alive
    Content-Type: application/...
    Content-Length: 16
    ...
    ```

- 리퀘스트 라인(Request Line)
    ```
    GET /foo/bar HTTP/1.1
    ```

    - **메소드, URI, 프로토콜 버전**으로 이루어진다.
    - URI가 *이면 서버가 자기 자신에게 요청을 보낸다는 뜻

- 리퀘스트 헤더(Request Header)
    ```
    Host: example.com
    Connection: keep-alive
    Content-Type: application/...
    Content-Length: 16
    ...
    ```

    - **key: value** 형식으로 이루어진다.
    - key는 대문자와 하이픈(-)으로 구성

## Response Message의 구성

- Response Message는 다음과 같이 구성된다.
    ```java
    HTTP/1.1 200 OK
    Date: Tue, 5 Jan 2021 15:46:16 GMT
    Content-Length: 362
    Content-Type: text/html

    <html>
    ...
    ```

- 스테이터스 라인(Status Line)
    ```
    HTTP/1.1 200 OK
    ```

    - **프로토콜 버전, 상태 코드, 상태 코드에 대한 설명**으로 이루어진다.

- 리스폰스 헤더(Response Header)
  
    ```
    Date: Tue, 5 Jan 2021 15:46:16 GMT
    Content-Length: 362
    Content-Type: text/html
    ```

- 리스폰스 바디 (Response Body)

    ```
    <html>
    ...
    ```

    - ⭐ **리스폰스 헤더와 공백(CRLF)으로 구분된다.**
    - **CRLF란?**
        - **CR(carriage return)**: 커서를 해당 줄의 맨 앞으로 이동
        - **LF(line feed)**: 커서를 다음 줄로 이동
        - **윈도우에서는 CRLF, 리눅스 계열에서는 CR이 필요없다고 판단하여 LF만 사용**

## 쿠키를 사용한 상태 관리

### 1. 리퀘스트 송신

- 이 때는 아직 쿠키가 없다.

### 2. 쿠키를 발행하는 리스폰스

- `Set-Cookie` 헤더를 포함한다.
- Set-Cookie 헤더는 쿠키명=쿠키값; 옵션명=값; ...으로 이루어진다.
    - 세미콜론(;)으로는 같은 쿠키 내에서 쿠키값, 옵션값 등을 지정
    - 컴마(,)로는 여러 쿠키를 구별

### 3. 쿠키를 보유한 리퀘스트 송신

- `Cookie: 쿠키명=쿠키값` 헤더를 포함한다.

## 응답 속도를 향상시키기 위한 노력

### 지속 연결

- HTTP 초기 연결은 `TCP 연결 → 1회 통신 → TCP 연결 종료`로 이루어짐
- HTTP 보급이 증가하며 통신도 증가하게 되고, 이 방식은 서버에 부하가 심해짐
- HTTP 1.1에서는 한 번 연결 시 직접 연결을 끊을 때까지는 연결이 지속되는 `지속 연결`을 도입

### 파이프라인화

- 지속 연결과 함께 도입된 `리퀘스트의 병렬 처리`

### 결론

속도는 `개별 연결 < 지속 연결 < 파이프라인화` 이다.

---

# ✔ 3장. 다양한 요청/응답 동작

## 메시지와 엔티티

### 메시지(Message)

- HTTP 통신의 기본 단위
- 엔티티의 운반을 위해 존재

### 엔티티(Entity)

- request/response의 payload(부가물)
- 헤더와 바디로 구성
- 메시지와 동일한 형태이나 인코딩을 적용할 시 엔티티 바디가 변한다.

## 데이터 인코딩

### 장점

- 다량의 엑세스 처리 효율 증가

### 단점

- CPU 등의 리소스 소비량 증가

### 데이터 인코딩의 종류

1. 용량 절감을 위한 압축 "콘텐츠 코딩"

   - 엔티티를 압축해서 송신
   - gzip, compress, deflate 등이 있다.

2. 데이터를 분할해서 보내는 "청크 전송 코딩"

   - 엔티티 바디를 청크(덩어리)로 분해

## 멀티파트

### 멀티파트란?

- 텍스트, 영상, 이미지 등 종류가 다른 데이터를 함께 전송하는 것을 말함

### 멀티파트의 종류

1. **`multipart/form-data`**: Web form에서 파일 업로드 시 사용
2. **`multipart/byteranges`**: 응답 메시지가 여러 종류 데이터를 포함한 경우 사용

### 멀티파트의 특징

- 파트마다 헤더 필드가 포함된다.
    - `Content-Type` 헤더 필드는 필수
- 바운더리 문자열로 각 엔티티를 구분한다.

## 레인지 리퀘스트

### 레인지 리퀘스트란?

- 범위를 지정해서 리퀘스트를 송신하는 기법
- 네트워크가 광대역이 아니던 시절, 데이터 다운로드 중 연결이 끊긴 상황을 고려한 기술
- **`Range: bytes=범위`** 헤더 필드를 이용

## 콘텐츠 네고시에이션

### 콘텐츠 네고시에이션이란?

- 클라이언트 상황에 따라 서로 다른 리소스를 제공하기 위한 기법
- **`Accept`, `Accept-Charset`, `Accept-Encoding`, `Accept-Language`, `Content-Language`** 등의 헤더를 이용하여 적합한 리소스를 제공

### 구현 방법

1. Server-driven Negotiation
    - 서버에서 리퀘스트 헤더 필드 정보에 따라 리소스를 선정하는 것
    - 사용자의 선택이 아니라 확실하다고 볼 수는 없음
2. Agent-driven Negotiation
    - 클라이언트 측에서 수동으로 네고시에이션
3. Transparent Negotiation
    - 서버와 클라이언트가 각각 콘텐츠 네고시에이션을 수행

---

# ✔ 4장. HTTP 상태 코드

## 상태 코드 (Status Code)

- 서버가 수행한 Response에 대하여 그 결과가 어떻게 되었는지 알려주는 역할

## Response Class

- 상태 코드는 세 자리 숫자와 설명으로 이루어진다.
- 이 중 첫 번째 자리는 Response Class를 의미하며 다음과 같이 분류된다.
- 또한 여기에는 대표적으로 사용되는 약 14개의 상태 코드가 있다.

### "1xx" Informational (리퀘스트를 받아 처리중)

### "2xx" Success (리퀘스트가 정상적으로 처리됨)

- **`200 OK`**: 정상 처리. 리소스 반환
- **`204 No Content`**: 정상 처리. 그러나 리소스가 없음
    - 반드시 어떠한 entity body도 포함해서는 안 됨
- **`206 Partial Content`**: 부분적 GET 요청에 대한 정상 처리

### "3xx" Redirection (리퀘스트를 완료하기 위해 추가 동작이 필요)

3xx 응답을 받은 경우 브라우저 측에서 특별한 처리(리다이렉트 등)를 수행해야 한다.

- **`301 Move Permanently`**: 해당 리소스에 영구적으로 새 URI가 부여된 경우
    - Location 이라는 헤더 필드에 리다이렉트할 새 URI가 지정됨
        
        ![그림1](https://user-images.githubusercontent.com/59721541/147728554-37dfca03-9024-418f-9082-958649fccc89.png)
        
- **`302 Found`**: 해당 리소스에 일시적으로 새 URI가 부여된 경우
- **`303 See Other`**: 새 URI가 부여되었으며 이를 GET 요청을 통해 얻어야 함
- **`304 Not Modified`**: 접근할 수 있는 리소스지만 조건이 안 맞음
    - 이 경우 반드시 Response Body가 비어있어야 함
- **`307 Temporary Redirect`**: 302와 같으나 내부 구현이 다름 (네이버는 이걸 쓰고 있다)

### "4xx" Client Error (리퀘스트를 이해할 수 없음 - 클라이언트 잘못)

- **`400 Bad Request`**: 잘못된 리퀘스트
    - 리퀘스트 재검토 후 재송신해야
    - 브라우저는 이를 200 OK와 동일하게 취급
- **`401 Unauthorized`**: 해당 리소스에 접근하기 위해서는 인증 정보가 필요함
    - Response Message에 WWW-Authenticate 헤더 필드를 포함해야 함
    - 클라이언트 대응1 - 인증 페이지를 띄움
    - 클라이언트의 대응2 - 대응 1이 이미 이루어진 경우 인증 실패 메시지를 표시
- **`403 Forbidden`**: 액세스할 수 없는 리소스
    - 파일 시스템의 퍼미션이 부여되지 않은 경우
    - 액세스 권한 문제(허가되지 않은 IP 등)
- **`404 Not Found`**: 존재하지 않는 리소스

### "5xx" Server Error (서버의 리퀘스트 처리 실패 - 서버 잘못)

- **`500 Internal Server Error`**: 서버에서 리퀘스트 처리 중 에러 발생 (서버 살아있긴 함)
- **`503 Service Unavailable`**: 서버가 아예 죽음 (과부하, 점검 등의 이유로)

---

