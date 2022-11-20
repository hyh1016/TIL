# ❓ Generic

## 제네릭 (Generic)

### 정의

- 컴파일 타임에 타입을 체크해 주는 기능
- 제네릭의 사용은 두 가지 이점을 가진다.
    1. 지정한 타입 이외의 타입을 가진 데이터가 할당되면 컴파일 에러를 발생시킨다. 따라서, `타입 안정성`을 보장할 수 있다.
        - ex) List<String>으로 선언하면 String 이외 값이 들어가면 컴파일 에러가 발생
    2. 제네릭으로 선언한 값은 묵시적 형변환이 가능하다.
        - List<String> 해당 필드로부터 꺼낸 값은 형변환 없이도 String으로 간주
        - 내부적으로 컴파일러가 명시적 형변환이 필요한 경우 추가해주기 때문

### 사용 이유 (목적)

- 제네릭 이전에는 어떤 자료형인지 확정되지 않아 어떤 타입의 값을 넣든 컴파일 에러가 발생하지 않았고, 만약 이를 특정 자료형으로 이용하고자 한다면 명시적으로 형변환을 해줬어야 했다.
    - 그러나 이는 `런타임 에러`를 발생시킬 가능성을 내포하는데, 런타임 에러는 최대한 컴파일 에러로 돌리는 것이 좋다. 컴파일 에러는 프로그램을 실행하지 않고도 정정하는 것이 가능해 개발 중에 감지하고 수정할 수 있기 때문이다. (또한, 요즘 대부분 IDE는 컴파일하지 않고도 컴파일 에러는 알려 줌)
- 정리하자면, 제네릭은 ⭐잘못된 형변환에 의해 발생하는 런타임 에러인 `ClassCastException`을 컴파일 타임으로 끌어오도록 하는 역할을 수행⭐한다. 이것이 제네릭을 사용하는 가장 큰 이유(목적)이다.

## 제네릭 적용

### 제네릭 클래스

- 클래스를 작성할 때 타입 변수를 명시한 것
- 객체를 생성할 때 타입 변수 자리에 실제 타입을 지정(대입)할 수 있다.
- 클래스명 옆에 <타입 변수>를 명시함으로써 선언 가능하며, 클래스 내부의 `필드 타입`, `파라미터 타입`, `반환 타입`으로 사용할 수 있다.
- 제네릭 클래스 선언 시 다음에 유의해야 한다.
    - 제네릭 클래스 내부에서도 어떤 변수든 생성 시점에서는 타입 변수가 오면 안 된다.
    (당연히 생성 시점에는 타입이 확정돼야 함)
    - static 필드 또는 메소드에는 타입 변수를 사용할 수 없다.
    (static 필드/메소드는 모든 인스턴스가 공유하는 요소이므로 인스턴스별로 타입이 지정될 수 없음)
- 제네릭 클래스의 대표적인 예시로는 Collection의 List, Set, 그리고 Map 자료구조 등이 있다.
    
    ex) ArrayList는 JDK1.5에서 제네릭 기능이 추가되면서 다음과 같이 구현되었다.
    
    ```java
    public class ArarayList<E> extends AbstractList<E> {
    	
    	private transient E[] elementData;
    	
    	public boolean add(E o) { ... }
    
    	public E get(int index) { ... }
    
    }
    ```
    

### 제한된 제네릭 클래스 (타입 제한)

- 타입 변수를 <T extends 클래스>으로 설정하면 타입 지정 시 특정 타입(과 그 자손)만 가능하게 타입을 제한할 수 있다.
    - <T extends 인터페이스>의 경우에도 implements가 아닌 extends를 쓴다.
- ⭐ 이와 같이 타입을 제한하면 해당 클래스/인터페이스의 메소드를 사용할 수 있다는 장점이 있다.
- ex) 모든 타입 객체를 저장할 수 있는 `Box`와 과일 객체만 저장할 수 있는 `FruitBox`
    
    ```java
    class Box<T> {
    
    	List<T> list = new ArrayList<T>();
    
    	void add(T item) { list.add(item); }
    	T get(int i) { return list.get(i); }
    
    }
    
    // Box의 기능을 그대로 제공하되 오직 과일만 넣을 수 있는 클래스
    class FruitBox<T extends Fruit> extends Box<T> {}
    ```
    

### 와일드카드

- <T extends 클래스명>은 클래스의 선언 시점에 사용하는 것이고, 와일드카드는 이와 같은 동작을 하나 인스턴스 선언 시점에 사용하는 것이다.
- 와일드카드를 이용하면 하나의 참조형 변수가 가능한 타입 범위 내에서 여러 타입의 인스턴스를 참조할 수 있다.
- 그러나 주의할 점은, 어쨌든 참조가 가능한 것이 여러개일 뿐 참조(생성 및 할당) 시점에는 단 하나의 타입으로 제한되어야 한다는 것이다.
- 타입 제한 클래스와 마찬가지로 <? extends List> 하면 어쨌든 List로 간주하여 List의 메소드 이용 가능하다.
- <? extends 클래스> 사용하면 해당 클래스와 그 자손들만 할당이 가능하다.
    - 해당 클래스로 간주하고 이용할 수 있으므로(다형성) 가장 많이 사용된다.
- <? super T> 사용하면 해당 클래스와 그 조상들만 할당이 가능하다.
- ex) 동일한 참조형 변수에 타입 제한을 만족하는 여러 타입 할당 가능
    
    ```java
    class Product {}
    class Tv extends Product {}
    class SamsungTv extends Tv {}
    
    ArrayList<? extends Product> list = new ArrayList<Tv>();
    // 가능. Product, TV, SamsungTv 가능
    
    ArrayList<? super Product> list = new ArrayList<Tv>();
    // 불가능. Product, Product의 부모 클래스들(Object 등) 가능
    ```
    
- 와일드카드는 메소드의 매개변수 안에서도 사용 가능하며, static 메소드에서도 사용이 가능하다.
    
    ```java
    static Juice makeJuice(FruitBox<? extends Fruit> box) {
    	// FruitBox에는 Fruit 또는 그를 상속하는 어떤 것도 대입 가능
    }
    ```
    

### 제네릭 메소드

- 메소드를 정의할 때 타입 변수를 선언하는 것이다.
- 제네릭 클래스와 같이 사용할 수도 있다.
    - 다른 타입 변수명을 사용할 것을 권장하나 같은 변수명을 사용하면 제네릭 메소드의 타입 변수가 더 우선시된다.
        - global variable보다 local variable이 더 우선권을 갖는 것과 유사
- 제네릭 메소드의 영향 범위는 `해당 메소드의 파라미터` 뿐이다.
- 제네릭 메소드에서의 타입은 대부분 생략이 가능하다.
- static 메소드에도 사용할 수 있다. (메소드 호출 시마다 타입을 결정하므로)
- 제네릭 메소드를 이용하는 방식, 와일드카드를 이용하는 방식은 서로 같은 의미로 사용될 수 있으며, 이 경우 둘 중 하나를 선택해서 사용하면 된다.
    
    ex) 임의의 과일 타입 객체를 받아 주스를 만들어 반환하는 메소드
    
    ```java
    // 제네릭 메소드를 이용
    static <T extends Fruit> Juice makeJuice(FruitBox<T> box) {
    }
    
    // 와일드카드를 이용
    static Juice makeJuice(FruitBox<? extends Fruit> box) {
    }
    ```
    
    - 대부분 와일드카드를 우선적으로 쓰고, 쓸 수 없을 때 대안으로 제네릭 메소드를 사용한다.

## Reference

[Java의 정석 - ch 12. 제네릭](https://www.youtube.com/watch?v=QcXLiwZPnJQ&list=PLW2UjW795-f6xWA2_MUhEVgPauhGl3xIp&index=135)
