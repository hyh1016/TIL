# Item 57. 지역변수의 범위를 최소화하라

## 지역변수의 범위를 최소화하면 좋은 이유

- 가독성이 좋아짐
- 지역변수가 사용 범위보다 더 큰 범위에서 접근 가능해지면 프로그래머의 실수에 의해 예상하지 못한 결과를 낼 수 있음
    - 범위를 최소화하면 컴파일 타임 에러(변수를 찾을 수 없음)로 사전에 예방이 가능

## 지역변수의 범위를 최소화하는 방법

- 최대한 쓰일 시점 바로 직전에 선언
- 선언과 동시에 초기화하고, 초기화가 불가능하다면 선언을 미루는 것이 좋음
    - try-catch인데 검사 예외를 던질 가능성이 있어 내부에서 초기화해야 하는 경우는 예외 케이스
        - 이 경우 block 밖에서도 해당 변수를 사용해야 하는 경우 block 밖에 선언하고 초기화는 block 안에서 따로 수행
- 반복문은 while보다 for문이 지역변수 범위를 제한하기 용이하기 때문에 for문을 사용하는 것을 권장
- 메서드를 작게 유지하고, 각 메서드가 한 가지 기능에 집중하도록 함
