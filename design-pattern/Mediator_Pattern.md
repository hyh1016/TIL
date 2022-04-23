# 📜 Mediator Pattern

## Mediator Pattern (중재자 패턴)

다음과 같이 여러 클래스들이 서로 강하게 연결되어 서로를 참조하는 경우를 생각해보자.

![Mediator-Prev](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/37dbc9d1-05bf-4c27-be65-aae64fac9c91/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220423%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220423T140159Z&X-Amz-Expires=86400&X-Amz-Signature=346ba1bfe7fe3797c9cfcd5377748b5ecd9428b3fe6f1f3670f7e4ac3273897b&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

하나의 클래스에서 변경이 일어나면 연관된 다른 클래스에서도 수정이 일어나게 되기 때문에, `제어 흐름이 클래스마다 흩어져 있어` 새로운 클래스를 추가하기 복잡하다.

이러한 문제의 해결을 위해 각 클래스간 상호작용을 도맡아 처리할 클래스를 선언하는 것을 중재자 패턴이라고 하며, 이 클래스를 `중재자(Mediator)`라고 한다.

위의 클래스 다이어그램에 중재자 패턴을 적용한 결과는 다음과 같다.

![Apply-Mediator](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/f735c667-52bd-442c-b3f3-cf93864a2daa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220423%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220423T140220Z&X-Amz-Expires=86400&X-Amz-Signature=6b7516068c008abc29b90449f709dd46cd8016741b598646e800a587398300da&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

각 클래스는 중재자 클래스를 제외한 클래스와 연관 관계를 가지지 않는다. 대신 다른 클래스와 상호작용하고자 할 때 중재자를 호출해 이를 처리한다.

### 구현

![Mediator-Pattern](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/1677e862-b922-4ff4-be14-5126c1207366/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220423%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220423T140249Z&X-Amz-Expires=86400&X-Amz-Signature=781156c5634a2fff8e59707dea1b998977cc2e62393bb3a6d67d6431c95600bf&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

### 용어

- `Mediator` - 클래스 간 상호작용을 도맡아 처리하는 클래스
- `Colleague` - 중재자를 호출하는 클래스

### 장점

- M:N의 객체 관계를 M:1로 전환하여 클래스 간 연결을 느슨하게 할 수 있다. 이를 통해 변경에 대한 영향을 줄일 수 있다.
- 클래스 간 상호작용 자체를 `캡슐화`하여 변경의 영향을 줄인다.

### 주의할 점

클래스 간 상호작용을 하나의 클래스가 모두 담당하기 때문에 경우에 따라 중재자 클래스가 너무 복잡해져 유지보수가 어려워질 수 있다.
