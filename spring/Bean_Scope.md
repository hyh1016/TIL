
# 🍃 빈의 생성과 관리 범위 (SingleTon, Prototype)

## Singleton

클래스의 인스턴스가 단 하나만 생성되도록 하는 디자인 패턴을 말한다.

IoC Container 내부의 Bean들은 대부분 Singleton으로 관리된다. 즉, 한 번만 생성되고 이것을 getter를 통해 여러 곳에서 주입받아 이용하는 방식으로 운영된다.

## Prototype

빈의 범위를 프로토타입으로 지정하면 getBean 메서드를 호출할 때마다 새로운 객체를 생성하여 반환한다.

프로토타입 범위의 빈은 일반적이지 않은 것이기 때문에 빈의 생명주기를 따르지 않는다. 스프링 컨테이너의 소멸 시점에 함께 소멸되지 않기 때문에 별도의 소멸 처리 코드를 작성해야 한다.

## 관리 범위 지정

@Scope 어노테이션을을 이용하면 된다.

```java
@Bean
@Scope("singleton") // default

@Bean
@Scope("prototype") // prototype
```