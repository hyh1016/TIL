# 📜 Proxy Pattern

## Proxy Pattern (프록시 패턴)

![Untitled](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/24f96d81-504e-4aad-bb2e-eab44fd94048/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220509%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220509T074007Z&X-Amz-Expires=86400&X-Amz-Signature=e8807f30b0e12bbe63ad010e03511d7824efacc8e10cffc04725e81f19914cc8&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

특정 객체로의 접근을 조절하기 위해 `대리자(프록시)`를 세우는 것

많은 비용이 드는 기능은 사이에 프록시(간단한 객체)를 두고 필요할 때에만 실제 객체(복잡한 객체)로 대체

### 구성 요소

- `Proxy` - 대리자 객체. 실제 객체(RealSubject)에 대한 레퍼런스를 유지한다. 프록시를 통해 실제 객체에 대한 접근을 조절할 수 있다.
- `Subject` - 실제 객체와 프록시의 공통 인터페이스를 정의한다.
- `RealSubject` - 실제 객체이다.

### 종류

- `리모트 프록시` - 원래 객체가 다른 주소 공간에 존재하는 경우 이 사실을 숨길 수 있도록 프록시를 둠
- `가상 프록시` - 원래 객체가 매우 복잡한 경우 아주 단순한 프록시를 둠
- `프로텍션 프록시` - 원래 객체에 대한 접근 권한을 제어하기 위해 프록시를 둠
- `스마트 레퍼런스` - 원래 객체에 접근할 때 추가적인 액션을 수행하기 위해 프록시를 둠
