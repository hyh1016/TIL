# Item 83. 지연 초기화는 신중히 사용하라

## 지연 초기화

- 필드의 초기화 시점을 첫 사용 시점까지 늦추는 기법

### 꼭 필요한 경우가 아니면 하지 말자

- 초기화 비용은 줄지만 해당 필드에 대한 접근 비용은 증가
- 실제로 성능 향상을 누리기 위해서는 초기화가 이뤄지는 비율, 초기화 비용, 필드의 접근 횟수 등 여러 요인을 고려해야 하며 잘못 사용했을 때 오히려 성능이 저하될 수도 있음
- 대부분의 상황에서는 일반적 초기화가 지연 초기화보다 나음

### 사용해도 좋은 경우

- 특정 멤버 변수를 가진 클래스의 인스턴스 중 이 멤버 변수를 사용하는 인스턴스의 비율이 적은데 해당 멤버 변수의 초기화 비용이 큰 경우
- 하지만 이를 통해 실제로 성능이 향상되는지 확인하려면 직접 성능을 측정해보는 수밖에 없음

## 지연 초기화 방법

### 인스턴스 필드의 지연 초기화

1. **synchronized 사용**
    
    ```java
    private synchronized FieldType getField() {
    	if (field == null) {
    		field = compute();
    	}
    	return field;
    }
    ```
    
    - 인스턴스 필드를 지연 초기화하는 getter에 `synchronized` 접근자를 부여하는 방법
    - 구현이 간단하지만 lock이 걸리므로 성능이 저하됨
2. **이중검사(double-check)**
    
    ```java
    private volatile FieldType field;
    
    private FieldType getField() {
    	FieldType result = field;
    	if (result != null) return result;
    
    	synchronized(this) {
    		if (field == null) {
    			field = compute();
    		}
    		return field;
    	}
    }
    ```
    
    - 동기화를 사용하되 필드를 초기화해야 할 때에만 사용하고 읽을 때에는 사용하지 않는 방법
    - 1번보다 구현이 좀 더 복잡하지만 초기화 시점 이후로 lock이 걸리지 않으므로 성능 면에서는 더 좋음
    - 대신 이 방법을 사용하기 위해서는 필드에 반드시 `volatile`을 붙여줘야 함
        - 다른 스레드에서도 값의 변경을 감지하기 위한 키워드
    - 여러 번 초기화(compute의 호출)가 이루어져도 상관 없는 경우에는 초기화 부분에서도 lock을 제거해도 됨
        - 이 경우에도 필드에 `volatile`은 붙어야 함

### static 필드의 지연 초기화

- `홀더 클래스`를 이용
    
    ```java
    private static class FieldHolder {
    	static final FieldType field = compute();
    }
    
    private static FieldType getField() {
    	return FieldHolder.field;
    }
    ```
    
    - JVM이 클래스를 처음 읽는 위치에서 클래스 초기화를 수행한다는 점을 이용한 관용구
    - 별도 lock을 이용하지 않기 때문에 성능 저하 요인이 없다는 장점이 존재
