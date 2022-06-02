# 📜 Abstract Factory Pattern

## Abstract Factory Pattern (추상 팩토리 패턴)

![Abstract-Factory](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/09c478a2-bda9-40be-ae1b-b55b6ad20c90/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220530%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220530T084700Z&X-Amz-Expires=86400&X-Amz-Signature=daef8454cb07005ab387b333f20f7f636529803a1479722b7e6cfe9587574d96&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

해당 패턴은 [팩토리 메소드 패턴](./Factory_Method_Pattern.md)과 함께 보는 것이 좋다.

팩토리 메소드 패턴을 이용하면 인스턴스를 생성할 책임을 분리하여 새로운 서브타입이 추가되어도 팩토리 클래스만 수정될 뿐 팩토리 객체를 이용하는 클래스는 수정되지 않는다.

추상 팩토리 패턴은 팩토리 메소드에서의 Product가 여러 구성요소로 이루어질 때, 이 **구성 요소들의 조합체를 만드는 팩토리를 정의**하는 것이다.

### 구성 요소

- `AbstractFactory` - Product를 생성하기 위한 클래스를 추상화한 것. 기존에 Product의 서브타입을 생성하던 객체(Client)가 이에 의존하게 되어 구체적인 것이 아닌 추상적인 것에 의존하도록 설계를 변경한다.
- `ConcreteFactory` - 각 (클라이언트가 요구하는) 완성물 내 부품들을 만들고 조합하기 위한 팩토리
- `AbstractProduct` - 각 완성물 내 부품들
- `Product` - 각 부품들의 서브타입

### 특징

- 사실상 팩토리 메소드 패턴을 한 번 더 캡슐화하는 과정에 가깝다.
- 각 팩토리의 인스턴스는 하나씩만 생성하면 되기 때문에 싱글톤과 함께 쓰일 때가 많다.

### 팩토리 메소드와 추상 팩토리

삼성, LG 컴퓨터를 제조, 판매하는 컴퓨터 제조 업체에서 팩토리 메소드, 추상 팩토리 패턴을 적용한다고 하자.

그렇다면 어떤 회사 컴퓨터의 주문이 들어왔냐에 따라 분기를 나누어 삼성 또는 LG 컴퓨터의 인스턴스를 생성해야 한다. 여기서 관련이 없는 객체가 컴퓨터 서브타입의 추가/제거에 영향을 받지 않기 위해 인스턴스 생성 및 반환 책임을 분리하는 `팩토리 메소드 패턴`이 적용될 수 있다.

또한, 컴퓨터에는 모니터, 키보드, 마우스와 같은 부품이 포함되어야 한다. 마찬가지로 각 부품 요소에 대해 팩토리 메소드 패턴을 이용하는 경우에는 모니터 팩토리, 키보드 팩토리, 마우스 팩토리를 생성해야 한다.

그러나 사실 컴퓨터를 구성하는 부품은 저기서 끝이 아니다. 수많은 부품에 대해 모두 팩토리를 만들게 되면 이는 코드를 복잡하게 만들고, 팩토리 클래스의 빈번한 수정을 야기한다.

여기서 추상 팩토리 메소드 패턴을 적용하여 삼성 컴퓨터의 부품을 생성, 조립하는 팩토리와 LG 컴퓨터의 부품을 생성, 조립하는 팩토리를 만든 뒤 여기서 부품을 생성하고 조립한다.

최종 클래스 다이어그램은 다음과 같이 형성된다.

![Abstract-Factory-Example](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/9b8194c3-b6ce-4afc-96ab-4fa83e724ec2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220530%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220530T084704Z&X-Amz-Expires=86400&X-Amz-Signature=4fb5c999bf793f0217c505998290858fbd16ed0d58970117212f5e1d1e869133&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)
