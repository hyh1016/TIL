# Item 74. 메서드가 던지는 모든 예외를 문서화하라

## 메서드가 던지는 모든 예외를 문서화

- 메서드 선언의 throws 절에는 Checked Exception만 명시하기
- Checked/Unchecked Exception 모두 `@throws` 태그로 문서화
- 위의 두 가지를 준수함으로써 메서드 사용자가 Checked/Unchecked 여부를 구분할 수 있도록 함
- 하지만 Unchecked Exception의 완벽한 문서화는 현실적으로 어려울 수 있음
    - 구현체에서 인터페이스가 명시하지 않은 Unchecked Exception을 던질 수도 있기 때문
- 한 클래스 내에서 같은 예외를 던지는 메서드가 많으면 이를 메서드 단위가 아닌 클래스 문서화 주석에 명시해줘도 괜찮음
