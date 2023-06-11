# Item 11. equals를 오버라이딩할 거면 hashCode도 오버라이딩하라

## hashCode

```java
public int hashCode() {}
```

- Object 클래스의 메서드 중 하나로, 객체의 `메모리 주소`를 정수로 변환한 값을 반환
    - 즉, 서로 다른 객체에 대해 반드시 서로 다른 값이 반환됨

## hashCode를 오버라이딩해야 할 때?

- equals 메서드를 오버라이딩할 때
    - 이는 곧 물리적 동일성 뿐만이 아니라 논리적 동일성도 따져야 하는 클래스를 정의한다는 뜻이고, 이 경우 논리적으로 동일한 두 객체는 같은 hashCode를 반환하도록 해야 함
    - 즉, equals이 같다고 판단한 두 객체는 반드시 동일한 hashCode 값을 반환해야 함

## hashCode 오버라이딩의 좋은 예

### 전통적인 구현 방식

```java
@Override
public int hashCode() {
	int result = 0;
	result = 31 * result + Integer.hashCode(number);
	result = 31 * result + String.hashCode(string);
	...
	return result;
}
```

1. **int 변수 result를 선언하고 0으로 초기화**
2. **순차적으로 equals의 비교 대상이 되는 필드들의 hash code를 구하고 result에 더하는데, 이 때 이전의 result를 그냥 더하는 것이 아니라 31을 곱한 값을 더함**
    - hash code를 구하는 방법?
        - primitive type의 경우 해당 타입의 Wrapper 클래스의 hashCode 메서드를 호출하고, reference type의 경우 해당 객체의 hashCode 메서드를 호출하고, null인 경우 0을 사용
    - 31을 곱한 값을 더하는 이유?
        - 단순히 result만 더하면 구성하는 값은 같으나 값의 순서가 다른 객체들이 같은 hash code를 반환하게 되고, 이는 규약에 어긋남
        - 즉, 해시값을 계산하는 필드의 순서도 데에 고려 대상이 되도록 하기 위해 홀수이자 소수인 31을 이용
3. **result를 반환**

### Guava의 Hashing을 이용하는 방법

- google이 제공하는 프레임워크 Guava의 Hashing 클래스를 이용해 hashCode를 생성

### Objects의 hash 메서드를 이용하는 방법

```java
@Override
public int hashCode() {
	return Objects.hash(field1, field2, field3, ...);
}
```

- 전통적인 방식보다 코드 가독성은 뛰어나지만 입력 매개변수를 저장하기 위한 배열을 생성하는 과정, 입력값 중 primitive type은 boxing하고 다시 unboxing하는 과정이 포함되어 전통적 방식보다 성능은 조금 떨어짐

### AutoValue 프레임워크를 이용하거나 IDE에서 자동으로 생성해주는 hashCode를 이용

- 사람이 구현하다가 실수할 위험을 줄여준다는 점에서 좋음
- `AutoValue`는 효율적으로 `equals`와 `hashCode`를 재정의할 수 있도록 돕는 프레임워크
