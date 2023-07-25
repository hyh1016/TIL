# \[Error] Bean could not be injected because it is a JDK dynamic proxy

## 필요 선행 지식

* [Reflection](../java/Reflection.md)

## CGLIB vs JDK Dynamic Proxy

* 둘 다 모두 Spring에서 AOP 기능을 지원하기 위해 사용하는 프록시 생성 기법

### CGLIB

* 바이트코드를 조작해 클래스를 생성
* 본 객체를 상속하는 프록시 객체를 생성하고 멤버 객체로 타겟(실제 객체)을 소유
* 상속으로 동작하기 때문에, final이 부여되었거나 접근 제어자가 private인 메소드에는 적용할 수 없음

### JDK Dynamic Proxy

* 리플렉션을 이용
* 인터페이스를 구현하는 클래스를 생성하고, 멤버 객체로 타겟(실제 객체)을 소유
* AOP가 적용된 메소드 호출 시 프록시 객체에서 Advice 로직 전 or 후로 타겟 객체의 메소드를 호출해서 핵심 로직이 수행될 수 있도록 함
* Spring에서는 클래스가 하나 이상의 인터페이스를 구현하는 경우 이 클래스의 프록시는 JDK dynamic proxy 기법으로 생성

## Error - Bean could not be injected because it is a JDK dynamic proxy

* 해당 오류는, 인터페이스가 아닌 인터페이스의 구현 클래스를 주입받고자 할 때 발생
* 해당 오류에서 언급한 Bean이 CGLIB 기반으로 생성되도록 함으로써 이 오류를 해결할 수 있음
* Spring에서는 `proxyTargetClass` 라는 옵션을 통해 인터페이스를 구현하는 클래스의 프록시를 인터페이스 구현 기반으로 생성할지 클래스 상속 기반으로 생성할지를 지정할 수 있음
  * false (default): 인터페이스 기반
  * true: 클래스 상속 기반

## 여담

* 최근이 되어서야 AOP 공부를 했는데, AOP에 대한 지식 없이 이 오류를 만났으면 이해도 못하고 벙쪘을 것 같다.
* 역시 기본 개념이 중요하다…

## Reference

* [스택오버플로우 답변](https://stackoverflow.com/questions/45124660/the-bean-could-not-be-injected-as-a-type-because-it-is-a-jdk-dynamic-proxy-tha)
