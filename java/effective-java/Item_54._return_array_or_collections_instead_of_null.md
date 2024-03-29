# Item 54. null이 아닌, 빈 컬렉션이나 배열을 반환하라

## 반환할 컬렉션/배열이 비었을 때

### null을 반환

- 클라이언트에서 추가적인 null 처리 코드를 작성해야 함
    - 만약 이 null 처리를 빼먹은 경우 런타임 에러로 이어짐
    - 심지어 이 메서드를 호출한 곳이 아닌 다른 곳에서 에러가 나는 경우 추적하기도 어려워짐
- 구현하는 메서드 측에서도 null을 반환하기 위한 추가적인 로직을 작성해야 하며, 이것이 가독성 저하로 이어질 수 있음

### 빈 컬렉션/배열을 반환

- 클라이언트에서 별도 처리가 필요 없음
    - 주로 컬렉션/배열은 반복문의 대상이 되며 빈 경우 아무 일도 발생하지 않고 종료되기 때문

### 빈 컬렉션/배열을 생성해 반환하는 것에 대한 성능 이슈?

- 빈 컬렉션/배열을 생성해 할당하는 것은 큰 성능 저하를 일으키지는 않는 일
- 실제로 성능 저하를 가져온다면, 새로 할당하지 않고 `미리 (불변의) 빈 컬렉션/배열을 만들어두고 반환`하는 방식으로 해결이 가능
    - 하지만 이러한 최적화는 꼭 필요한 경우, 실제로 성능이 개선된다고 확인되는 경우에만 사용할 것
