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

1. 애플리케이션 계층
   - 어떤 프로토콜로 통신할지 결정
   - **HTTP, FTP, DNS** 등을 이용
2. 트랜스포트 계층
   - 어떤 포트로 통신할지 결정 
   - **TCP**를 이용 (실시간성이 필요한 경우 UDP를 이용하기도)
   - 통신하기 쉽도록 메시지를 패킷 단위로 분해 (조각낸다는 의미에서 `Segmantation`이라고 부름)
       - 이후 일련 번호를 부여 **(순서 보장을 위함)**
   - `3 way handshaking`을 한다. **(데이터를 확실하게 보내기 위함)**
       - 연결을 시도하려는 A가 **SYN** packet을 보낸다.
       - 이를 받은 B가 **SYN/ACK** packet을 보낸다. (A가 이를 받을 시 A의 검증 완료)
       - 이를 받은 A가 **ACK** packet을 보낸다. (B가 이를 받을 시 B의 검증 완료)
3. 네트워크 계층
    - 어떤 IP(HOST)로 통신할지 결정
   - **IP**를 이용
   - 라우팅을 통해 목적지로 전달
       - 라우터는 **자기 역할만 수행**한다.
       - 즉, **누가 자기에게 보냈는지**와 **자기가 어디로 보내야 할지**만 알고 있다.
4. 링크 계층
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