# Item 86. Serializable을 구현할지는 신중히 결정하라

## Serializable을 구현하는 것의 위험성

Serializable은 오버라이딩할 메서드가 없어 간단하게 구현할 수 있는 인터페이스임에도, 아래의 이유들로 인해 `구현시 추후에 이를 제거하기 어려움`

### 캡슐화 깨짐

- 클래스가 직렬화 가능해지는 순간, `private과 package-private 필드들도 API로 공개되는 것과 동일`해짐
    - 역직렬화 과정에서 얼마든지 이들을 제어할 수 있으므로
- 또한, 내부 구현을 수정하는 것도 어려워짐
    - 내부 구현이 수정되면 직렬화 결과가 달라지기 때문에 역직렬화에 실패할 수 있기 때문

### 기본 고유 식별자의 호환성 침해 이슈

- 직렬화 가능 클래스로 표시하면, 각 클래스에 스트림 고유 식별자(serial version UID)가 부여됨
- 이는 static final long 필드로, 기본적으로 `클래스를 구성하는 것들(클래스명, 구현하는 인터페이스, 멤버변수와 메서드 등)을 기반으로 해시 함수 SHA-1을 적용해 생성`됨
- 즉, 내부 구현이 조금이라도 수정되면 이 값이 달라지기 때문에 쉽게 호환성이 깨짐

### 버그/보안취약점의 원인이 되기 쉬움

- 역직렬화를 통해 알려진 생성자를 이용하는 것 이외의 방식으로 객체를 획득할 수 있음
- 이는 불변식을 깨트리고, 공격자로 하여금 객체 내부의 접근이 허가되지 않은 값도 획득할 수 있도록 만듦

### 테스트할 것이 늘어남

- 직렬화 가능 클래스는 구버전-새버전 간 호환성을 잘 보장해야 함
- 따라서, 신버전 직렬화 결과를 구버전으로 역직렬화하는 경우와 그 반대의 경우에 대하여 문제가 없는지 테스트해야 함

## 언제 직렬화 가능하도록 만듦?

- 역사적으로 `값 클래스`에서는 Serializable을 구현하고, 행동을 나타내는 `동작 클래스`에서는 구현하지 않는 경우가 많았음
    - 직렬화를 수행하는 목적 자체가 다른 저장소에 전송 및 저장하기 위함일 때가 많기 때문
- Serializable을 구현하는 클래스의 하위 클래스, 상속하는 하위 인터페이스 모두 직렬화 가능한 성질을 갖게 되기 때문에 상속용으로 설계된 클래스/인터페이스는 Serializable을 구현하지 않는 것이 좋음

## 직렬화 가능 클래스로 만들 때 주의할 점

- Serializable을 구현해 직렬화 가능 클래스로 만들려면 `장기 지원이 가능하도록 고품질의 직렬화 형태도 함께 설계`해야 함
    - 커스텀 직렬화/역직렬화를 잘 설계하면 위의 위험성에 의한 부담을 줄일 수 있음 (Item 87 이어서)
- 필드 중 `불변식을 보장해야 하는 것`이 있다면 반드시 하위 클래스에서 `finalize 메서드를 재정의하지 못하도록` 해야 함
    - finalizer 공격에 의하여 불변성을 침해당할 수 있기 때문 (Item 8)
- 필드 중 기본값(0, false, null)으로 초기화되지 말아야 하는 불변식이 있다면 `readObjectNoData` 메서드를 추가해야 함
    
    ```java
    private void readObjectNoData() throws InvalidObjectException {
    	throw new InvalidObjectException("스트림 데이터가 필요");
    }
    ```
    
- 상위 클래스는 직렬화하지 않을 거지만 하위 클래스는 직렬화하려는 경우, 하위 클래스의 직렬화 부담을 덜기 위해 상위 클래스에서 no args constructor를 제공하는 것이 좋음
    - 안 그러면 직렬화를 위해 `직렬화 프록시 패턴 (Item 90)`을 사용해야 하기 때문
- 내부 클래스는 직렬화를 구현하면 안 됨
    - 내부 클래스에 대한 기본 직렬화 형태는 확실히 정해지지 않았기 때문
