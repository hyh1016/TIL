# 📜 Facade Pattern

## Facade Pattern

클라이언트(시스템을 이용하려는 객체)가 복잡한 시스템을 간편하게 이용할 수 있도록 간략화된 인터페이스(API)를 제공해주는 디자인 패턴

이 인터페이스를 `Facade(퍼싸드)`라고 부른다.

### 구성

![Facade](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/fa61e6a2-de8b-44e1-8101-9c7c411f3f4c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220406%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220406T061454Z&X-Amz-Expires=86400&X-Amz-Signature=0cf86f7c360838c137662c62bc04bdbf29cf68cfb8b9aa2f8dc363b479202ed1&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

- `System` - 복잡한 로직들을 포함한 여러 클래스들. 각자의 책임을 수행
- `Facade` - 이 System을 적절히 호출하여 클라이언트에게 사용하기 편한 인터페이스(API)를 제공
- `Client` - System과 직접적으로 연결되지 않고, Facade를 통해 System 내 기능을 이용

### Facade의 이점

- 시스템 인터페이스(Facade)를 구현하는 사람을 제외하고는 복잡한 내부 시스템을 이해하지 않아도 된다. (은닉을 통한 효율성)
- 시스템을 간소화할 수 있다.
- 시스템의 일부만을 Facade와 연결하여 시스템을 부분집합 형태로 사용할 수 있다.
