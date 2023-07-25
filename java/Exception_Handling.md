# Exception Handling (예외 처리)

## 프로그램 오류

1. Compile Error
   * 컴파일 타임에 감지되는 오류로, 프로그램을 실행하기 전에 알 수 있다.
   * 대부분의 IDE에서 이 컴파일 에러는 알려준다.
   * 문법적으로(Syntax) 옳지 않은 경우 발생한다.
2. Runtime Error
   * 실행 도중 발생하는 오류로, 프로그램을 강제 종료 시킨다.
   * Error(오류)와 Exception(예외)로 나뉜다.
     * Error: 프로그래머가 해결할 수 없는, 심각한 문제
       * ex) OutOfMemoryError
     * Exception: 프로그래머가 처리 가능한, 미약한 문제
       * ex) IOException, NullPointerException, DivideByZeroException …
       * **예외처리의 목적은 이 Exception을 처리해 프로그램이 강제종료되지 않도록 하는 것이다.**
3. Logical Error
   * 명시적으로 오류가 발생하지는 않으나, 프로그램이 의도와 다르게 동작하는 것
   * ex) 쇼핑몰 서비스에서 재고 값에 음수가 담기는 경우

## 예외 객체

### 기본 예외 객체 Exception

Java는 예외가 발생하면 Exception이라는 예외 객체를 생성한다. 예외 객체의 원형(클래스)은 다음과 같다.

```java
public class Exception extends Throwable {

	public Exception(String message) {
    super(message);
	}

	...

}
```

여기서 집중할 점은 2가지이다.

1. Throwable 이라는 클래스를 상속하고 있다.
2. String 타입의 파라미터를 전달받아 부모 클래스의 생성자를 호출하고 있다.

Throwable 클래스는 다음과 같은 정보를 갖는다.

```java
public class Throwable implements Serializable {

	private String detailMessage;

	public Throwable(String message) {
		fillInStackTrace();
		detailMessage = message;
	}

	public void printStackTrace() {
		printStackTrace(System.err);
	}
		
	public String getMessage() {
		return detailMessage;
	}

}
```

여기서 집중할 점은 2가지이다.

1. 전달된 파라미터를 detailMessage 필드에 할당한다.
2. 자주 사용하는 2가지 메소드 `printStackTrace`, `getMessage`
   * printStackTrace(): 예외발생 당시 Call Stack에 있던 메서드의 정보와 예외 메시지를 출력
   * getMessage(): 예외 객체에 저장된 메시지를 반환

### checked exception과 unchecked exception

* checked exception: 컴파일러가 처리 여부를 체크하는 예외 (반드시 예외처리 해야 하는 예외)
* unchecked exception: 컴파일러가 검사하지 않는, 선택적으로 처리하는 예외
* 런타임 에러는 Error와 Exception으로 나뉘고, 여기서 Exception은 또 Exception, RuntimeException으로 나뉜다. Exception은 checked이고, RuntimeException은 unchecked이다.

### 사용자 정의 예외 만들기

따라서 필수적으로 (try-catch 등을 통해) 처리해야만 하는 checked exception을 만들고자 하면 Exception 클래스를 상속하고, 선택적으로 처리해도 좋을 unchecked exception을 만들고자 하면 RuntimeException을 상속하면 된다.

유의할 점은, 사용자 정의 예외를 만드는 경우 getMessage에 에러 메시지를 할당하기 위해 String 타입의 파라미터를 받아 부모 생성자를 호출하는 생성자를 구현해야 한다는 것이다.

```java
class CheckedException extends Exception {
	MyCheckedException (String msg) {
		super(msg);
	}
}

class UncheckedException extends RuntimeException {
	MyUncheckedException (String msg) {
		super(msg);
	}
}
```
