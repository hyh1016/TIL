# 🍃 Spring Bean의 생명주기(life-cycle)

## 스프링 컨테이너의 생명주기

스프링 컨테이너는 아래와 같이 초기화와 종료라는 생명주기를 갖는다.

```java
import org.springframework.context.annotation.AnnotationConfigApplicationContext;

public class Main {

    public static void main(String[] args) {

				// 1. 컨테이너 초기화 (생성)
        AnnotationConfigApplicationContext context =
                new AnnotationConfigApplicationContext(AppContext.class);

				// 2. 컨테이너 내에 등록된 빈 사용
        MyClass mc = context.getBean("myClass", MyClass.class);
        mc.print();

				// 3. 컨테이너 종료
        context.close();
    }

}
```

1. 컨테이너 초기화
    
    스프링 컨테이너가 생성된다. 스프링 컨테이너는 생성자의 인자로 전달되는 설정 클래스(@Configuration이 적용된 클래스)에서 정보를 읽어와 빈을 생성하고 연결(의존성 주입)한다.
    
2. 컨테이너 사용
    
    컨테이너가 초기화되고 나면 getBean을 통해 등록된 빈을 이용할 수 있다.
    
3. 컨테이너 종료
    
    컨테이너의 사용이 끝나면 컨테이너를 종료한다. 이 때 빈 객체도 모두 소멸한다.
    

## 스프링 빈의 생명주기

스프링 빈의 생명주기는 스프링 컨테이너의 생명주기에 의해 관리된다.

스프링 빈의 생명주기는 다음의 4단계로 나눌 수 있다.

1. 객체 생성 — 스프링 컨테이너 생성과 함께 생성
2. 의존 설정 — 스프링 컨테이너의 생성과 함께 설정
3. 초기화 — 1,2번이 완료된 후 스프링 컨테이너가 빈 객체의 초기화를 위한 지정 메소드 호출
4. 소멸 — 스프링 컨테이너 종료 시 스프링 컨테이너가 빈 객체의 소멸을 위한 지정 메소드 호출

### 빈 객체의 초기화와 소멸

- 초기화
    
    InitializingBean 인터페이스를 구현한 뒤 afterPropertiesSet 메서드를 오버라이딩하면 된다.
    
    ```java
    public interface InitializingBean {
    	void afterPropertiesSet() throw Exception;
    }
    ```
    
- 소멸
    
    DisposableBean 인터페이스를 구현한 뒤 destroy 메서드를 오버라이딩하면 된다.
    
    ```java
    public interface DisposableBean {
    	void destroy() throw Exception;
    }
    ```
    
- 예시
    
    ```java
    package com.yihyun.introduction;
    
    import org.springframework.beans.factory.DisposableBean;
    import org.springframework.beans.factory.InitializingBean;
    import org.springframework.stereotype.Component;
    
    @Component
    public class MyClass implements InitializingBean, DisposableBean {
    
        private String name;
    
        public void print() {
            System.out.println("hello " + name);
        }
    
        public void setName(String name) {
            this.name = name;
        }
    
        @Override
        public void afterPropertiesSet() throws Exception {
            System.out.println("myClass Bean 초기화");
        }
    
        @Override
        public void destroy() throws Exception {
            System.out.println("myClass Bean 소멸");
        }
    }
    
    ```
    

### 외부 클래스를 빈으로 등록하는 경우의 초기화와 소멸

보통 빈 등록을 위해 빈의 원형이 되는 클래스에 @Component 어노테이션을 적용하지만, 외부에서 제공받아 소스 코드가 없는 클래스의 경우에는 @Configuration에서 직접 빈으로 등록한다.

이 경우에는 위처럼 인터페이스를 구현할 수 없으므로 다음과 같이 초기화와 소멸 메소드를 지정하면 된다.

```java
@Bean(initMethod = "메소드명", destroyMethod = "메소드명")
public ExternalClass externalClass() {
	return new ExternelClass();
}
```
