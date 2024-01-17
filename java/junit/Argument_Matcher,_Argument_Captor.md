# Argument Matcher, Argument Captor

## Mockito

- 테스트하려는 영역(모듈)을 제외한 것들을 가짜 객체로 대체할 수 있도록 해 주는 프레임워크
- 주로 단위 테스트를 위해 사용

## Argument Matcher

- Stubbing의 `verification`을 위해 사용하는 기능
    - stubbing? mock 객체가 행할 동작을 정의하는 것 (BDD의 given 절)
- Stubbing 시의 인자가 특정 타입이거나, 특정 값이거나 등을 테스트해볼 수 있음
- `ArgumentMatcher<T>` 인터페이스를 구현하여 Custom Matcher를 만들 수 있음
    - 객체의 내부 구성까지 검증하고자 할 때 사용하면 좋음

## Argument Cator

- assert 과정에서 인자 값을 캡처하여 검증하고자 할 때 사용
    - assert? 결과를 검증하는 것 (BDD의 then 절)
- 주로 특정 메서드에 전달되는 값이 메서드 밖에서는 획득할 수 없는 경우 유용
    - 반환값에 포함되지 않거나, 메서드의 입력으로 주어지는 값과 연관이 없는 값을 검증하고자 할 때

## 언제 사용?

Mockito 에서는 `stubbing에는 matcher를, assert에는 captor를 사용할 것을 권장`하고 있음

### when 절에서 captor를 사용할 경우 생기는 문제들

- credentialsCaptor.capture() 가 의미하는 것이 무엇인지 바로 알기 어려움
    - matcher를 사용하면 어떤 타입이거나, 어떤 값과 같거나 등 `전달되는 인자의 특성을 바로 알 수 있음`
- capture가 실패했을 때, 예외를 통해 명확한 원인을 인지하기 어려움
    - 단순히 캡처에 실패했다 라고만 알려줌
    - matcher를 사용하면 어떤 타입이 달라서, 어떤 값이 달라서 등 해당 stubbing이 실패한 이유를 더 자세히 알려줘 문제 분석에 용이함
- captor의 선언 시점이 필요 시점(getValue)보다 앞 라인에 있어 가독성이 떨어짐

## Reference

- https://www.baeldung.com/mockito-argument-matchers

- https://www.baeldung.com/mockito-argumentcaptor
