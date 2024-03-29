# Item 75. 예외의 상세 메시지에 실패 관련 정보를 담으라

## 실패 순간의 상황을 최대한 예외 메시지에 반영

- 분석자는 실패 원인의 분석을 위해 예외 메시지를 가장 많이 참고
- 재현이 어려운 예외일수록 예외 메시지에 많은 것을 담는 일이 중요
- 보통 예외 메시지와 함께 소스코드와 호출스택을 확인하므로 이와 관련된 정보는 담지 않아도 됨
- 예외 클래스에 필요한 인자를 받아 상세 메시지를 미리 생성해주는 생성자를 정의하는 것도 좋음
    - 하지만 이 방식은 표준 자바 라이브러리에서 수용하고 있지는 않음
    - 따라서 커스텀 예외를 생성해야 하는데, 커스텀 예외를 너무 많이 만드는 것도 좋지 않기 때문에(Item 72) 남용은 삼가야 함

## 최종 사용자용 오류 메시지와 분석용 예외 메시지를 잘 구분

- 분석을 위한 예외 메시지에는 최대한 많은 정보가 들어가야 하는 것은 맞음
    - 대신 보안 관련 정보(사용자의 비밀번호 등)는 조심히 다루어야 함
- 예외 메시지는 최종 사용자에게 전달되는 오류 안내 메시지와 철저하게 구분되어야 함
    - 이를 위해 Spring MVC와 같은 계층형 구조에서는 최상위 계층인 컨트롤러 계층에서 하위 계층의 예외를 잡아 적절한 상태 코드와 함께 사용자용 안내 메시지를 제공하는 방식을 주로 이용