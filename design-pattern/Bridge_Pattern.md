# 📜 Bridge Pattern

## Bridge Pattern (브리지 패턴)

![Bridge-Pattern](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/8a9a055f-0e49-45e6-a19b-bb31fd3f8dbe/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220412%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220412T123306Z&X-Amz-Expires=86400&X-Amz-Signature=993c2d486b708868bd9cc16ba03330d70e6347973ba0bd05f6ec9fd00c911546&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

- `추상을 구현으로부터 분리`하여 독립적으로 변하게 하는 패턴
- 추상 클래스 `Abstraction`과 구현 인터페이스 `Implementor`는 포함 관계를 갖는데, 이 관계를 bridge라고 한다.
- 브리지 패턴은 주로 구현 단에서 변화가 잦을 때 사용한다.

### 구성

- 왼쪽에는 abstract class와 operation이 정의된다.
- 오른쪽에는 implement되는 여러 버전이 하나의 interface로 묶여 있다.

### Bridge & Adapter

브리지 패턴은 다음과 같이 어댑터 패턴과 함께 사용되는 경우가 많다.

![Bridge-Adapter](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/f0e72071-fcf8-42da-86b3-f9924972a165/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220412%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220412T123321Z&X-Amz-Expires=86400&X-Amz-Signature=b54a0be6b915b28c1942bca4024d264aa3c34a5c308804d9e08850871b778d5d&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

### 브리지 패턴 예시 - 도형(Shape)과 도형 그리기 도구(Drawing)

![Bridge-Example](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/fc38808c-7b41-45f6-90e7-2d1b7049fa4c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220412%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220412T123341Z&X-Amz-Expires=86400&X-Amz-Signature=e70d917cb92e5104a26944a1740a0c8c69c61465db09a9c400eabd654902a3a8&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

위와 같이 설계하면 추상 계층에서는 구현 계층의 인스턴스 draw를 통해 draw 메서드를 호출하기만 하므로, draw가 내부적으로 어떤 변화가 일어나든 draw 메서드의 명칭에만 변함이 없다면 변화를 신경쓰지 않아도 된다.
