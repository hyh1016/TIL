# application/octet-stream

## Content-Type

- HTTP 프로토콜로 데이터를 주고받을 때, Content-Type 헤더가 등장하면서 여러 형식의 데이터를 주고받을 수 있게 되었다.
- Content-Type의 value로는 MIME 타입 형식의 데이터가 제공된다. MIME 타입의 종류는 **Discrete types과 Multipart types로 분류되며,** 그 종류는 아래와 같다.
    - Discrete Types(개별 타입)
    - Multipart Types(멀티파트 타입)
- 개별 타입은 동일 포맷의 데이터만을 전송할 때 사용하며, 멀티파트 타입은 여러 포맷(plain text, binary 등)을 동시에 존재할 때 사용한다.

## application/octet-stream

- 알려지지 않은 타입의 리소스를 전송할 때 사용하는 Content-Type
- byte 단위의 알 수 없는 binary data를 전송하기 위해 사용한다.
- 보안상의 이유로 해당 타입으로 전송된 리소스는 브라우저에서 기본 동작을 허용하지 않고, 사용하기 위해서는 디스크에 저장할 것을 강제하고 있다.
- 위와 같은 이유로 이미지, 동영상 등을 해당 타입으로 지정해 전송하면 브라우저에서 자동 실행되지 않는 문제가 발생한다.
    - 이를 해결하기 위해서는 명시적 MIME 타입을 지정해주어야 한다. (image/png, audio/midi와 같은 타입)

## Content-Disposition

- 제공되는 데이터의 용도를 알려주는 헤더
- `application/octet-stream`을 사용할 때, `Content-Disposition: attachment`와 함께 사용함으로써 저장될 파일명을 지정해줄 수 있다.
- 주로 AWS S3를 다룰 때 이 방식을 많이 이용한다. s3의 경우 여러 타입의 파일을 저장할 수 있는 파일 스토리지이기 때문에 기본적으로 Content-Type이 `application/octet-stream` 으로 지정되고, 이를 실제로 다운로드 용도로 사용하는 경우 Content-Disposition 헤더와 함께 사용해 저장될 파일명을 지정한다.

## Reference

- [MDN - MIME 타입](https://developer.mozilla.org/ko/docs/Web/HTTP/Basics_of_HTTP/MIME_types#%EC%A0%95%ED%99%95%ED%95%9C_mime_%ED%83%80%EC%9E%85_%EC%84%A4%EC%A0%95%EC%9D%98_%EC%A4%91%EC%9A%94%EC%84%B1)