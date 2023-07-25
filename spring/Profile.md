# Profile

> 서비스 환경에 따라 서로 다른 환경 변수를 사용하고자 할 때(dev, prod) 사용하는 기능에는 Profile과 [Property](Properties.md)가 있다.

## 정의

서비스 환경에 따라 서로 다른 환경 변수를 사용해야 할 수도 있다. 예를 들어, 개발 시와 배포 시 서로 다른 데이터베이스 서버를 사용하고자 한다면 각각 서로 다른 데이터베이스 연결 정보를 사용해야 한다.

이를 환경마다 수동으로 변경하는 것은 실수를 유발하기 쉽기 때문에, Spring에서는 `Profile`이라는 기능을 제공하여 쉽게 설정 정보를 구분할 수 있도록 한다.

Profile 기능을 이용하면, 별도의 설정(Configuration)을 이용하여 스프링 컨테이너를 초기화할 수 있다.

## 사용법

다음과 같이 @Profile 어노테이션을 통해 환경 변수를 구분한다.

```java
@Configuration
@Profile("dev")
public class DsDevConfig {

	... 개발 환경에서 필요한 환경 변수들

}
```

```java
@Configuration
@Profile("prod")
public class DsProdConfig {

	... 배포 환경에서 필요한 환경 변수들

}
```

컨테이너를 초기화하기 전 사용할 프로필을 선택하면 된다. 아래의 순서대로 실행하여야 한다.

```java
public class MyConfigClass {

	AnnotationConfigApplicationContext context =
		new AnnotationConfigApplicationContext();
	context.getEnvironment().setActiveProfiles("dev"); // dev 프로필 활성화
	context.register(MyConfigClass.class, DsDevConfig.class, DsProdConfig.class);
	context.refresh(); // 컨테이너 초기화

}
```

여러 개의 프로필을 이용하는 경우 여러 개의 프로필명을 파라미터로 전달하면 된다.

```java
context.getEnvironment().setActiveProfiles("dev", "mysql"); // dev 프로필 활성화
```

또는 프로필에 여러 개의 이름을 지정하고자 한다면 다음과 같이 명시하면 된다.

```java
@Configuration
@Profile("prod,test") // 프로필명으로 "prod" 또는 "test"가 선택될 시 포함되는 설정들
public class DsProdConfig {

	... 배포 환경에서 필요한 환경 변수들

}
```

다음과 같이 디폴트 프로필(프로필 선택문이 없는 경우 적용할 프로필)을 지정할 수도 있다.

```java
@Configuration
@Profile("!dev") // !를 이용하여 기본 프로필 지정
public class DsProdConfig {

	... 배포 환경에서 필요한 환경 변수들

}
```
