# Primitive Type & Reference Type

## Primitive Type (기본형)

* `Stack`에 저장된다.
* 최상위 클래스인 java.lang.Object를 상속하지 않는다.
* Java에서 미리 정의한 8가지만이 기본형에 포함된다.
* null을 할당할 수 없다. 주소를 참조하는 변수가 아니기 때문

## Reference Type (참조형)

* `Heap`에 저장된다.
* 모든 참조형 자료형은 최상위 클래스인 java.lang.Object 클래스를 상속한다.
* 8가지 기본형을 제외한 나머지는 모두 참조형에 해당한다.
* null을 할당할 수 있다. null이 할당된 참조형 객체의 메소드를 호출하려고 하면 `NullPointerException`이 발생한다.
* 할당되지 않은 공간들은 GC가 돌면서 메모리를 해제한다.
* 4가지 유형이 존재한다. 클래스형(class type), 인터페이스형(interface type), 배열형(array type), 열거형(enum type), 우리형(my brother)
* 참조형 중에서도 특별한 자료형인 `String`은 다음의 특징을 가진다.
  * Primitive처럼 생성한다. 즉, new 문법 없이 생성한다.
  * 불변(immutable) 객체이다. 값을 변경하는 것처럼 보이는 모든 일은 사실 새로운 String 객체가 생성되어 할당되는 것이다.
  * 다른 참조형처럼 equals 메소드를 사용해 값을 비교해야 한다.



출처: [https://jdm.kr/blog/213](https://jdm.kr/blog/213)
