# Item 33. 타입 안전 이종 컨테이너를 고려하라

## 제네릭 컨테이너

- 제네릭 컨테이너는 컨테이너 당 하나의 타입만 매개변수화할 수 있음
    - List<String> 컨테이너는 String 타입만 받을 수 있다는 뜻
- 하지만 제네릭 컬렉션 등의 경우 더 유용하게 사용해야 할 때가 있음
    - 하나의 컬렉션 내에 여러 개의 타입 매개변수를 저장하고 싶다거나 한 경우
    - 그렇다고 타입 매개변수를 Object로 지정해버리면 제네릭의 타입 안전성을 누릴 수 없음
    - 또한, 꺼낼 때마다 알맞은 타입으로 명시적 형변환을 해 주어야 함
        - 이 과정에서 잘못된 타입이 들어가 있었다면 `ClassCastException`을 발생시킬 것
- 유연하게 사용하면서 타입 안전성은 유지하기 위해, `타입 안전 이종 컨테이너 패턴(Type Safe Heterogeneous Container Pattern)`을 이용할 수 있음

## 예시

### 클래스 객체를 키로 하는 맵

- 아래와 같은 자료구조를 갖는 클래스를 선언
    
    ```java
    Map<Class<?>, Object> unsafeMap = new HashMap<>();
    ```
    
- 저장하려는 객체의 타입을 키로 하도록 하여 여러 타입을 저장하고 가져오는 시점에 해당 타입으로 명시적 형변환을 할 수 있음
- 하지만 임의로 잘못된 타입을 키로 지정해 데이터를 넣게 되면 타입 안전성이 깨짐

### 타입 안전 이종 컨테이너 패턴을 적용

- 아래와 같이 `클래스 객체와 넣을 객체가 같은 타입 매개변수를 공유하도록` 함으로써 알맞은 타입의 객체가 삽입되도록 할 수 있음
    
    ```java
    Map<Class<?>, Object> safeMap = new HashMap<>();
    
    public <T> void put(Class<T> type, T instance) {
        safeMap.put(Objects.requireNonNull(type), type.cast(instance));
    }
    
    public <T> T get(Class<T> type) {
        return type.cast(safeMap.get(type));
    }
    ```
    
- Class 역시 제네릭 클래스이기 때문에, get이 호출되는 시점에 T가 결정되며 이 T를 기반으로 타입 체크를 한 후 명시적 형변환을 하는 cast 메서드를 이용할 수 있음
- 데이터 삽입 시점에서도 캐스팅을 해주는 이유는 `클래스 객체 역시 제네릭 클래스이기 때문에 임의로 로 타입의 클래스(Class.class)가 전달되는 경우 타입 안전성이 깨지기 때문`

### 타입 안전 이종 컨테이너의 단점

- 아래와 같이 key로 사용된 것이 제네릭 클래스일 때에는 타입 안전성을 보장할 수 없음
    
    ```java
    List<Integer> list = List.of(1, 2, 3);
    putList.class, list);
    List<String> stringList = f.getFavorite(List.class); // only compile warning
    stringList.forEach(System.out::println); // 호출 시점에 ClassCastException 이 발생
    ```
    
- 제네릭은 실체화가 불가하기 때문에, 제네릭 클래스는 로우 타입으로 사용하면 타입 정보가 손실됨
- 그런데 제네릭 클래스의 클래스 객체는 로우 타입
    - List<Integer>의 클래스 객체도, List<String> 클래스 객체도 List.class로 동일

## 타입 안전 이종 컨테이너의 문제점 우회하기

> 이 내용은 책에 기술된 내용은 아니고 제 개인적 정리입니다.
> 

사실 위의 단점이 문제가 되는 경우가 많았는데, 특히 역직렬화 과정에서 제네릭 클래스의 객체를 획득하려고 할 때에 이 `제네릭은 실체화가 불가능해 제네릭 클래스의 클래스 객체는 로우 타입 정보만을 갖는 문제`가 많은 난관이 되었다.

일부 역직렬화기는 변환하려는 객체의 타입 정보를 전달할 때 로우 타입만 전달하면 제대로 동작하지 않았고(아마도 타입 안전성 보장을 위해서인가보다), 명시적으로 타입을 지정해주기 위해 아래와 같은 익명 클래스를 생성해 전달했다.

```java
new TypeReference<List<String>>() {}
```

이 클래스는 내부적으로 `제네릭 클래스를 받아 타입 매개변수의 타입을 멤버 변수로 저장`한다.

따라서 이 클래스를 전달하면 `런타임에 제네릭 클래스의 타입 정보가 소거되어도 이 클래스에 저장된 멤버 변수 타입값을 참조해 제네릭 클래스의 타입을 확인할 수 있는 것`이다.

이 [스택오버플로우](https://stackoverflow.com/questions/67866342/what-is-typereference-in-java-which-is-used-while-converting-a-json-script-to-ma) 에서도 TypeReference의 존재 이유에 대해서 잘 설명해주고 있다.