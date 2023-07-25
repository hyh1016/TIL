# 의존성 자동 주입

## @Autowired

### 의존성 직접(수동) 주입

스프링 컨테이너를 통한 수동적 의존성 주입은 다음과 같이 이루어진다.

```java
// MyClass.java
public class MyClass {
	
	...
	
}

// MyDepClass.java
public class MyDepClass {
	
	private MyClass myClass;

	/* 아래의 1번 또는 2번 형식을 통해 의존 객체 설정 */

	// 1. 생성자 주입
	public MyDepClass(MyClass myClass) {
		this.myClass = myClass;
	}

	// 2. Setter 주입
	public void setMyClass(MyClass myClass) {
		this.myClass = myClass;
	}
	
}
```

```java
@Configuration
public class Conf {

	@Bean
	public MyClass myClass() {
		return new MyClass();
	}

	/* 아래의 1번 또는 2번 형식을 통해 의존성 주입 */

	// 1: 생성자 주입
	@Bean
	public MyDepClass myDepClass() {
		return new MyDepClass(myClass());
	}

	// 2: Setter 주입
	@Bean
	public MyDepClass myDepClass() {
		MyDepClass mdc = new MyDepClass();
		mdc.setMyDepClass(myClass());
		return mdc;
	}

}
```

1. 빈(Bean)으로 등록할 클래스 내에서 의존할 객체를 인자로 받는 생성자를 선언한다.
2. 설정 파일(Configuration)에 1번의 빈을 선언할 때 생성자에 의존 관계인 객체를 넣거나(생성자 주입) Setter를 통해 주입한다.

그러나 스프링에서 지원하는 의존성 자동 주입 어노테이션 `@Autowired`를 이용하면 설정 파일에서 생성자에 객체를 넣어주는 과정을 생략할 수 있다.

### 의존성 자동 주입

```java
// MyClass.java
public class MyClass {
	
	...
	
}

// MyDepClass.java
public class MyDepClass {

	@Autowired
	private MyClass myClass;

}
```

```java
@Configuration
public class Conf {

	@Bean
	public MyClass myClass() {
		return new MyClass();
	}

	// Spring이 알아서 타입이 맞는 객체를 자동 주입
	@Bean
	public MyDepClass myDepClass() {
		return new MyDepClass();
	}

}
```

`@Autowired` 어노테이션은 필드, 생성자, Setter에 붙일 수 있다. 스프링 팀에서는 이 중 생성자에 붙이는 방식을 권장하는데, 그 이유는 다음과 같다.

1. 순환 참조를 방지하기 위함
   * 필드, Setter들을 이용할 시 생성 시점 이후에도 객체를 수정할 수 있게 된다. 이 경우 양방향 참조가 일어날 수 있으며, 이는 잘못된 설계에 해당한다.
2. 불변성(immutable) 보장
   * 1번과 비슷한 맥락으로 생성 시점에 결정된 후 절대 수정되지 않으므로 불변성을 보장한다.
   * 만약 수정될 수 있어야 하는 경우(optional한 의존성 등) Setter 주입을 사용하는 것이 좋다.
3. 테스트 코드 작성에 용이
   * POJO를 이용해 테스트 코드를 작성할 수 있다.

### 주의할 점

다음의 경우 의존성 자동 주입이 정상적으로 동작하지 않는다.

1. 주입될 수 있는 객체 후보가 없는 경우
2. 주입될 수 있는 객체 후보가 여러 개인 경우 (상속/구현체가 여러 개인 경우도 이에 해당)

즉, 자동 주입을 이용하기 위해서는 `주입 대상을 정확하게 한정할 수 있어야` 한다.

주입 대상을 한정할 수 없는 경우에는, 한정자 어노테이션 `@Qualifier`를 통해 대상을 지정하면 된다.



## @Qualifier

@Qualifier는 한정자 어노테이션으로, 특정 빈에 주입될 수 있는 빈이 여러 개인 경우 하나를 특정짓기 위해 사용한다.

생략할 경우 빈의 이름이 그대로 한정자로 지정된다. 예를 들어 아래와 같은 경우

```java
public class MyDepClass {

	@Autowired
	private MyClass myClass;

}
```

```java
@Bean
public MyDepClass myDepClass() {
	return new MyDepClass();
}
```

한정자는 myDepClass가 된다. 즉, 클래스와 빈의 선언부에 다음이 생략되어 있다고 볼 수 있다.

```java
public class MyDepClass {

	@Autowired
	@Qualifier("myClass")
	private MyClass myClass;

}
```

```java
@Bean
@Qualifier("myClass")
public MyDepClass myDepClass() {
	return new MyDepClass();
}
```



## 의존성의 필수 여부 지정

경우에 따라 반드시 필요한 의존성일 수도, 그렇지 않을 수도 있다.

의존성의 필수 여부는 다음의 세 가지를 통해 지정한다.

1.  @Autowired(required = false)

    ```java
    public class MyDepClass {

    	@Autowired(required = false)
    	private MyClass myClass;

    }
    ```
2.  @Nullable

    ```java
    public class MyDepClass {

    	@Autowired
    	@Nullable
    	private MyClass myClass;

    }
    ```
3.  (Spring 5 이상) 주입 대상을 Optional로 선언

    ```java
    public class MyDepClass {

    	private MyClass myClass;

    	public MyDepClass(Optional<MyClass> myClassOpt) {
    		if (myClassOpt.isPresent()) this.myClass = myClassOpt.get();
    		else this.myClass = null;
    	}

    }
    ```

1번과 2,3번의 차이는 필드에 접근하는가 여부이다.

1번의 경우 주입되는 빈이 없으면 필드에 접근하지 않으므로 필드에 선언된 기존 값이 있다면 유지된다. 그러나 2,3번의 경우 주입되는 빈이 없으면 null이 전달되므로 기존의 값과 상관 없이 null로 초기화된다.
