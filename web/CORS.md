# CORS

## CORS (Cross-Origin Resource Sharing, 교차 출처 자원 공유)

### 정의

교차 출처(Cross Origin) 간 리소스 공유(Resource Sharing)의 약자

서로 다른 Origin을 갖는 애플리케이션 간에 리소스를 공유하고자 할 때 준수해야 할 규약들을 `CORS Policy` 라고 함

### 클라이언트 (리소스 요청자)

1. 프리플라이트 요청 (OPTIONS) 으로 지원하는 메소드, 헤더 정보 확인
   * [Simple Request](https://developer.mozilla.org/ko/docs/Web/HTTP/CORS#%EB%8B%A8%EC%88%9C\_%EC%9A%94%EC%B2%ADsimple\_requests) 인 경우에는 생략됨
   * 아래는 이 OPTIONS 요청에서 사용되는 헤더들
     * `Access-Control-Request-Method`
       * 사용 가능한 메소드인지를 응답받기 위한 헤더
     * `Access-Control-Request-Headers`
       * 사용 가능한 헤더인지를 응답받기 위한 헤더
2. 프리플라이트 요청을 기반으로 실제 요청 전달
   * 애플리케이션을 구현할 때에는 실제 요청만을 작성하며, `Fetch` 등의 요청 메소드가 프리플라이트를 자동으로 트리거

### 서버 (리소스 제공자)

* 프리플라이트(OPTION) 요청에 대해서는 다음의 헤더를 통해 지원하는 메소드, 헤더 정보 제공
  * `Allows` 또는 `Access-Control-Allow-Methods`
  * `Allow-Headers` 또는 `Access-Control-Allow-Headers`
* 허용된 클라이언트인지 검증
  * 허용된 헤더라면 `Access-Control-Allow-Origin` 헤더를 포함한 응답 제공
  * 프리플라이트, 실제 요청 모두 이 과정(헤더)이 요구됨

### 서버-클라이언트 요청 흐름

1. 클라이언트 — 프리플라이트 요청
   * [Simple Request](https://developer.mozilla.org/ko/docs/Web/HTTP/CORS#%EB%8B%A8%EC%88%9C\_%EC%9A%94%EC%B2%ADsimple\_requests) 인 경우에는 생략됨 (중요하므로 한 번 더 강조)
2. 서버 — 프리플라이트 요청에 대한 응답 (사용 가능 메소드, 헤더 정보 포함)
3. 클라이언트 — 서버의 응답 기반으로 실제 요청 메시지 생성
4. 서버 — 실제 요청에 대한 응답

### 인증 요청인 경우

* 클라이언트 — `withCredentials: true`
  * 이걸 포함해야 헤더에 쿠키 정보를 넣음
* 서버 — `Access-Control-Allow-Credentials: true`
  * 브라우저는 인증 요청에 대한 응답 헤더에 이게 없으면 파기
  * 서버에서 이 헤더를 포함하고자 하면 `Allow-Origin` 은 와일드카드로 설정 불가

### 주의사항

* CORS는 기본적으로 무조건 요청에 `origin 정보`가 있어야 허용해줄 수 있음
  * 리소스를 요청한 오리진이 허용된 오리진인지 아닌지 판별해야 하므로 당연함

### 출처

\[MDN] [https://developer.mozilla.org/ko/docs/Web/HTTP/CORS](https://developer.mozilla.org/ko/docs/Web/HTTP/CORS)
