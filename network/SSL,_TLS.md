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

## Reference

[https://aws.amazon.com/ko/compare/the-difference-between-ssl-and-tls](https://aws.amazon.com/ko/compare/the-difference-between-ssl-and-tls/)