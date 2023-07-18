# 태그 달린 클래스보다는 클래스 계층구조를 활용

## 태그 달린 클래스

- 하나의 클래스가 두 가지 이상의 의미를 표현할 수 있으며, 그 중 현재 표현하는 의미를 `태그` 값으로 알려주는 클래스
- 각 의미를 표현하기 위한 필드를 모두 소유하고, 태그 필드를 소유해야 함

### 예시 - 다양한 도형을 표현할 수 있는 Figure 클래스

```java
class Figure {
    enum Shape { RECTANGLE, CIRCLE };

    final Shape shape; // 태그 필드

    // shape가 사각형일 때를 위한 필드
    double length;
    double width;

    // shape가 원일 때를 위한 필드
    double radius;

    Figure(double length, double width) {
        shape = Shape.RECTANGLE;
        this.length = length;
        this.width = width;
    }

    Figure(double radius) {
        shape = Shape.CIRCLE;
        this.radius = radius;
    }

    double area() {
        return switch (shape) {
            case RECTANGLE -> length * width;
            case CIRCLE -> Math.PI * radius * radius;
        };
    }
}
```

### 태그 달린 클래스의 문제점

- 일단 SRP 위반
    - 하나의 의미 내 수정이 일어나면 전체 클래스에 영향을 미침
- 하나의 의미를 사용하기 위해 해당 의미에 사용되지 않는 필드들까지 초기화됨
- 새 의미를 추가하면 메서드 내 모든 switch 문을 수정해줘야 함
- 비효율적이고, 오류를 내기 쉬우며, 가독성도 안좋음

## 태그 달린 클래스 대신 클래스 계층구조를 활용

- 각 의미를 표현할 클래스의 뿌리(root)가 될 추상 클래스를 선언하고, 의미와 상관 없이 동일한 의미를 갖는 필드/동일한 동작을 수행하는 메서드를 root 클래스에 올림
- 의미에 따라 동작이 달라지는 메서드는 추상 메서드로 정의
- 루트 클래스를 확장(상속)한 구체 클래스를 의미별로 하나씩 정의하며, 해당 클래스 내에서 필요한 필드와 메서드를 선언

### 예시 - 위의 Figure 클래스를 클래스 계층구조로 변환

```java
abstract class Figure {
    abstract double area();
}

class Rectangle extends Figure {
    final double length;
    final double width;

    Rectangle(double length, double width) {
        this.length = length;
        this.width = width;
    }

    @Override
    double area() {
        return length * width;
    }
}

class Circle extends Figure {
    final double radius;

    Circle(double radius) {
        this.radius = radius;
    }

    @Override
    double area() {
        return Math.PI * radius * radius;
    }
}
```

- 각 구체 클래스들은 하나의 책임만을 수행
- 관련 없는 필드를 소유하지 않음
- 한 구체 클래스의 변화가 다른 구체 클래스에 영향을 미치지 않음
- 간결하고 명확하며, 새로운 구체 클래스를 추가하기 쉬움
- 기존 필드들은 `의미`가 변화할 수 있기 때문에 불변으로 정의할 수 없었으나, 클래스 계층구조를 사용한다면 생성자를 통해 값을 초기화한 뒤 값이 변화하지 않음을 보장할 수 있다면 불변으로 정의할 수 있음
