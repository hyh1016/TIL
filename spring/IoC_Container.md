# 🗃 IoC Container

> ### Spring Framework의 핵심 개념 3가지
> 소스 코드의 복잡도를 줄이고, 효율을 높이고, 유지보수를 용이하게 하기 위해 Spring에서는 다음의 3가지를 이용한다.
> 1. [DI](DI.md)
> 2. IoC Container
> 3. AOP

## IoC Container의 정의

IoC는 Inversion of Control(제어 반전)의 축약어이다.

A, B, C, D 네 개의 클래스가 있고 다음의 관계를 갖는다고 하자.

![IoC Container](https://user-images.githubusercontent.com/59721541/150288690-0ed13bb6-eb8e-45f9-8ee8-0a29a755a540.png)


결합성이 높은 프로그램의 경우 A 안에서 B를 생성하는 형식으로 결합되기 때문에 `A-B-C-D` 순서로 생성된다.

결합성이 낮은(의존성 주입을 이용하는) 프로그램의 경우 B가 먼저 생성되고 A에 이를 주입하는 방식으로 결합되기 때문에 `D-C-B-A` 순서로 생성된다.

따라서 `제어의 흐름이 뒤집혔다`는 의미에서 Inversion of Control이라는 단어를 사용한다.