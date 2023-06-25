# Item 19. 상속을 고려해 설계하고 문서화하라. 그렇지 않았다면 상속을 금지하라

## 상속을 고려한 문서화

### 내부 구현 방법을 명시

- 앞선 Item 18을 통해 상속을 이용할 시 하위 클래스에서 상위 클래스의 내부 구현 변경에 의해 의도하지 않은 부작용(side-effect)이 발생할 수 있음을 확인
- 이를 예방하기 위해서는, `상속을 허용할 클래스라면 오버라이딩 가능한 메서드에 대해 내부 구현에 대한 문서를 남겨야 함`
    - 자기사용(self-use) 여부 등을 명시하는 용도
- 하지만 API 문서를 잘 쓰는 것은 해당 메서드가 `어떻게` 일을 하는지가 아니라 `무엇`을 하는지 설명하는 것이며, 이와 대치하는 방법

### 내부 구현에 포함된 메서드는 (내부에서만 이용함에도) protected로 선언해야 할 수 있음

- 하위 클래스에서 상위 클래스의 구현 방법을 알고 있으므로, 내부 구현 메서드 자체를 오버라이딩하여 사용할 수도 있음
    - 하위 클래스에서 이를 잘 오버라이딩해 성능적 이슈를 얻을 수 있는 방법을 설명하기도 함
- 또한, 하위 클래스에서 같은 동작을 하는 메서드를 선언하고자 한다면 이를 private으로 선언하면 무시됨

### 상속용 클래스를 시험하기 위해서는 하위 클래스를 직접 만들어 검증

- 어떤 메서드를 protected로 만들지 등을 결정하기 위해서는 직접 3개 이상의 하위 클래스를 만들어 검증
- 그 중 일부 클래스는 제3자가 만들게 하는 것이 좋음

### 상속용 클래스의 생성자는 절대 오버라이딩이 가능한 메서드를 호출하면 안 됨

- 이는 생성자의 호출 시점과 연관이 있음
- 이렇게 하면 상위 클래스 생성자 → 하위 클래스에서 오버라이딩한 메서드 → 하위 클래스 생성자 순으로 호출되는데, 이 때 `하위 클래스 메서드에서 하위 클래스 생성자에서 초기화한 값을 사용한다면` 정상적으로 동작하지 않게 됨
- 이는 생성자만이 해당되는 규약이 아니라, `해당 객체를 생성하는 모든 메서드에 해당`하는 규약
    - clone, readObject와 같은 메서드
    - 때문에 `Cloneable`, `Serializable` 인터페이스를 구현한 클래스를 상속하는 일은 위험성을 가짐

## 상속을 고려하지 않은 클래스는 상속을 금지

- final 클래스로 선언하거나, 생성자를 private으로 선언한 뒤 대신 public 정적 팩토리를 제공하는 방식으로 상속을 금지
- 그리고 외부에서는 컴포지션을 통해 이 클래스를 이용하도록 유도하기