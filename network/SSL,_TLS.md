# SSL/TLS

## SSL/TLS

### 정의

- 호스트(장치, 애플리케이션) 간 통신에 있어 보안 연결을 생성하는 프로토콜
- 주고받을 데이터를 암호화해 이 데이터들이 유출되지 않는다는 신뢰성을 제공하기 위해 사용
- `SSL`의 보안 결함이 발견되고, SSL 취약성을 보완한 업그레이드 버전 프로토콜 `TLS`가 등장해 현재에는 주로 TLS가 사용됨
    - TLS는 HMAC을 사용하며, 보안 취약점이 아직 발견되지 않은 고급 암호화 알고리즘을 사용
    - TLS는 SSL보다 핸드셰이크 단계도 적어 연결 속도도 더 빠름
- 현재 기준 TLS 최신 버전은 1.3이며, 1.1 이하로는 공식적으로 더이상 사용되지 않아 1.2 이상의 버전을 사용해야 함

### SSL/TLS의 사용 예시 - HTTPS

- HTTP - 클라이언트/서버 간 통신을 위한 프로토콜
- HTTP는 데이터를 평문으로 주고받기 때문에 유출 위험 존재
- HTTP 연결에 SSL/TLS 프로토콜 설정하면 보안 통신이 가능, 이를 HTTPS라고 함
    - 즉, HTTPS 자체가 새로운 프로토콜이라기보다는 HTTP 아래 계층에 SSL/TLS라는 보안 계층이 추가된 형태라고 볼 수 있음

### SSL/TLS 보안 연결 수행 과정

브라우저와 웹 서버 간 통신에서 보안 연결을 제공하는 서버와의 SSL/TLS 연결은 아래와 같은 순서로 이루어짐

1. 클라이언트가 서버에 SSL/TLS 연결을 위한 요청을 보냄
    - 임의의 난수값(client), 클라이언트가 지원하는 암호화 방식, 세션 아이디를 서버에 제공
2. 서버는 요청에 대한 응답으로 자신의 인증서, 지원하는 암호화 방식, 임의의 난수값(server)을 제공
3. 클라이언트는 서버의 인증서에 대한 유효성 검증을 수행
    1. 유효한 인증서인가? - 실제 믿을 만하 인증 기관에서 발급된 인증서인지
    2. 해당 서버의 인증서인가? - 인증서가 인증 기관이 해당 서버에게 발급해준 인증서가 맞는지
4. 유효성 검사에 통과했다면, 클라이언트는 대칭키 역할을 할 난수값을 생성해 서버의 공개키로 암호화해 서버에 전달
    - 이 난수값은 어떻게 생성되는가?
        - 1, 2번 과정에서 서로 주고받은 임의의 난수값을 조합하여  PMS(Pre Master Secret)라는 난수값을 생성
        - PMS 난수값, 1, 2번 과정에서 주고받은 2개의 난수값을 바탕으로 생성됨
5. 서버는 이를 자신의 비밀키로 복호화해 소유. 여기서부터 이 대칭키는 `세션키` 역할을 하게 됨
6. 이제 SSL/TLS 보안 연결이 수립되었으며, 클라이언트와 서버는 데이터를 세션키로 암호화/복호화하여 주고받음

### 어떻게 유효한 인증서인지 아는가?

- 인증서는 특정 CA(인증 기관)에 의해 발급되며, 해당 CA가 자신의 비밀키로 암호화해 생성함
- 즉, 인증서를 발급한 CA의 공개키를 통해 인증서가 복호화된다면 해당 인증서가 해당 CA에 의해 발급되었음을 검증할 수 있음
- 보통 우리가 사용하는 인증서는 중간 CA가 발급해 준 것으로, 중간 CA의 인증서 또한 그 상위 CA가 발급해준 것
- 즉, 우리는 중간 CA의 공개키로 우리의 인증서를 검증하고, 획득한 중간 CA 인증서를 상위 CA의 공개키로 검증하는 방식으로 마치 chain 처럼 검증을 수행할 수 있으며, 이를 **Chain of Trust(신뢰 체인**이라고 함
- 이렇게 상위 인증서들을 검증해나가다보면 최종적으로 루트 CA의 공개키를 통해 루트 CA가 이 인증 과정의 최초 인증자임을 검증해낼 수 있음
- 클라이언트(브라우저)는 신뢰 가능한 루트 CA들의 인증서 및 공개키를 내장하고 있으며, 서버 인증서의 루트 CA가 자신이 가진 루트 CA 목록에 포함되면 인증서가 유효하다고 판단

### 어떻게 서버의 인증서인지 아는가?

- 서버의 공개키로 복호화한 서버의 인증서 내에 인증서 소유 도메인 정보 등이 포함되어 있음
- 클라이언트는 이 인증서 내부 데이터를 보고 인증서 소유 도메인이 요청을 보내려는 서버와 일치하는지 확인하여 서버의 인증서임을 판단

### 무료 인증기관, Let’s Encrypt

- 대부분 CA는 운영 비용 충당을 위해 인증서를 유료로 발급하지만, 일부 CA는 무료로 인증서를 발급해 줌
- 그 중 가장 주로 사용되는 CA가 Let’s Encrypt이며, 해당 기관은 인증서를 무료 발급해 모든 웹 사이트가 비용 문제로 인증서 발급을 포기하지 않고 암호화된 통신할 수 있도록 하는 것을 목적으로 함
- 해당 기관은 인증서의 생성, 디지털 서명, 설치 등 프로세스를 자동화시켜 많은 인증서 발급 요청에 대한 대응을 **자동화**
- 자동화이기 때문에 엄격한 심사 단계를 거치기 어려워 DA(도메인 유효성 검사)만 수행하며, 해당 CA가 발급하는 인증서는 암호화된 통신을 통해 중간에 데이터가 탈취되거나 변조되는 공격 등을 막는 것이 목적이지 “이 인증서를 가진 사이트는 신뢰 가능한 사이트로 피싱 사이트 등이 아니다”를 의미하는 역할을 해주지는 않는다고 함
    
    [The CA's Role in Fighting Phishing and Malware](https://letsencrypt.org/2015/10/29/phishing-and-malware)

## Reference

[https://aws.amazon.com/ko/compare/the-difference-between-ssl-and-tls](https://aws.amazon.com/ko/compare/the-difference-between-ssl-and-tls/)
[https://gruuuuu.github.io/security/what-is-x509](https://gruuuuu.github.io/security/what-is-x509/)