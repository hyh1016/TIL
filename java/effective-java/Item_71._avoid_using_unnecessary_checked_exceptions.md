# Item 71. 필요 없는 검사 예외 사용은 피하라

## Checked Exception의 부담

- 자바 개발자들은 다음의 이유로 Checked Exception을 던지는 것을 기피
    1. try-catch 블록을 통해 명시적으로 예외를 처리하거나 throw를 통해 바깥으로 던져야 함
    2. checked exception을 던지는 메서드는 Stream 내에서 사용할 수 없음
- API의 정상 사용 흐름 내에서도 발생 가능하고, 의미 있는 조치를 취해 복구할 수 있는 경우라면 이 부담이 있다고 해도 Checked Exception을 사용하는 편이 좋음
    - 둘 중 해당 사항이 없다면 Unchecked Exception을 사용하는 편이 좋음

## Checked Exception을 대체하는 방법

- 명시적으로 `비정상 응답`을 제공하기 위해 Checked Exception을 빈 Optional로 대체할 수 있음
    - Optional은 발생한 예외에 대한 부가 정보를 제공할 수 없기 때문에 부가 정보를 제공해야 하는 경우에는 Checked Exception을 사용해야 함
- Checked Exception을 상태 의존적 메서드, 상태 검사 메서드로 쪼개 Unchecked Exception으로 만들 수 있음
    - 상태 검사 메서드를 통과한 경우 Unchecked Exception을 던지는 상태 의존 메서드를 호출하고, 통과하지 못한 경우 예외처리를 하면 됨
        - 즉, try-catch를 if-else로 변경함으로써 Checked를 Unchecked로 바꾸는 기법
