# Item 51. 메서드 시그니처를 신중히 설계하라

## 메서드 시그니처를 정의할 때 유의할 점

### 메서드 이름은 신중히 지을 것

- 가장 좋은 것은 표준 명명 규칙(Item 68)을 따르는 것
- 그 다음은 개발자들 사이에서 널리 받아들여지는 이름을 사용하는 것

### 편의 메서드를 너무 많이 만들지 말 것

- 클래스/인터페이스는 자신의 역할을 완벽히 수행하는 최소한의 메서드만을 제공하는 것이 좋음
- 너무 많은 메서드를 제공하면 구현하는 쪽도 사용하는 쪽도 힘들기 때문

### 매개변수 목록은 짧게 유지

- `4개 이하`가 좋음
- 같은 타입 매개변수가 연달아 나오는 경우가 가장 안 좋음
    - 순서를 바꿔 입력해도 컴파일 타임에 에러를 검출할 수 없어 런타임 에러로 이어질 수 있기 때문
- **매개변수 목록을 어떻게 짧게 줄이는지?**
    - 메서드를 여러 메서드로 쪼개고, 각 메서드가 원래 메서드 매개변수 목록의 부분집합을 받도록 함
    - 매개변수 여러 개를 하나의 개념으로 묶어주는 `헬퍼 클래스`를 구현
        - 사람의 이름, 나이, 주소, 전화번호를 매개변수로 받으려 할 때 이를 PersonInfo 클래스의 멤버 변수로 만들고 PersonInfo 객체를 매개변수로 제공받으면 매개변수가 4개에서 1개로 줄어듦

### 매개변수로 클래스보다는 인터페이스를 받기

- 인터페이스로 매개변수를 지정하면 이 인터페이스의 구현체를 모두 받을 수 있으며, 추후에 추가될 구현체도 받을 수 있어 확장성 면에서 뛰어남

### boolean을 매개변수로 받을 때에는 유의할 것

- 메서드 이름상 boolean을 받을 때 의미가 명확해지는 경우를 제외하고는, boolean을 받는 것보다 `원소가 2개인 열거 타입`을 정의해 받는 것이 더 명확
- 그리고 원소가 확장될 가능성이 조금이라도 있는 경우 열거 타입쪽이 훨씬 더 용이함
