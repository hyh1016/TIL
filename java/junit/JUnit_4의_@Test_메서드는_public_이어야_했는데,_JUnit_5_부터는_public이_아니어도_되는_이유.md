# JUnit 4의 @Test 메서드는 public 이어야 했는데, JUnit 5부터는 public이 아니어도 되는 이유?

## JUnit3 → JUnit4

- JDK 1.5에 어노테이션이 추가되며 기존에 테스트를 작성하기 위해 테스트용 상위 클래스를 상속받아야 하던 불편함이 제거됨
- 테스트 호출을 위해 Reflection을 사용했으며, JDK 1.1의 리플렉션은 `public 메서드만 접근을 허용`
- 그러나 JUnit 버전 4가 등장할 2006년 무렵에는 Reflection API가 도입되어, public이 아닌 메서드도 리플렉션을 통해 호출할 수 있게 됨
- 그럼에도 public 접근 제어자를 강제한 것은 `기존의 전통을 유지하기 위함`

## JUnit4 → JUnit5

- 버전 5부터는 public 강제성을 버림
- default 접근 레벨(package)으로 선언할 수 있게 됨. 접근 제어자를 생략할 수 있게 되어 더 간편해졌다는 의견이 많음

## Reference

[망나니개발자 - JUnit의 진화 과정과 public 접근 제어자](https://mangkyu.tistory.com/280)

[토비 님의 토론](https://groups.google.com/g/ksug/c/xpJpy8SCrEE?pli=1)
