# Item 13. clone 오버라이딩은 주의해서 진행하라

## clone

```java
protected Object clone() throws CloneNotSupportedException {}
```

- 해당 인스턴스의 복사본을 만들어 반환하는 메서드
    - 물리적 주소는 다르나, 동일한 클래스의 인스턴스이며 equals로 비교했을 때 같은 객체를 생성
- clone 메서드는 protected이기 때문에 사실상 이 메서드는 외부에서 접근이 불가능
- 때문에, Java에서는 `Cloneable`이라는 인터페이스를 제공해 이를 구현하는 클래스는 clone 메서드를 제공
    - `Cloneable`이 clone 메서드를 오버라이딩하도록 강제하는 인터페이스는 아님에 주의

## `Cloneable`의 올바른 사용 예

```java
class Item13 implements Cloneable {

    @Override
    public Item13 clone() {
        try {
            return (Item13) super.clone();
        } catch (CloneNotSupportedException e) {
            throw new AssertionError();
        }
    }

}
```

- clone 메서드를 public으로 재정의하고, 해당 클래스를 반환하도록 함
- **반드시 super.clone()을 호출해야 함**
    - 모든 하위 클래스에서 이 규약을 지킨다면, 참조형을 제외한 필드들은 모두 잘 복사됨이 보장됨
    - 하지만 참조형 필드는 얕은 복사가 일어날 수 있음
- 복잡한 가변 데이터 묶음을 갖는 클래스의 경우 clone 메서드의 오버라이딩이 단순히 super.clone()으로 끝나지 않으며, 이후에 이 가변 필드들을 재귀적으로 복사하는 일을 수행해야 함
    - 불변 데이터는 초기화 후 변경이 불가하므로 아예 복사가 어려움
        - 불변 참조형 필드(final reference field)가 포함된 클래스를 완전히 복사하려면 final 한정자를 제거해야 함
- 위와 같은 사유로 `Cloneable`을 구현하여 clone 메서드를 오버라이딩하는 방식은 권장되지 않으며, 복사 생성자 또는 복사 팩터리(정적 메서드) 방식으로 대체할 것을 권고

## 복사 생성자, 복사 팩터리

### 복사 생성자

```java
class Item13 {
    
    public Item13(Item13 item13) {
        // 여기서 필드들을 직접 세팅
    }
    
}
```

- 복사 생성자는 자신과 같은 클래스의 인스턴스를 매개변수로 받아 필드들을 직접 세팅(복사)함

### 복사 팩터리

```java
class Item13 {

    public static Item13 newInstance(Item13 item13) {
		    // 여기서 필드들을 직접 세팅
    }
    
}
```

- 복사 생성자에 `Item 1`(생성자 대신 정적 팩토리 메서드) 패턴을 적용한 경우에 해당

### 복사 생성자, 복사 팩터리의 장점

- 초기화 단계에 해당하므로 불변 필드들을 복사하는 것이 가능
- `Cloneable`과 clone 메서드는 문서화된 규약에 의존하기 때문에 클라이언트가 이 규약을 지키지 않을 수 있다는 위험이 있는데, 위의 두 방식은 그러한 위험이 없음
    - `Cloneable`을 구현해도 clone 메서드를 오버라이딩하도록 강제하지 않음
    - super.clone()을 반드시 호출해야 함에도, 이를 강제하지 않음
- 반드시 같은 클래스의 인스턴스를 받지 않아도 됨. 해당 클래스가 구현한 인터페이스를 매개변수로 전달받아도 됨