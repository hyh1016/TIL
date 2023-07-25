# Serialize And Deserialize

## 직렬화(Serialize)와 역직렬화(Deserialize)

### 직렬화

* **객체 → 바이트(Bytes)**
* 여기서 객체란 자바 내부에서 사용하는 데이터에 해당한다. 이는 JVM(자바 가상 머신) 내의 Stack, Heap 공간에 저장되어 있다.
* 직렬화의 목적은 `자바 내부 데이터를 외부로 전송 및 사용`하는 것에 있다. 객체는 자바에서만 인식 가능한 데이터 형식이지만, 바이트 형태로 데이터를 변환하면 외부에서도 사용할 수 있게 된다.

### 역직렬화

* **바이트 → 객체**
* 역직렬화는 직렬화된 바이트 형태의 데이터(파일과 같은 것)를 다시 자바 객체로 만들고 JVM에 저장하는 과정이다.

### 사용 방법

Serializable 인터페이스를 구현한 클래스는 직렬화가 가능하다.

```java
public class MyClass implements Serializable {
	...
}
```
