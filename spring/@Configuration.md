# 🍃 Configuration

## 정의

Spring에서 Bean 등록 등을 수행하는 설정 파일을 선언하기 위해 사용하는 어노테이션

기존에 xml로 관리하던 것을 더 용이하게 관리하기 위해 Annotation 기반의 관리 방식이 등장했다.

다음의 두 가지 역할을 수행한다.

- 클래스 내부에서 커스텀 빈을 등록할 수 있다.
- 해당 커스텀 빈들을 `싱글톤`으로 관리되도록 한다.
- Configuration 어노테이션이 명시된 해당 클래스 또한 빈으로 등록된다.

단순히 @Bean 어노테이션만 사용해도 IoC 컨테이너에 Bean으로 등록되는 것은 맞으나, 이 Bean을 싱글톤으로 관리하기 위해 @Configuration 어노테이션을 함께 사용한다.

## 사용법

```java
// Bean으로 등록하고자 하는 클래스 구현

public class Person {
	
	private String name;
	private String age;

	...

}
```

```java
// Config Class를 구현하고 내부에 Bean을 선언
// @Configuration 어노테이션에 의해 해당 Bean은 Singleton으로 관리됨

@Configuration
public class MyConfig {

	...
	
	@Bean
	public Person person() {
		return new Person();
	}
	
}
```

## 원리

- Configuration을 명시하지 않고 Bean을 등록하면 Bean이 선언된 클래스(MyConfig) 그 자체를 스프링 빈으로 등록한다.
- Configuration을 명시하고 등록하면 MyConfig를 생성하는 것이 아니라 Spring이 미리 정의해 둔 임의의 클래스가 MyConfig를 상속받도록 한 뒤 해당 클래스를 빈으로 등록한다. 이 임의 클래스에는 내부적으로 싱글톤 유지를 위한 로직이 존재한다.
    - 싱글톤 유지를 위한 로직?
        
        내부적으로 `프록시 패턴`을 이용하여 해당 빈이 없을 때에만 생성하여 반환하고 있을 때에는 생성된 빈을 반환하도록 설정된다. 이는 proxyBeanMethods 옵션 값을 false로 주어 해제할 수 있으며, 이 경우 싱글톤으로 관리되지 않고 getBean을 통한 빈 호출 시마다 새로운 빈이 생성된다.
        

## 출처

[https://castleone.tistory.com/2](https://castleone.tistory.com/2)

[https://mangkyu.tistory.com/234](https://mangkyu.tistory.com/234)