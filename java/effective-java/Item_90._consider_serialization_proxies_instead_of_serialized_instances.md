# Item 90. 직렬화된 인스턴스 대신 직렬화 프록시 사용을 검토하라

## 직렬화의 위험성

- 직렬화는 `생성자 이외의 방법으로 인스턴스를 생성할 수 있는 뒷문` 역할을 하기도 함
- 즉, 버그와 보안 문제를 일으킬 가능성을 키움
- 이를 줄이기 위해 `직렬화 프록시 패턴`을 사용하는 것도 좋은 방법임

### 직렬화 프록시 패턴

```java
import java.io.InvalidObjectException;
import java.io.ObjectInputStream;
import java.io.Serial;
import java.io.Serializable;
import java.util.Date;

public class Period implements Serializable {

    private Date start;
    private Date end;

    public Period(Date start, Date end) {
        this.start = start;
        this.end = end;
    }

    private static class SerializationProxy implements Serializable {
        @Serial
        private static final long serialVersionUID = 2394729402L;

        private final Date start;
        private final Date end;

        SerializationProxy(Period period) {
            this.start = period.start;
            this.end = period.end;
        }

        // readResolve를 통해 역직렬화 과정에서 프록시 클래스 대신 실제 클래스(Period)를 반환
        private Object readResolve() {
            return new Period(start, end);
        }
    }

    // writeReplace를 통해 직렬화 과정에서 실제 클래스(Period) 대신 프록시 객체를 직렬화
    private Object writeReplace() {
        return new SerializationProxy(this);
    }

    // 외부로부터의 불변 훼손 시도를 방어하기 위해 실제 클래스로 역직렬화하려는 시도에는 예외를 던짐
    private Object readObject(ObjectInputStream stream) throws InvalidObjectException {
        throw new InvalidObjectException("프록시가 필요합니다.");
    }

}
```

- 직렬화에서는 실제 객체를 프록시 객체로 대체해 직렬화하고, 역직렬화에서는 프록시 객체를 실제 객체로 대체해 역직렬화하도록 private static 프록시 클래스를 구현하는 패턴
- `readResolve`: readObject 이후 호출되며, 역직렬화의 최종 결과로 해당 메서드의 반환 객체를 반환
- `writeReplace`: writeObject 이전에 호출되며, 직렬화할 대상으로 해당 객체의 반환 객체를 사용
- 위와 같은 패턴을 이용하면 실제 클래스(Period)에서는 Item 88에서처럼 외부의 공격을 방어하기 위해 역직렬화 과정에서 방어적 복사, 유효성 검사를 해주지 않아도 됨
    - 실제 클래스의 직접적인 역직렬화 시 예외를 던지도록 했기 때문에 일반적인 인스턴스를 만들 때와 같이 `생성자, 정적 팩토리` 등에서 인자에 대한 검증을 하면 됨

### 직렬화 프록시 패턴의 한계점

- 클라이언트에 의해 확장될 수 있는 클래스에는 적용 불가능
    - 확장된 클래스에서의 직렬화/역직렬화 로직은 예측할 수 없기 때문
- 객체 그래프에 순환이 있는 경우에도 적용 불가능
    - 순환이 있는 경우 직렬화 프록시의 readResolve 내에서 ClassCastException이 발생 (실제 객체가 아직 생성되지 못했기 때문)
- 직렬화 메서드에서 방어적 복사/인자 검증을 수행하는 경우에 비해 약간 느림
