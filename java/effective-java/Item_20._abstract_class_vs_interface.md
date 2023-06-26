# Item 20. 추상 클래스보다는 인터페이스를 우선하라

## 추상 클래스 vs 인터페이스

### 상속/구현하는 클래스의 계층 구조 생성 여부

- 추상 클래스는 이를 상속하는 모든 하위 클래스들의 공통 조상이어야 함
- 인터페이스는 다양한 종류의 클래스가 수행할 수 있는 `부가 기능`을 추가하게 할 수 있음
    - 하나의 인터페이스를 구현하는 클래스들이 모두 같은 계층으로 묶일 필요가 없음
    - 이러한 점 덕분에 특정 인터페이스가 등장했을 때 다양한 클래스들이 추후 릴리스에서 이 인터페이스를 추가할 수 있음
        - ex) Comparable, Iterable 등

### 기본 기능에 부가 기능을 추가하는 방법

- 추상 클래스는 기존 동작에 추가적인 기능을 추가하기 위해서는 반드시 `상속`을 해야 함
    - 유연성 면에서 좋지 않고, 부작용이 있을 수 있음 (Item 18)
- 인터페이스는 컴포지션과 함께 이용하여 해당 인터페이스를 구현한 모든 클래스를 내부 필드로 소유하여 부가 기능을 추가하는 활용성이 좋은 `래퍼 클래스`를 제공할 수 있음

## 두 가지의 장점을 모두 취하는 추상 골격 구현

```java
interface Interface {
    default void print() {
        System.out.println("기반 메서드");
    }
}

abstract class AbstractInterface implements Interface {
    @Override
    public int hashCode() {
        return super.hashCode();
    }

    @Override
    public boolean equals(Object obj) {
        return super.equals(obj);
    }

    @Override
    public String toString() {
        return super.toString();
    }
}
```

- 인터페이스로 타입과 일부 디폴트 메서드를 구현
    - 이를 `기반 메서드`라고 함
- (추상) 골격 구현 클래스는  (오버라이딩이 필요한) 기반 메서드를 제외하고 나머지 확정 가능한 메서드를 구현
- 위와 같이 구현하면, 아래와 같이 생성 시점에 인터페이스로 획득하되 불필요한 구현은 생략할 수 있음

```java
class Item20 {
    public static void main(String[] args) {
				// 결과는 인터페이스로 받음
        Interface i = getInterface();
    }

    public static Interface getInterface() {
				// 기반 메서드만 오버라이딩하고, 오버라이딩하지 않아도 될 메서드는 추상 클래스가 구현하도록 함
        return new AbstractInterface() {
            @Override
            public void print() {
                System.out.println("오버라이딩한 기반 메서드");
            }
        };
    }
}
```

- 이와 같이 인터페이스의 특정 메서드를 오버라이딩함으로써 특정 기능만 제어하고, 나머지 부분은 추상 클래스에 의해 제어되도록 구현할 수 있음 (템플릿 메서드 패턴)
- 인터페이스를 이용하면서도 모든 내용을 구현할 귀찮음을 덜어주는 구현법
- 구현할 점이 많은 매우 복잡한 인터페이스라면, 골격 구현을 함께 제공하는 방법을 고려해보는 것도 좋음
- 대신 인터페이스/추상 클래스 내 오버라이딩이 가능한 메서드들은 Item 19에서 명시했듯 오버라이딩을 염두에 두고 문서화를 해야 함
