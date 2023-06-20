# Item 16. public 클래스에서는 public 필드가 아닌 접근자 메서드를 사용하라

## 나쁜 예와 좋은 예

### 나쁜 예

```java
class Point {
	public double x;
	public double y;
}
```

### 좋은 예

```java
class Point {
    private double x;
    private double y;

    public Point(double x, double y) {
        this.x = x;
        this.y = y;
    }

    public double getX() {
        return x;
    }

    public double getY() {
        return y;
    }

    public void setX(double x) {
        this.x = x;
    }

    public void setY(double y) {
        this.y = y;
    }
}
```

- public 필드 대신 public 접근자 메서드를 제공하면 좋은 이유는, 메서드는 내부 표현 방식을 변경할 수 있기 때문
    - 값의 반환/주입 이외에도 다른 동작을 추가할 수 있음

## package 또는 private 클래스는 필드의 접근 제어자가 자유로움

- 어차피 패키지 밖에서는 사용할 수 없으므로 외부 접근이 없음
- 따라서 내부 필드가 어떤 접근 제어자를 가져도 이는 패키지 또는 클래스 내에서만 사용
- 이러한 필드는 필드를 노출하는 것이 더 깔끔한 구현이 된다면 그렇게 해도 됨
