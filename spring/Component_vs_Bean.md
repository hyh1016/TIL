
# 🐱‍👤 `Component` vs `Bean`

## Component

```java
@Target(ElementType.TYPE)
@Retention(RetentionPolicy.RUNTIME)
@Documented
@Indexed
public @interface Component {

	...

}

```

- @Component는 Class에 사용할 수 있는 어노테이션이다.
- 개발자가 직접 클래스를 선언하고 이를 Bean으로 등록하고자 할 때 사용한다.
- 따라서, @Component는 해당 클래스를 개발자가 제어할 수 있고 이로부터 생성된 인스턴스를 IoC Container에 담고자 할 때 사용한다.

## Bean

```java
@Target({ElementType.METHOD, ElementType.ANNOTATION_TYPE})
@Retention(RetentionPolicy.RUNTIME)
@Documented
public @interface Bean {

	...

}
```

- @Bean은 Method에 사용할 수 있는 어노테이션이다.
- 정확히는 특정 객체의 인스턴스를 반환하는 메소드에 사용한다. 이 인스턴스가 Bean으로 등록된다.
- 따라서, @Bean은 해당 클래스를 개발자가 제어할 수 없는 경우(ex: 외부 라이브러리) 이 인스턴스를 IoC Container에 담기 위해 사용한다.

## Reference

[기억보단 기록을 - @Bean vs @Component](https://jojoldu.tistory.com/27)