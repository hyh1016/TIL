# WebSocket

## 등장 배경

HTTP 프로토콜을 이용한 통신은 기본적으로 단방향이다. `Client로부터 생성된 Request Packet이 서버에게 전달되면, 서버는 이에 대한 Reseponse Packet을 제공하는 방식`으로 통신이 이루어진다.

이러한 단방향 통신의 단점은 서버에 변화가 있더라도, `반드시 클라이언트가 요청을 해야 해당 변화를 확인할 수 있다`는 것이다. `웹소켓`은 서버가 `요청 없이도 클라이언트에게 데이터를 전송`할 수 있도록 `양방향 통신 환경을 제공`함으로써 이러한 단점을 해결한다.

## WebSocket (웹소켓)

### 정의

서버와 클라이언트 간 양방향 통신을 위한 `프로토콜`

`ws://`로 시작하며, TCP/IP 기반으로 동작한다.

### 동작 원리

1.  **클라이언트가 서버에게 핸드쉐이킹(websocket 연결을 위한 협상)에 해당하는 HTTP 요청 전송**

    ```sql
    GET /chat HTTP/1.1
    Host: example.com:8000
    Upgrade: websocket
    Connection: Upgrade
    Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==
    Sec-WebSocket-Version: 13
    ```

    * `HTTP 1.1` 이상의 버전을 사용해야 함
    * HTTP 메소드는 반드시 `GET`
    * `Upgrade: websocket` 헤더를 포함
    * `Connection: Upgrade` 헤더를 포함
    * 클라이언트/서버 간 인증을 위한 `Sec-WebSocket-Key` 헤더를 포함
    * 서버가 웹소켓 버전을 인식할 수 없는 경우 버전 명시를 위해 `Sec-WebSocket-Version` 헤더를 포함
2.  **서버는 1번 요청에 대한 응답을 전송**

    ```sql
    // Success
    HTTP/1.1 101 Switching Protocols
    Upgrade: websocket
    Connection: Upgrade
    Sec-WebSocket-Accept: s3pPLMBiTxaQ9kYGzzhZRbK+xOo=
    ```

    * 이제부터 웹소켓 프로토콜을 사용할 것이라는 상태 코드 `101`을 사용
    * 마찬가지로 `Upgrade`, `Connection` 헤더를 포함
    * 클라이언트의 `Sec-WebSocket-Key` 값을 [매직 스트링](https://en.wikipedia.org/wiki/Magic\_string)과 이어 붙이고 SHA-1 해시 알고리즘으로 암호화하고 base64로 인코딩한 값을 담은 `Sec-WebSocket-Accept` 헤더를 포함

    ```sql
    // Fail
    HTTP/1.1 400 Bad Request
    ```

    * 만약 연결에 실패했다면 서버는 즉시 `400`을 반환하고 즉시 소켓을 종료해야 함
3. **성공적으로 프로토콜이 웹소켓(ws)으로 변경된 경우, 이제 서버와 클라이언트는 언제든 메시지를 전송할 수 있다. (즉, 양방향 통신을 할 수 있다.)**
