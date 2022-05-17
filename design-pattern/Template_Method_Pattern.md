# 📜 Template Method

## Template Method (템플릿 메소드 패턴)

![Template-Method-Pattern](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/b7a7409f-16fd-4e70-ab5c-b26d5e9e4e92/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220517%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220517T144322Z&X-Amz-Expires=86400&X-Amz-Signature=01c5190c8a209aa7ba8ae81f00153dec818656e06582cf0db2a04bc6ca01892d&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

구체적인 구현 내용이 다르지만 기본 골격이 비슷한 프로그램을 설계할 때 기본 골격에 해당하는 알고리즘은 일괄적으로 관리하고 구체적인 부분의 구현은 미룰 수 있다면 재사용성이 좋은 설계를 할 수 있다. 이로부터 고안된 것이 템플릿 메소드 패턴이다.

### 구성 요소

- `template method` - 기본 골격에 해당하는 부분을 다루는 메소드
- `primitive method` - 개별적으로 차이가 발생하는 부분을 다루는 메소드. protected로 선언한다.

### 특징

- 일반적인 상속의 경우 하위클래스가 상위클래스 내 메소드를 호출하지만, 템플릿 메소드 패턴에서는 **상위클래스가 하위클래스가 구현한 함수를 호출**한다.
- 템플릿 메소드와 프리미티브 메소드의 네이밍을 대비되게 하는 것이 좋다. (구분을 쉽게 하기 위함)
- 프리미티브 메소드가 특정 객체를 생성한다면 팩토리 메소드 패턴과 함께 사용할 수 있다.
- 기본 골격이 되는 부분을 다루는 클래스는 `한 번만` 생성되어도 된다. 때문에 해당 패턴은 `싱글턴 패턴`과 함께 사용될 때가 많다.
