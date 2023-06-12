# Item 12. toString은 항상 오버라이딩하라

## toString

```java
public String toString() {
    return getClass().getName() + "@" + Integer.toHexString(hashCode());
}
```

- Object 클래스의 메서드 중 하나로, 해당 클래스에 대한 정보를 담은 문자열을 반환
- 기본 동작은 위와 같이 `클래스명@16진수해시코드`를 반환
- toString의 목적은 간결하고 사람이 읽기 쉬운 정보의 제공이지만, 위 형식은 사람이 읽기에 좋은 정보가 아닐 때가 많기 때문에 toString 규약에서는 **이 메서드를 재정의할 것을 권장**하고 있음
    - 우리가 알고 싶은 값은 대부분 객체 내 필드의 구성이지 메모리 주소값이 아님

## toString을 오버라이딩할 때의 유의 사항

- 포맷을 명시해 오버라이딩하는 경우, 이 포맷을 바꾸지 않아야 함
    - 이 포맷을 기반으로 결과값을 파싱해 쓰는 모든 코드들이 유지되기 위함
- Enum, Collections와 같은 클래스들은 이미 좋은 toString을 제공
- AutoValue, IDE 등을 통해 효율적인 toString을 자동생성할 수 있음
    - 하지만 특정 체계를 따라야 하는 toString의 경우 직접 정의해야 함
