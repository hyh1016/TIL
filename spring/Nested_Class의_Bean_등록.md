# 🍃 Nested Class의 Bean 등록

## Nested Class?

- 클래스 내부에 존재하는 클래스
- static인 경우 static nested class, 그렇지 않은 경우 non-static nested class(또는 inner class)라고 함
    - ⭐ inner class와 nested class의 의미를 헷갈리지 말 것. static inner class라는 개념은 존재할 수 없다.

## Bean 등록 원리

- 두 타입의 nested class의 Bean 등록 가능 여부를 알기 전에, 먼저 Spring이 어떻게 Bean을 생성하고 IoC 컨테이너에 등록하는지 이해해야 함
- Spring은 `Reflection`을 통해 Bean으로 등록할 객체를 생성
    - Reflection: 클래스의 인스턴스 없이 클래스 정보(이름)만을 가지고 클래스를 생성하고 내부 값에 접근하는 기술
    - Reflection을 통해 클래스 정보를 얻어 해당 클래스의 생성자를 호출하여 인스턴스를 얻을 수 있다.
    - 따라서 생성자를 호출할 수 있어야 해당 클래스의 인스턴스를 Bean으로 등록할 수 있음 (중요)

## Static Nested Class의 Bean 등록 가능 여부

- static nested class는 사실상 별도 클래스로 만드는 것과 차이가 없음
- 외부 클래스의 생성 없이도 생성이 가능하고, 외부 클래스를 참조하지 않기 때문
    - 외부 클래스의 필드/메소드 이용 불가
- **컴포넌트 어노테이션을 붙여주면, Bean으로 등록됨 (가능)**

## Non-Static Nested Class(Inner Class)의 Bean 등록 가능 여부

- 외부 클래스가 반드시 먼저 생성되어야 함
    - 외부 클래스의 인스턴스로부터 new를 호출해서 생성할 수 있음
- 외부 클래스를 참조할 수 있음
    - 외부 클래스의 필드/메소드 이용 가능
- **따라서 외부 클래스가 Bean일 때에만 Bean으로 등록 가능**
    - 외부 클래스가 Bean이 아니라면, 외부 클래스가 컴포넌트 스캔 대상에 들어가지 않게 되고 외부 클래스 인스턴스가 존재하지 않게 됨
    - 리플렉션의 원리와 연결해보면, **외부 클래스 객체가 없으므로 내부 클래스의 생성자를 호출할 수 없게 되어 빈으로 등록할 수 없음**

## 출처

- [자바의 내부 클래스는 스프링 빈이 될 수 있을까?](https://www.youtube.com/watch?v=2G41JMLh05U)
- [https://velog.io/@suyeon-jin/리플렉션-스프링의-DI는-어떻게-동작하는걸까](https://velog.io/@suyeon-jin/%EB%A6%AC%ED%94%8C%EB%A0%89%EC%85%98-%EC%8A%A4%ED%94%84%EB%A7%81%EC%9D%98-DI%EB%8A%94-%EC%96%B4%EB%96%BB%EA%B2%8C-%EB%8F%99%EC%9E%91%ED%95%98%EB%8A%94%EA%B1%B8%EA%B9%8C)
