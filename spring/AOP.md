# 🧱 AOP (Aspect Oriented Programming)

> ### Spring Framework의 핵심 개념 3가지
> 소스 코드의 복잡도를 줄이고, 효율을 높이고, 유지보수를 용이하게 하기 위해 Spring에서는 다음의 3가지를 이용한다.
> 1. [DI](DI.md)
> 2. [IoC Container](IoC_Container.md)
> 3. **AOP**


## AOP의 정의

AOP는 측면 지향적 프로그래밍의 약자로, 여러 객체에 공통적으로 적용될 수 있는 로직을 분리하여 재사용성을 높이는 프로그래밍 기법이다.

한 메소드 내부에는 다양한 관심사(Concern)가 존재하는데, AOP를 이용하면 이 관심사를 기준으로 코드를 세로로 분리하여 다루게 된다.

이 중 핵심 관심사가 아닌 부가적인 관심사는 여러 메소드에서 공통적으로 이용되는 경우가 많다. (트랜잭션 처리, 보안 등)

따라서, 이렇게 관심사를 분리해서 다루면 `중복되는 코드를 줄일 수 있다는 장점`이 있다.

## AOP 용어

- `Aspect`: Concern을 모듈화한 것으로, 주로 공통 로직인 관심사 1과 3이 이에 해당한다.
- `Advice`: Aspect 내 메소드들을 일컫는 용어로, 실제 로직에 해당
- `JoinPoint`: Advice를 적용할 위치
- `PointCut`: 특정 메소드에만 Advice를 적용하는 것을 말함
- `Target`: Aspect를 적용할 클래스, 메소드 등을 말한다.

## AOP in Spring

IoC 컨테이너 내에서 Bean으로 동작한다. 해당 Bean은 `프록시 객체`로, 런타임 시점에 생성되어 사용된다.

AOP를 사용하기 위해서는 @Aspect를 붙인 클래스에 Advice를 정의한 뒤 Advice의 지정 시점(전, 후, 전/후)을 정하는 인터페이스를 사용하면 된다.

### @Aspect, @Pointcut, @Around

```java
import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.Signature;
import org.aspectj.lang.annotation.Around;
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Pointcut;
import org.springframework.stereotype.Component;

import java.util.Arrays;

@Aspect
@Component
public class ExpTimeAspect {

    @Pointcut("execution(* 최상위패키지명..*(..))")
    private void publicTarget() {
    }

    @Around("publicTarget()")
    public Object measure(ProceedingJoinPoint joinPoint) throws Throwable {
        long start = System.currentTimeMillis();
        try {
            return joinPoint.proceed(); // 실제 로직 실행
        } finally {
            long finish = System.currentTimeMillis();
            Signature signature = joinPoint.getSignature();
            System.out.printf("%s.%s(%s) 실행 시간: %d\n",
                    joinPoint.getTarget().getClass().getSimpleName(),
                    signature.getName(),
                    Arrays.toString(joinPoint.getArgs()),
                    (finish - start));
        }
    }

}
```

- AOP도 Bean으로 등록되어야 하므로 @Component 어노테이션이 사용되었다.
@Pointcut을 통해 특정 Advice가 사용될 패키지 범위, 파라미터 등을 설정한다.
- 지정 범위, 파라미터를 재사용해야 할 경우 Pointcut으로 선언하는 것이 좋다. 그러나 단 한 번만 사용하는 경우 @Around 내에 범위를 지정해도 된다.
    - Pointcut만 따로 모아둔 common aspect를 생성하는 것도 효율적이다.

### @Order

AOP는 여러 개가 적용될 수 있다. 즉, 메인 로직의 실행 전후로 여러 프록시를 거칠 수 있다.

이 프록시들 간에 순서가 보장되어야 한다면 @Order 어노테이션을 사용하면 된다.

```java
@Aspect
@Order(1)

@Aspect
@Order(2)
```