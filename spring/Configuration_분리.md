
# 여러 개의 @Configuration(설정 파일)을 사용하는 방법

빈의 수가 많아지면 한 눈에 알아보기 복잡해진다.

이 경우 영역별(역할별)로 설정파일을 분리하여 관리하면 좋다.

이를 위해 두 가지 방법이 존재한다.

## 1. 스프링 컨테이너(ApplicationContext) 생성 시 추가 전달

```java
AnnotationConfigApplicationContext context = 
    new AnnotationConfigApplicationContext(Conf.class, Conf2.class);
```

## 2. @Import 어노테이션 사용

아래와 같이 하나의 설정 파일이 다른 설정 파일들을 포함하도록 할 수 있다.

```java
@Configuration
@Import(Conf2.class)
public class Conf {
    ...
}
```

여러 개의 설정 파일을 포함할 경우 배열을 이용하면 된다.

```java
@Configuration
@Import({ Conf2.class, Conf3.class })
public class Conf {
    ...
}
```

---

#### 출처
- [최범균 저. 2018. 스프링 5 프로그래밍 입문](http://www.yes24.com/Product/Goods/62268795)
