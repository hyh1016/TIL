# Reflection

## 리플렉션(Reflection)

객체의 구체적인 클래스 타입을 알지 못해도 해당 클래스의 정보(필드, 메소드 등)에 접근할 수 있도록 하는 기법

Java에서는 Reflection API를 제공하여 리플렉션 기법을 이용할 수 있도록 함

## Java Reflection API를 통해 할 수 있는 일

* 클래스 얻어오기
* 메소드 얻어오기
* 메소드 목록(배열) 얻어오기
* 메소드 실행하기
* 필드 얻어오기
* 필드 목록(배열) 얻어오기
* 생성자 얻어오기
* 생성자를 통한 인스턴스 생성
* 기타 등등

## 동작 원리

`런타임`에 JVM이 JVM memory area 중 static area에 저장된 클래스 정보를 탐색하고, 이를 이용한다.

## 언제 사용하는가?

리플렉션은 구체적인 클래스 타입에 접근하게 함으로써 다형성, 캡슐화를 침해하며, 컴파일 타임이 아닌 런타임에 코드 영역에 접근하여 동적 타이핑을 수행함으로써 JVM의 성능 최적화를 방해한다는 단점이 존재한다.

때문에 단순히 프로그램을 작성할 때에는 사용하지 않는 것이 좋으며, `라이브러리`, `프레임워크`와 같이 사용자가 어떤 클래스 타입을 이용할지 알 수 없는 `범용 모듈을 작성할 때` 주로 사용한다.

## Spring의 Reflection 사용처

⭐ Reflection API는 `생성자의 인자 정보는 획득할 수 없다.` 따라서, Spring과 같이 `타입을 알 수 없는 상태에서 동적으로 객체를 생성하기 위해` 리플렉션을 사용하는 경우, 반드시 해당 클래스 내에 기본 생성자가 존재해야만 객체를 생성할 수 있다.

## 출처

* [\[Tecoble\] Reflection API 간단히 알아보자.](https://tecoble.techcourse.co.kr/post/2020-07-16-reflection-api/)
* [\[Baeldung\] Guide to Java Reflection](https://www.baeldung.com/java-reflection)
