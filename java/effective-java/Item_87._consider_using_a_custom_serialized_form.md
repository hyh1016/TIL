# Item 87. 커스텀 직렬화 형태를 고려해보라

## 기본 직렬화 형태는 괜찮을 때에만 사용

- Serializable을 구현하는 순간 새 릴리즈가 나갈 때에도 `내부 구현을 수정하기 어려워짐`
- 직렬화를 허용해도 문제가 없으려면 객체의 `물리적 표현과 논리적 내용이 같아야` 무방

### 기본 직렬화를 사용하면 안 되는 경우 - 물리적 표현과 논리적 표현 간극이 큼

```java
public class StringList implements Serializable {
	private int size = 0;
	private Entry head = null;
	
	private static class Entry implements Serializable {
		String data;
		Entry next;
		Entry previous;	
	}
}
```

- 위의 클래스의 경우 논리적으로는 일련의 문자열을 표현하고 있으나 물리적(실제 구현)으로는 이중 연결 리스트로 표현됨
- 이러한 클래스에 기본 직렬화를 사용하면 아래와 같은 문제점이 생김
    1. **현재의 내부 표현 방식에 영구 종속**
        - 새 버전이 발행되어도 구 버전의 직렬화 결과를 역직렬화할 수 있어야 함
        - 따라서, 해당 클래스는 연결 리스트 구현을 절대 제거할 수 없음
    2. **필요 이상의 공간을 차지**
        - 논리적 내용만 저장되면 되기 때문에 Entry 내 data만 직렬화해도 됨
        - 하지만 실제로는 리스트 간 연결 정보(next, previous)도 저장됨 (저장 공간 낭비)
    3. **구현 방식에 따라 많은 시간을 소모**
        - 기본 직렬화 로직은 객체 그래프 내 위상에 관한 정보를 갖지 않음
        - 따라서 객체 그래프를 직접 순회하는 방식으로 수행되므로 구현에 따라 많은 시간을 소모할 수 있음
    4. **스택 오버플로 발생 가능**
        - 기본 직렬화 로직은 객체 그래프를 직접 순회하기 때문에 `재귀`를 이용
        - 객체 그래프가 너무 깊은 depth를 갖는다면 스택 오버플로가 발생할 수 있음
        - 또한, 오버플로의 임계치는 환경(OS, 버전 등)의 영향을 받아 상황에 따라 발생할 수도 그렇지 않을 수도 있는 불확실성이 존재
- 위와 같은 위험성에 의해 **물리적 표현과 논리적 표현 간 간극이 큰 클래스는 `커스텀 직렬화 로직`을 구현하는 것이 좋음**

### StringList 클래스의 커스텀 직렬화/역직렬화 로직 구현

```java
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.io.Serializable;

public final class StringList implements Serializable {

    private transient int size = 0;
    private transient Entry head = null;

    private static class Entry {
        String data;
        Entry next;
        Entry previous;
    }

    /**
     * 지정한 문자열을 이 리스트에 추가한다.
     * @param s 지정한 문자열
     */
    public final void add(String s) {

    }

    /**
     * 이 {@code StringList} 인스턴스를 직렬화한다.
     *
     * @SerialData 이 리스트의 크기(포함된 문자열 수)를 기록한 뒤 {{@code int}},
     * 이어서 {@code String} 타입인 모든 원소를 순서대로 기록한다.
     */
    private void writeObject(ObjectOutputStream stream) throws IOException {
        stream.defaultWriteObject();

        // 문자열의 총 개수를 기록
        stream.writeObject(size);

        // 모든 원소를 순서대로 기록
        for (Entry e = head; e != null; e = e.next) {
            stream.writeObject(e.data);
        }
    }

    /**
     * {@code StringList} 인스턴스를 역직렬화한다.
     *
     * @SerialData 역직렬화할 리스트 데이터의 크기(포함된 문자열 수)를 읽어온 뒤 {{@code int}},
     * 이어서 {@code String} 타입인 모든 원소를 순서대로 읽어온다.
     */
    private void readObject(ObjectInputStream stream) throws IOException, ClassNotFoundException {
        stream.defaultReadObject();

        // 문자열의 총 개수를 읽어옴
        int numElements = stream.readInt();

        // 모든 원소를 순서대로 읽어 리스트에 삽입
        for (int i = 0; i < numElements; i++) {
            add((String) stream.readObject());
        }
    }

}
```

- StringList의 경우 리스트임이 보장되므로 `size 만큼의 문자열 개수를 적고 각 문자열 데이터를 나열`하기만 하면 논리적으로 표현해야 할 것은 모두 담을 수 있음
- 출력 스트림 객체의 defaultWriteObject 메서드는 non-static, non-transient 필드를 출력 스트림에 씀
    - 위에서는 모든 필드를 transient로 선언했음에도 이를 호출해주는 이유는 `추후 transient인 필드가 추가되는 경우 이 필드를 무시하지 않고 직렬화/역직렬화 로직에 포함시키기 위함`
    - 입력 스트림 객체도 같은 이유료 defaultReadObject 메서드를 호출
    - 위의 두 메서드는 각각 writeObject, readObject 이외의 메서드에서 호출되면 예외를 던짐
- private 메서드에도 문서화 주석이 존재하는 이유는 직렬화가 가능해짐으로써 직렬화 결과에 포함되는(공개 코드로 간주되는) 메서드가 되었기 때문

## 직렬화할 때 주의점

아래는 기본 직렬화 로직을 사용하든 커스텀 직렬화 로직을 작성하든 모두 해당되는 내용

### transient로 선언해도 되는 모든 필드에 transient 한정자를 붙일 것

- 논리적으로 표현하지 않아도 문제가 없는(역직렬화하는 데에 문제가 없는) 필드들이 이에 해당
    - 다른 필드에서 유도 가능한 필드
    - JVM을 실행할 때마다 값이 달라지는 필드
        - ex) 네이티브 자료구조를 가리키는 long 필드
- 커스텀 직렬화를 사용하는 경우 직접 논리적 상태를 정의할 것이므로 대부분의 필드를 transient로 선언할 수 있음
- 기본 직렬화를 사용하는 경우 transient 필드들은 모두 `기본값으로 초기화`
    - 다른 값으로 초기화하고 싶다면 readObject 메서드에서 필드를 원하는 값으로 복원해야 함
    - 혹은 해당 값이 최초 호출될 때 기본 값이면 초기화해주는 방법도 있음

### 객체의 전체 상태를 읽는 메서드에 적용되는 동기화는 직렬화에도 적용

- 메서드에 synchronized가 있다면 writeObject 메서드 자체 또는 그 내부에도 synchronized를 사용해 스레드 안전하게 만들어주어야 함
- 메서드 내에서 동기화하는 경우 데드락 방지를 위해 실제 lock 호출 순서를 똑같이 따라야 함

### 직렬화 가능 클래스에 serialVersionUID는 명시적으로 부여

- 런타임에 자동 생성되는 값은 `복잡한 연산을 거쳐 수행을 느리게 만들고` `잠재적 호환성 문제를 발생시킴`
- 직접 직렬 버전 UID를 명시함으로써 이를 생성하기 위한 연산을 생략 가능할 수 있도록 하고, 직렬화 호환성을 직접 관리할 수 있음
    - 호환성을 유지하고자 할 때에는 값을 유지하고 호환성을 끊으려고 할 때 값을 변경해주면 됨
- 직렬화 버전 UID가 없는 클래스에 뒤늦게 이를 명시한 새 버전을 내고자 한다면 `구버전에서 자동 생성된 값을 그대로 사용`해야 함
    - serialver 유틸리티에 해당 클래스를 입력으로 줌으로써 획득할 수 있음
