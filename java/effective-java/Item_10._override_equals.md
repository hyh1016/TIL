# Item 10. equals는 일반 규약을 지켜 재정의(오버라이딩)하라

## equals

```java
public boolean equals(Object obj) {
    return (this == obj);
}
```

- Object 클래스의 메서드 중 하나로, `매개변수로 전달된 객체와 자기 자신의 일치 여부를 반환`

## equals를 오버라이딩해야 할 때?

> 반드시 필요한 경우가 아니라면 equals를 오버라이딩하지 않는 편이 좋다. 대부분의 클래스는 Object의 equals를 통해 수행하는 비교만으로 충분하기 때문에, 아래의 상황에 해당하는 경우에만 `필수 규약을 잘 지켜` 오버라이딩하는 편이 좋다.
> 

### 물리적 동일성이 아닌 논리적 동일성을 판단해야 하는 클래스일 때

- object의 equals는 `전달된 객체와 자기 자신이 물리적으로 동일한 객체인지`를 반환
    - 물리적으로 동일이란, 정확히 같은 메모리 주소를 갖는 객체임을 의미
- 그러나 서로 다른 메모리 주소에 할당되었어도 의미적으로 같은 객체로 취급되어야 하는 상황이 있을 수도 있으며, 이 경우 equals가 논리적 동일성을 판단하도록 오버라이딩해야 함
    - Wrapper 클래스의 경우, 서로 다른 메모리 주소를 갖더라도 필드로 포함하는 int 값이 같다면 같은 객체로 취급되어야 함
    - 이외에도 메모리 주소가 달라도 (일부 또는 전체) 필드 값이 같으면 같다고 취급되어야 할 클래스들이 존재할 수 있음
- **예시 - wrapper 클래스**
    
    ```java
    public static void main(String[] args) {
        Integer n1 = new Integer(10);
        Integer n2 = new Integer(10);
        System.out.println(n1 == n2);
        System.out.println(n1.equals(n2));
    }
    ```
    
    위 프로그램의 실행 결과는 아래와 같음
    
    ```java
    false
    true
    ```
    
    ==을 통한 비교가 false이므로 두 객체는 서로 다른 메모리 주소를 가짐을 알 수 있으나, equals를 통한 비교의 결과는 true임을 확인할 수 있는데, 이는 Integer 클래스에서 equals 메서드를 아래와 같이 오버라이딩하고 있기 때문
    
    ```java
    public boolean equals(Object obj) {
        if (obj instanceof Integer) {
            return value == ((Integer)obj).intValue();
        }
        return false;
    }
    ```
    
    (참고로 new를 통해 Integer를 생성하는 것은 좋은 생성 방식이 아님. 하지만 본 예시에서는 두 객체의 물리적 주소를 다르게 하기 위해 일부러 new를 사용함. valueOf를 통해 생성하는 것이 좋은 방법이지만 위 예제에서 valueOf를 사용하면 ==을 통한 비교 결과도 true이기 때문에 예제가 설명하고자 하는 목적과 맞지 않아 new를 사용)
    

### 하위 클래스가 상위 클래스의 equals 만으로 동일성을 판단할 수 없는 경우

- 하위 클래스에서 equals를 오버라이딩하지 않으면 상위 클래스의 equals를 그대로 이용하게 되는데, 이 경우 정보 불충분 등으로 동일성을 제대로 판단하지 못할 수도 있음
- **예시 - Point와 ColorPoint**
    
    다음은 2차원 공간의 점을 나타내는 Point 클래스
    
    ```java
    class Point {
    
        private int x;
        private int y;
    
        public Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
    
        @Override
        public boolean equals(Object obj) {
            if (this == obj) return true;
            if (!(obj instanceof Point)) return false;
            Point p = (Point) obj;
            return this.x == p.x && this.y == p.y;
        }
    
    }
    ```
    
    이를 상속하는 ColorPoint라는 클래스에서 color 라는 새 정보를 필드로 소유한다고 하면, 상위 클래스인 Point의 equals 만으로는 색상 일치 여부를 알 수 없음
    
    이러한 경우에는 색상 정보까지 포함하여 일치 여부를 판단하도록 equals를 오버라이딩해야 함
    

## equals를 오버라이딩할 때 준수해야 할 규약

- `반사성`: null이 아닌 x에 대해 x.equals(x)는 반드시 참
- `대칭성`: null이 아닌 x, y에 대해 x.equals(y)가 참이면 y.equals(x)도 참
- `추이성`: null이 아닌 x, y, z에 대해 x.equals(y)가 참이고 y.equals(z)가 참이면 x.equals(z)도 참
- `일관성`: null이 아닌 x, y에 대해 x.equals(y)를 반복해서 호출한 결과는 항상 참이거나 거짓
- `not null`: null이 아닌 x에 대해 x.equals(null)은 항상 거짓

## equals 오버라이딩의 좋은 예

```java
@Override
public boolean equals(Object o) {
	if (o == this) return true;
	if (!(o instanceof MyClass)) return false;
	MyClass m = (MyClass) o;
	// m과 this 간 필드 비교
	// ...
}
```

1. ==를 통한 비교 결과가 참인지 확인 (물리적으로 동일한 경우 무조건 동일)
2. 동일한 클래스/인터페이스의 인스턴스인지 확인 (아니라면 거짓)
3. 명시적으로 형변환한 뒤, 동일해야 하는 필드에 대한 동일 여부 비교
    - 동일할 필요가 없는 필드를 잘 제외하는 것 또한 중요