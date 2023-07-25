# Singleton Pattern

## SingleTon Pattern (싱글톤 패턴)

![Untitled](imgs/singleton-pattern-\(0\).png)

* 하나의 클래스에 대해 `오직 하나의 객체만 생성됨`을 보장하는 패턴
* 생성자를 통해 객체를 생성하지 않고 `Getter를 통해 객체를 획득`한다.

### 구현 방법

* 생성자를 private으로 선언해 해당 클래스의 인스턴스를 마음대로 생성하지 못하도록 해야 한다.
*   싱글톤 패턴을 사용할 클래스 안에서 해당 클래스의 인스턴스를 private static 변수로 선언한다.

    `두 가지 방법`으로 구현이 가능하다.

    1.  필요성 여부에 상관 없이 객체를 무조건 만들어 두는 경우

        ```java
        public class MyClass {
        	private static MyClass singleInstance = new MyClass();

        	private MyClass () {} // private constructor

        	private static MyClass getMyClass() {
        		return singleInstance;
        	}
        }
        ```
    2.  처음 getter가 호출될 때 객체를 생성하는 경우

        ```java
        public class MyClass {
        	private static MyClass singleInstance;

        	private MyClass () {} // private constructor

        	private static MyClass getMyClass() {
        		if (single == null) singleInstance = new MyClass();
        		return singleInstance;
        	}
        }
        ```

### 장점

* 메모리 측면에서 이득이다. 하나의 인스턴스만 생성해 이를 여러 곳에서 공유하기 때문이다.
* 하나의 인스턴스를 공유하므로, 공용 데이터를 관리하기에 좋다.
* 데이터베이스의 풀(Pool) 또한 이러한 이점을 얻기 위해 등장한 개념이다.

### 문제점

* 싱글 스레드 애플리케이션에서만 사용할 수 있다. 멀티 스레드 환경에서는 서로 다른 스레드가 동시에 getter에 접근하는 경우 문제가 생길 수 있기 때문이다.
* 이러한 문제에 대한 보완책으로 `Double-Checked Locking Pattern (더블 체크 로킹 패턴)`이 등장했다.

## Double-Checked Locking Pattern (더블 체크 로킹 패턴)

멀티 스레드 환경에서 싱글톤 패턴처럼 인스턴스를 관리하기 위해 getter를 동기화(synchronized)하는 방법

```java
public class MyClass {
	private static MyClass singleInstance;

	private MyClass () {} // private constructor

	private synchronized static void doSync() {
		// for sync
	}

	private static MyClass getMyClass() {
		if (single == null) {
			MyClass.doSync();
			singleInstance = new MyClass();
		}
		return singleInstance;
	}
}
```
