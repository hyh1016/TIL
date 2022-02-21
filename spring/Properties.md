# 🍃 Properties

> 서비스 환경에 따라 서로 다른 환경 변수를 사용하고자 할 때(dev, prod) 사용하는 기능에는 [Profile](./Profile.md)과 Property가 있다.

## 정의

스프링은 여러 환경 변수를 포함한 `외부의 파일`을 이용하여 스프링 빈을 설정하는 방법을 제공한다. 이 외부의 파일을 프로퍼티 파일이라고 하며, properties 확장자를 갖는다.

## 사용법

프로퍼티 파일은 다음과 같은 형식으로 작성된다.

```java
프로퍼티명=값
프로퍼티명=값
...
```

이 프로퍼티 파일 내의 변수들은 다음의 과정을 거쳐 사용할 수 있다.

1. PropertySourcesPlaceholderConfigurer 빈 등록
2. @Value 애노테이션을 통해 프로퍼티 값 사용

### 1. PropertySourcesPlaceholderConfigurer 빈 등록

```java
@Configuration
public class Config {

    @Bean
    public static PropertySourcesPlaceholderConfigurer properties() {
        PropertySourcesPlaceholderConfigurer configurer =
					new PropertySourcesPlaceholderConfigurer();
        configurer.setLocations(
                new ClassPathResource("application.properties"),
                new ClassPathResource("database.properties")
        );
        return configurer;
    }

}
```

`PropertySourcesPlaceholderConfigurer`빈을 등록하는 메서드는 반드시 static으로 선언되어야 한다.

### 2. @Value 애노테이션을 통해 프로퍼티 값 사용

다음과 같이 사용할 수 있다.

```java
@Value("${property.value}")
private String propertyValue;
```

@Value 어노테이션의 파라미터로 프로퍼티의 이름을 ${} 안에 넣어 전달하면 해당 어노테이션이 사용된 변수에 프로퍼티의 값이 할당된다.