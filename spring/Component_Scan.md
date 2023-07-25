# Component Scan

## 정의

```java
@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.TYPE)
@Documented
@Repeatable(ComponentScans.class)
public @interface ComponentScan {

	...

}
```

* Component Scan(컴포넌트 스캔)은 Bean으로 등록할 Component를 찾는 동작을 말한다.
* `@ComponentScan` 어노테이션은 @Component 어노테이션과 내부적으로 @Component 어노테이션을 포함하는 어노테이션(@Controller, @Service, Repository 등)이 사용된 클래스를 찾아 Bean으로 등록한다.
* 컴포넌트 스캔을 통해 빈을 등록하기 위해서는 @Configuration 어노테이션이 선언된 설정 파일에 `@ComponentScan` 어노테이션을 적용해야 한다.

## 빈의 이름 지정 방식

### Default

```java
@Component
public class MyClass {

}
```

빈의 이름을 별도로 지정하지 않은 경우 클래스의 이름 첫 글자를 소문자로 바꾼 이름이 빈 이름으로 사용된다. (위의 클래스로부터 생성된 빈의 이름은 myClass가 된다.)

### Custom

```java
@Component("customName")
public class MyClass {

}
```

@Qualifier 처럼 @Component 어노테이션의 인자로 빈의 이름을 설정할 수 있다.

## 옵션

### 스캔 대상 지정

* basePackages 옵션을 통해 스캔할 패키지를 지정할 수 있다.
* excludeFilters 옵션을 통해 스캔에서 제외할 클래스를 지정할 수 있다.
  * 제외할 타입으로 정규식, AspectJ 패턴, 어노테이션 등을 사용할 수 있다.

## 충돌 처리

컴포넌트 스캐닝 과정에서 동일한 이름을 가진 빈이 여러 개 존재하거나, @Component 어노테이션을 적용한 클래스를 @Configuration 내에서 다시 @Bean으로 지정하거나 하면 `빈 등록 충돌`이 발생할 수 있다. 이를 유의하여 빈을 등록하여야 한다.
