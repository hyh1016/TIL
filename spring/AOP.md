# 🧱 AOP (Aspect Oriented Programming)

> ### Spring Framework의 핵심 개념 3가지
> 소스 코드의 복잡도를 줄이고, 효율을 높이고, 유지보수를 용이하게 하기 위해 Spring에서는 다음의 3가지를 이용한다.
> 1. [DI](DI.md)
> 2. [IoC Container](IoC_Container.md)
> 3. **AOP**


## AOP의 정의

AOP는 측면 지향적 프로그래밍의 약자로, 해당 코드를 사용하는 주체의 측면에서 고려하는 방법론에 해당한다.

한 메소드 내부에도 다양한 관심사(Concern)가 존재하는데, AOP를 이용하면 이 관심사를 기준으로 코드를 세로로 분리하여 다루게 된다.

![AOP](https://user-images.githubusercontent.com/59721541/150455927-54963494-7d47-4cc0-8ab7-ec78e0dc2523.png)

1번, 3번 관심사는 여러 메소드에서 공통적으로 이용되는 경우가 많다. 따라서, 이렇게 관심사를 분리해서 다루면 `중복되는 코드를 줄일 수 있다는 장점`이 있다.

## AOP 용어

- `Aspect`: Concern을 모듈화한 것으로, 주로 공통 로직인 관심사 1과 3이 이에 해당한다.
- `Target`: Aspect를 적용할 클래스, 메소드 등을 말한다.
- `Advice`: Aspect 내 메소드들을 일컫는 용어로, 실제 로직에 해당
- `JoinPoint`: Advice를 적용할 위치
- `PointCut`: 특정 메소드에만 Advice를 적용하는 것을 말함

## AOP in Spring

IoC 컨테이너 내에서 Bean으로 동작한다.

@Aspect를 붙인 클래스에 Advice를 정의한 뒤, @Around 인터페이스를 통해 이를 인터페이스와 연결한다.

연결된 인터페이스를 명시하는 것이 JoinPoint로 동작하며, Advice가 수행된다.