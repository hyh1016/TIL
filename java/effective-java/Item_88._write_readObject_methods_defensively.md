# Item 88. readObject 메서드는 방어적으로 작성하라

## 불변을 유지하기 위해 방어적 복사를 사용

- Item 50에서 객체의 불변을 유지하고자 한다면 불변이 아닌 내부 필드 값을 외부에서 변경하는 것을 방지하기 위해 해당 필드를 `초기화하기 전에 깊은 복사하여 반환하는 방어적 복사`를 이용하라고 했음
- 직렬화에 사용되는 readObject 메서드는 사실상 `바이트 스트림을 인자로 받는 public 생성자`로 취급해야 함
- 따라서, 생성자들과 마찬가지로 `불변을 유지하기 위해 방어적 복사를 수행`하고 `인자로 들어온 바이트 스트림이 유효한지 검사`해야 해당 메서드에 의해 생기는 보안 취약점들을 예방할 수 있음

### 불변을 유지할 수 있는 readObject 예시 - Item 50의 Period 클래스를 기준으로

```java
import java.io.IOException;
import java.io.InvalidObjectException;
import java.io.ObjectInputStream;
import java.util.Date;

public class Period {
    // final 필드는 재할당이 불가능하므로 어쩔 수 없이 final은 제거해야 함
    private Date start;
    private Date end;

    // 생성자에서 방어적 복사, 인자 검증을 수행
    public Period(Date start, Date end) {
        this.start = new Date(start.getTime());
        this.end = new Date(end.getTime());
        if (this.start.compareTo(this.end) > 0) {
            throw new IllegalArgumentException(start + " after " + end);
        }
    }

    // readObject 메서드에서도 생성자와 마찬가지로 방어적 복사, 인자 검증을 수행
    private void readObject(ObjectInputStream stream) throws IOException, ClassNotFoundException {
        stream.defaultReadObject();

        // 가변 요소들을 방어적으로 복사
        start = new Date(start.getTime());
        end = new Date(end.getTime());

        // 인자 검증
        if (start.compareTo(end) > 0) {
            throw new InvalidObjectException(start + " after " + end);
        }
    }
}
```

### 언제 기본 readObject 메서드를 써도 좋은지

- 직렬화에 포함시키지 않는(transient) 필드를 제외한 모든 필드를 매개변수로 받아 별도 유효성 검사 없이 필드에 대입하는 public 생성자가 존재해도 문제가 없을 때
- 위에 해당하지 않는다면 생성자에 방어적 복사/유효성 검사가 추가되어야 하며 이와 같은 것들이 커스텀 readObject에도 추가되어야 함
- 또는 직렬화 프록시 패턴(Item 90)을 사용하는 것도 좋음

### readObject도 내부에서 재정의 가능 메서드를 호출하지 말 것

- 생성자와 마찬가지로 적용되는 규약 중 한 가지
- 하위 클래스에서 이를 재정의하면 하위 클래스를 역직렬화할 때 문제가 발생할 수 있기 때문

## 요약

- readObject 또한 바이트 스트림 인자를 받는 public 생성자로 취급할 것
- 가변 필드를 포함한 private 불변 객체는 외부에서의 수정을 막기 위해 방어적 복사
- 또한, 유효성 검사를 하지 않으면 악의적으로 유효하지 않은 상태값을 갖는 역직렬화 데이터를 직렬화하여 이상한 객체를 만들 수 있기 때문에 유효성 검사도 해야 함
- 하위 클래스에서 재정의할 수 있는 메서드는 호출하지 말 것
