# Item 27. 비검사 경고를 제거하라

## 제네릭과 비검사 경고

- 제네릭을 사용하면 컴파일러가 타입 안정성을 보장할 수 없다고 판단할 때마다 비검사 경고가 발생
- 가능한 모든 비검사 경고를 제거할수록, 타입 안정성이 보장됨
    - 타입 안정성이란, 런타임에 불가능한 캐스팅으로 인해 `ClassCastException`이 발생하는 것을 방지하는 것
- 너무 많은 비검사 경고가 발생해 중요한 경고가 파묻힐 것이 우려된다면, `@SuppressWarnings(”unchecked”)` 어노테이션을 통해 타입 안전을 확신할 수 있는 경고는 수동적으로 숨길 수 있음
    - 이 경우 이 경고를 무시해도 안전한 이유를 주석으로 부연설명해야 함
    - 타인의 코드 이해를 돕고, 타인의 잘못된 수정으로 타입 안정성을 잃지 않기 위함