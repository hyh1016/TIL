# 🌈 multipart/form-data

## Content-Type

- HTTP 프로토콜로 데이터를 주고받을 때, Content-Type 헤더가 등장하면서 여러 형식의 데이터를 주고받을 수 있게 되었다.
- Content-Type의 value로는 MIME 타입 형식의 데이터가 제공된다. MIME 타입의 종류는 **Discrete types과 Multipart types로 분류되며,** 그 종류는 아래와 같다.
    - Discrete Types(개별 타입)
        
        ```
        text/plain
        text/html
        image/jpeg
        image/png
        audio/mpeg
        audio/ogg
        audio/*
        video/mp4
        application/octet-stream
        …
        ```
        
    - Multipart Types(멀티파트 타입)
        
        ```
        multipart/form-data
        multipart/byteranges
        ```
        
- 개별 타입은 동일 포맷의 데이터만을 전송할 때 사용하며, 멀티파트 타입은 여러 포맷(plain text, binary 등)을 동시에 존재할 때 사용한다.

## multipart/form-data

- 멀티파트 타입의 데이터를 주고받는 요청 중 `Form Data`를 주고받는 요청에 해당한다.
- 주로 Form Data를 통해 text와 file을 함께 전송해 둘 간의 타입이 달라 개별 타입을 이용할 수 없을 때 해당 타입을 이용한다.
    - text는 plain/text, file은 이미지의 경우 image/jpg나 image/png와 같은 타입을 가진다.
    - 오직 plain/text만 전송하는 Form Data Request의 경우 `application/x-www-form-urlencoded` 타입을 이용하는 편이 더 효율적이고 명시적이다.
- 해당 타입으로 데이터를 전송할 때에는 전송 데이터의 encoding type도 multipart/form-data로 지정해주어야 한다.
    - Content-Type이 따르면 인코딩 로직도 다른데, 여러 타입의 데이터를 전송할 것이므로 전송되는 데이터를 인코딩하지 않기 위해서이다.

## multipart/form-data 전송 방법

- `Content-Type` 헤더에 `바운더리(boundary)`로 어떤 문자열을 사용할지 지정하고, 해당 바운더리로 데이터를 구분한다.
- 각 데이터별로 개별 타입을 명시해야 하며 하며, 바이너리 데이터의 경우 파일명도 명시해야 한다.
- 정리하자면 아래와 같은 형식을 갖는 것을 알 수 있다.
    
    ```html
    Content-Type: multipart/form-data; boundary=boundary로 사용할 문자열
    
    boundary로 사용할 문자열
    Content-Disposition: form-data; name=input name으로 지정된 문자열
    
    (데이터)
    boundary로 사용할 문자열
    Content-Disposition: form-data; name=input name으로 지정된 문자열
    
    (데이터)
    ...
    ```
    

### 예시

```html
<form action="http://localhost:8000/" method="post" enctype="multipart/form-data">
  <input type="text" name="myTextField">
  <input type="checkbox" name="myCheckBox">Check</input>
  <input type="file" name="myFile">
  <button>Send the file</button>
</form>
```

위와 같은 form data를 multipart/form-data로 전송한다면, 결과는 아래와 같다.

```
...other headers
Content-Type: multipart/form-data; boundary=---------------------------8721656041911415653955004498

-----------------------------8721656041911415653955004498
Content-Disposition: form-data; name="myTextField"

Test
-----------------------------8721656041911415653955004498
Content-Disposition: form-data; name="myCheckBox"

on
-----------------------------8721656041911415653955004498
Content-Disposition: form-data; name="myFile"; filename="test.txt"
Content-Type: text/plain

Simple file.
-----------------------------8721656041911415653955004498--
```

## Reference

- [MDN - MIME 타입](https://developer.mozilla.org/ko/docs/Web/HTTP/Basics_of_HTTP/MIME_types)