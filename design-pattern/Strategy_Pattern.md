# 📜 Strategy Pattern

## Strategy Pattern (스트래티지 패턴)

### 변경을 다루는 방법

일부를 수정했을 때 전체를 컴파일/빌드해야 하는 소프트웨어를 개발하는 것은 장기적 위험으로 이어진다. 따라서 변경을 위한 설계를 해야 한다.

이는 다음에 의해 이루어진다.

1. 추상적인 것(인터페이스)에 의존하고, 구체적인 것(구현물)에 의존하지 말아야 한다.
2. 상속(extend)보다는 집합(aggregation, 내부에 field로 포함하는 것)을 애용해야 한다.
3. 설계 시 변할 부분과 변하지 않을 부분을 잘 분리해야 한다.
    - 재설계의 원인이 무엇일지에 초점을 둔다.
    - 자주 변하는 개념은 캡슐화한다.

### 패턴 레벨에서 변경을 다루는 방법 - 스트래티지 패턴

`스트래티지 패턴`이란, 변하는 알고리즘 패밀리를 정의하고 각각을 캡슐화한 뒤, 이를 다른 클래스가 포함하게 만드는 설계 기법이다.

`스트래티지 패턴`은 동일한 문제를 다루는 여러 알고리즘이 하나의 인터페이스(Strategy)를 구현하도록 하여, 필요한 알고리즘으로 쉽게 대체할 수 있도록 한다.

### 구성 요소

![Strategy-Pattern](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/33f353f0-d0d1-4c27-b639-01aacb9401ed/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220605%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220605T014915Z&X-Amz-Expires=86400&X-Amz-Signature=f66e4071930a977bd93b20b0a0b5bbec75f205956d5ae39a34be57db37e62455&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

- `Context` - 전략을 이용하는 객체. 전략을 교체하기 위한 setter 메소드를 가진다.
- `Strategy` - 외부로부터 동일한 방식으로 알고리즘(전략)을 호출할 수 있도록 하기 위한 인터페이스/추상 클래스
- `ConcreteStrategy` - 구체적 알고리즘들이 정의되는 클래스

### 특징

- 단위 테스트에서 특정 컴포넌트(미개발)을 테스팅하고자 할 때 일단 Stub을 이용하고 이후 개발된 것으로 대체하기 위해 이 패턴을 사용할 수 있다.
