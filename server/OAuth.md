# 🛡️ OAuth

## 정의

<img width=300 src="https://user-images.githubusercontent.com/59721541/148330483-27a4a07a-b0db-46dd-9479-3a1751142e9a.png" />

사용자들이 제3자 서비스의 계정을 통해 인증을 수행할 수 있도록 접근 위임을 제공하는 **공통 표준(open standard) 인증방식**

여기서 제3자 서비스란 Google, Facebook, Github 등을 포함한다.

## 장점 (문제 해결)

- 기존에는 제3자 서비스의 계정을 이용하기 위해 본 서비스와 제3자 서비스에 모두 사용자의 아이디/비밀번호를 제공해야 함 ⇒ 보안 측면에서 손해 (하나 털리면 다 털림!)
    - OAuth를 이용하면 사용자가 입력한 사용자의 개인 정보가 아닌 임의로 생성되는 값인 `accessToken`을 이용해 인증을 수행하기 때문에, 두 개 서비스 모두에 개인 정보를 제공할 필요가 없다.
- 제3자 서비스의 아이디/비밀번호를 제공하는 형식에서는 본 서비스가 이를 남용할 우려가 있었다.
    - OAuth를 이용하면 허용할 권한을 제한할 수 있고, 사용자가 인증 과정에서 이 권한이 무엇인지 확인할 수 있다.

## 용어

- `Resource Owner` - 사용자. Resource(개인 정보)의 소유자
- `Resource Server` - 제3자 서비스. Resource(개인 정보)를 가지고 있으며, 제공하는 주체
    - `Authorization Server` - OAuth를 제공하는 제3자 서비스에 속한, 인증 관련 처리를 담당하는 서버
- `Client` - 이용하려는 서비스. Resource Server에 접근하여 데이터를 얻고 활용하는 주체

## 인증 흐름

> OAuth 인증을 통한 로그인을 제공하는 Client 입장에서의 인증 흐름은 다음과 같다.

1. OAuth 인증 방식을 제공하기 위해 인증 서버를 제공하는 리소스 서버에 내 서비스를 등록한다.
2. 리소스 서버는 차후 등록된 서비스의 인증을 위해 `Client ID`, `Client Secret`을 발급한다.
3. 사용자가 OAuth 로그인(구글로 로그인, 카카오로 로그인 등)을 요청한다.
4. 내 서버는 이를 받아 사용자를 인증 서버가 제공하는 인증 페이지로 이동시킨다.
이 때 인증 서버에는 클라이언트 아이디, 권한을 부여받을 영역(scope), 인증 후 리다이렉트할 URL이 **GET** 요청의 파라미터로 제공되어야 한다.
    
    ```
    https://resource.server?client_id={클라이언트아이디}&scope=email,profile...&redirect_url=https://client/callback
    ```
    
1. 사용자가 인증을 수행(동의)하면 리소스 서버는 code를 발급한다.
code는 직전에 제공한 리다이렉트 URL로 사용자를 리다이렉트시키며 제공된다.
    
    ```
    https://client/callback?code={코드}
    ```
    
1. 내 서버는 이를 받아 인증 서버에 access token을 발급할 것을 요청한다.
이 때 인증 서버에는 Client ID, Client Secret, 직전에 발급한 code, 리다이렉트할 URL이 **POST** 요청의 파라미터로 제공되어야 한다.
    
    ```
    https://resource.server/token?code={코드}&client_id={클라이언트아이디}&client_secret={클라이언트시크릿}&redirect_url=https://client/callback
    ```
    
1. 리소스 서버는 클라이언트 아이디와 시크릿, 코드가 모두 일치하는지 확인하고 맞다면 access token을 발급하여 이를 포함한 JSON을 반환한다.
    
    ```
    {
    	"access_token": "액세스 토큰",
    	"token_type": "Bearer",
    	"expires_in": 유효 시간,
    	"refresh_token": "갱신을 위한 토큰"
    }
    ```
    
2. 내 서비스는 이 access token을 통해 리소스 서버가 제공하는 API를 사용할 수 있다.
access token은 헤더로 전송하거나 url의 파라미터로 전송하는데, 보안 면에서는 (당연히) 헤더로 전송하는 것이 좋다.
    
    ```
    GET /api/apiurl
    Authorization: Bearer <access token>
    ```
    
    헤더로 전송하기 위해 이 토큰은 사용자가 쿠키 또는 세션을 통해 갖고 있어야 한다.
    

## 재발급

![refresh-token](https://user-images.githubusercontent.com/59721541/148330540-ad2480a2-bad1-4a22-b097-52c130021f1b.png)

앞서 access token을 포함한 JSON의 형식을 보면, access token에는 유효 시간이 존재함을 알 수 있다. 이 유효 시간이 만료되면 리소스 서버는 해당 access token을 유효하지 않은 것으로 판단한다.

이 경우 내 서버는 refresh token을 통해 access token을 갱신한다. 이 과정에서 refresh token도 갱신될 수도 있고, 아닐 수도 있다.

## 역할

### 사용자

사용자는 다음을 수행한다.

1. 로그인을 시도 (구글로 로그인, 페이스북으로 로그인 등의 버튼을 클릭)
2. 인증에 동의함으로써 로그인에 성공한다.

### 개발자

개발자는 다음을 수행한다.

1. 리소스 서버에 자신의 서비스를 등록한다.
2. 클라이언트 ID, 클라이언트 Secret을 발급받아 서버가 이를 이용할 수 있도록 한다.
3. 인증 흐름의 4~8을 수행하기 위한 API를 구현한다.

이 과정을 단순화하는 다양한 라이브러리들이 존재한다. Spring Security, Passport 등이 이에 해당한다.

### 리소스 서버

리소스 서버는 사용자의 보안을 위해 다음과 같이 동작한다.

- authorization code는 한 번 갱신을 마친 뒤 소멸한다. 즉, 매 번 다른 code가 발급된다.
- access token을 발급받기 위해서는 리소스 서버가 소유한 client id, client secret, authorization code와 개발자가 파라미터로 넘긴 세 개의 값이 모두 일치해야 한다.
- access token에는 유효 기간이 존재한다. 이 기간이 지나면 리소스 서버에서 소멸하며, 재발급을 위해 refresh token을 이용해야 한다.

## Reference

[OAuth - 위키백과](https://ko.wikipedia.org/wiki/OAuth)

[OAuth 2.0 rfc](https://datatracker.ietf.org/doc/html/rfc6749)

[생활코딩 WEB2 - OAuth](https://www.youtube.com/playlist?list=PLuHgQVnccGMA4guyznDlykFJh28_R08Q-)