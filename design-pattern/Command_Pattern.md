# 📜 Command Pattern

## Command Pattern (커맨드 패턴)

커맨드 패턴은 이름 그대로 여러 가지 명령(요청)이 호출되는 프로그램 설계를 위해 사용된다. 요청을 받는 객체들을 그룹화하여 다형성(은닉)을 적용하고, 호출했을 때 지정된 커맨드를 실행하도록 한다.

커맨드 패턴을 이용하면, 커맨드 호출을 요청하는 클래스의 변경 없이 커맨드를 확장/수정할 수 있도록 설계할 수 있음은 물론이고, 아래와 같은 부분에서 장점을 갖는다.

1. 객체의 action을 동적으로 설정할 수 있다. (참조하는 Command 객체를 변경함으로써)
2. 작업의 수행을 요청한 시점(Invoker 호출)과 수행되는 시점(Command 호출)을 분리할 수 있다.
3. 다음과 같은 명령을 구현할 때에 용이하다.
    - 뒤로가기(Undo) 기능
    - System의 수행 정도 기록 (Command 객체들이 수행될 때마다 기록을 남기게 할 수 있음)
    - 여러 커맨드 호출 (컴포지트 패턴을 적용한 MacroCommand 이용)

### 구성 요소

![Command-Pattern](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/4f8f2b78-073f-4657-b37a-6b7989fddc61/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220606%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220606T075854Z&X-Amz-Expires=86400&X-Amz-Signature=7e66f86093c41323897c03ecb459af4e98ddefd15ec3f13c35112bb97c070953&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

- `Invoker` - 커맨드의 실행을 요청하는 객체
- `Command` - 실행될 기능에 대한 인터페이스
- `ConcreteCommand` - 실제로 실행될 기능을 구현하는 클래스
- `Receiver` - 커맨드가 execute를 실행하는 과정에서 필요한 클래스 (optional)
    - Command의 execute는 단순히 receiver의 action을 유발하도록 구현될 수도 있고,
    receiver 호출 없이 내부에서 명령을 처리하도록 구현될 수도 있다.

### 특징

Client는 Receiver를 생성하고, ConcreteCommand에 이를 전달한 뒤 ConcreteCommand를 Invoker에 저장하는 역할을 수행한다. 이를 클래스 다이어그램으로 나타내면 아래와 같다.

![Command-With-Client](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/ba6a27a8-30d7-49bf-8608-4cb1636aee8c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220606%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220606T075855Z&X-Amz-Expires=86400&X-Amz-Signature=0715e05c079a1bb4aa15437f20355961364b22fb6494257bd96c2746070eed9b&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)
