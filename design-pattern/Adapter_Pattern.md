# ✒ Adapter Pattern

## Adapter Pattern (어댑터 패턴)

호환성 문제로 함께 사용할 수 없는 것들을 함께 사용하기 위해 어댑터를 정의하는 것을 어댑터 패턴이라고 한다.

### 구성

- `Client` - Adaptee를 이용하고자 하는 객체를 뜻한다.
- `Target (Interface)` - 원래라면 Adaptee와 직접적으로 연결되어야 하나 호환성 문제로 연결되지 않는 상위 개념
- `Adapter` - Target을 구현하고 Adaptee의 기능을 이용하는 어댑터
- `Adaptee` - 이용하고자 하는 클래스. 보통 레거시 코드나, 내부를 건드릴 수 없는 경우(외부 라이브러리 등) 등이 이에 해당

### 종류

- Class Adapter
- 오브젝트 어댑터

## Class Adapter (클래스 어댑터)

![Class-Adapter](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/cdf8aa29-5204-4586-9dad-56c349c86529/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220405%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220405T133500Z&X-Amz-Expires=86400&X-Amz-Signature=b7e6310162920d634c6162688079507c1d09a6a859be9b5c29821318e29da835&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

Adapter가 Adaptee를 상속함으로써 Adaptee의 기능을 호출한다.

## Object Adapter (오브젝트 어댑터)

![Object-Adapter](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/de100d7c-f6a2-42e0-b582-c03ae70a93c7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220405%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220405T133454Z&X-Amz-Expires=86400&X-Amz-Signature=c43b38a3cfaadb3385c9b5e64612b53c5fae034b2fcd551e16bc1a91b48210a8&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

Adapter가 Adaptee를 참조함으로써 Adaptee의 기능을 호출한다.

## Class Adapter vs Object Adapter

클래스 어댑터의 경우 상속을 통해 Adaptee를 이용하므로, 컴파일 타임에 Adaptee가 결정된다.

따라서 여러 개의 Adaptee를 사용하는 데에 무리가 있다.

객체 어댑터의 경우, Adaptee를 생성자 등에 의해 주입받아 field에 저장하기 때문에, Adaptee를 동적으로 교체할 수 있다.
따라서 여러 개의 Adaptee를 이용할 수 있으므로, Adaptee의 개수가 여러 개라면 객체 어댑터를 선택하는 것이 좋다.
