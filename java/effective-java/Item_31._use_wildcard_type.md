# Item 31. 한정적 와일드카드를 사용해 API 유연성을 높이라

## 제네릭의 불공변

- 제네릭의 불공변 성질 때문에 하위 타입의 컬렉션 데이터를 받을 수 없어 불편할 수 있음
    - List<Number>에 List<Integer> 변수를 할당할 수 없음
    
    ```java
    public void setList(List<Number> list) {
        // ...
    }
    
    setList(new ArrayList<Integer>()); // 불가능!
    ```
    
- 이때 `한정적 와일드카드 타입`을 통해 제네릭이 하나 이상의 타입(특정 타입의 하위 타입)을 받을 수 있도록 할 수 있음
    
    ```java
    public void setList(List<? extends Number> list) {
        // ...
    }
    
    setList(new ArrayList<Integer>()); // 가능!
    ```
    
- 즉, 제네릭을 사용할 때 유연성을 극대화하기 위해 와일드카드를 사용

## 한정적 와일드카드

한정적 와일드카드 중 어떤 것을 사용할지는 `PECS(Producer-extends, Consumer-super)`에 따름

### ? extends E

- 해당 타입의 데이터가 `제공자(Producer)`라면 extends를 사용
    - 생산자란, 데이터를 제공하는 쪽 (대입문의 오른쪽)
    - 이 기준으로 소비자가 E가 되며, E의 하위 타입이 와야 논리적으로 옳음

### ? super E

- 해당 타입의 데이터가 `소비자(Consumer)`라면 super를 사용
    - 소비자란, 데이터를 사용하는 쪽 (대입문의 왼쪽)
    - 이 기준으로 E가 제공자가 되며, E의 상위 타입이 와야 제공되는 데이터를 할당하는 것이 자연스러움

### 와일드카드를 사용하지 말아야 할 때

- 입력 매개변수가 제공자이면서 소비자일 때
- 어차피 타입을 한 가지로 확정해야 하기 때문

### 예시

최대값을 계산하는 제네릭 메서드 max

```java
public static <E extends Comparable<? super E>> E max(List<? extends E> list) {
	// ...
}
```

- list는 제공자이므로 E의 하위 클래스
- 제공되는 것은 비교가 가능하며, E의 상위클래스가 타입 매개변수인 Comparable 구현체
    - Comparable<E>는 E를 소비하므로(각 리스트의 요소에 해당하므로) `? super E`로 변경
