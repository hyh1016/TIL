# Browser Caching

## 필요한 HTTP Header

브라우저 캐싱을 도입하기 위해서는 아래의 헤더들이 설정되어야 한다.

### Cache-Control

* 브라우저의 캐싱 방법을 정하기 위해 서버/클라이언트가 사용하는 HTTP Header
* 캐시의 저장 여부, 유효 시간 등을 지정할 수 있음
* 자주 사용하는 디렉티브(directive) 목록
  * public/private: public은 이 리소스를 받는 모든 주체가 캐싱을 하도록 하고, private는 오직 end-user(마지막 수신자)만이 캐싱을 하도록 함
  * must-revalidate: 반드시 재검증을 거쳐 캐시된 리소스를 사용하도록 함
  * max-age=: 캐시가 유효하다고(최신 상태라고) 판단할 최대 시간

### E-Tag

* 리소스를 식별하는 식별자 역할을 하는 HTTP Header
* response header에 이 값이 포함되면, client(browser)는 이 값을 기준으로 리소스를 캐싱하고 변경 여부를 판단
* Cache-Control 헤더와 함께 사용하여 브라우저에 해당 리소스를 캐싱하도록 사용할 수 있음

## 브라우저 캐싱 동작 흐름

response header에 다음과 같은 value들이 설정되었다고 할 때, 브라우저 캐싱이 어떻게 동작하는지 알아보자.

```js
Cache-Control: public, max-age=180
ETag: "33a64df551425fcc55e4d42a148795d9f25f89d4"
```

1. 서버가 리소스를 제공할 때 응답 헤더에 적절한 ETag 값을 포함
   * 여기서 적절한 ETag란, 리소스별로 고유하게 부여될 수 있는 값을 말함
   * MDN에서 제안하는 ETag 후보들
     * 컨텐츠 자체의 hash
     * 마지막 수정 일자(타임스탬프)의 hash
2. 브라우저는 ETag를 기반으로 Cache-Control에 정의된 매커니즘에 기반하여 캐시를 저장
   * 위의 설정대로면 이 리소스를 받는 모든 주체가 180초 동안 캐시를 저장하도록 함
3. 브라우저는 캐시된 데이터를 사용하기 전 캐시가 만료되었는지를 먼저 확인
   * 캐시의 유효 기간을 설정하는 방법은 Cache-control 헤더에 max-age 를 설정하는 방법과 Expires 헤더를 설정하는 방법이 존재
     * max-age는 캐시가 등록된 시점을 기준으로 만료 시간을 지정
     * Expire는 캐시가 만료될 시점을 지정
4. 만약 캐시가 만료되지 않았다면, 서버에 요청을 보내지 않고 캐시를 사용
5. 캐시가 만료되었다면, 브라우저는 If-None-Match 헤더에 ETag 값을 담아 서버에 요청을 보냄
6. 서버는 5번에서 보낸 헤더의 값과 현재 리소스의 ETag 값을 비교해 두 값이 일치하는 경우 304 Not Modified와 함께 빈 body를, 일치하지 않는 경우 200 ok와 함께 새 리소스를 반환

## 여담

* 브라우저 캐시를 이용하면 자주 변경되지 않지만 자주 조회되는 리소스에 대한 트래픽을 절감할 수 있다.
* 그러나, 캐시 메커니즘을 어떻게 설정하느냐에 따라 이미 서버에서는 리소스가 변경되었음에도 브라우저는 변경 이전의 리소스를 캐싱하고 이를 계속 제공하는 상황이 발생할 수도 있다.
* 이를 예방하기 위해 나는 `must-revalidate` 디렉티브를 주로 사용한다. 이는 캐시의 만료 여부와 상관 없이 항상 서버에 유효성 검증을 위한 요청을 전송하도록 한다.
  * 매 순간 서버에 요청이 간다는 점에서 캐시의 혜택을 모두 누리지 못하게 된다고 볼 수도 있겠지만, 캐시가 유효한(최신의) 것일 때에는 서버가 리소스 전체를 제공하는 대신 304 응답과 함께 “리소스가 변경되지 않았음”만을 제공하기 때문에, 오가는 데이터의 양을 줄일 수 있다는 점에서 여전히 의미가 있다.

## 출처

* [MDN - Cache Control](https://developer.mozilla.org/ko/docs/Web/HTTP/Headers/Cache-Control)
* [MDN - ETag](https://developer.mozilla.org/ko/docs/Web/HTTP/Headers/ETag)
* [토스 기술 블로그 - 웹 서비스 캐시 똑똑하게 다루기](https://toss.tech/article/smart-web-service-cache)
