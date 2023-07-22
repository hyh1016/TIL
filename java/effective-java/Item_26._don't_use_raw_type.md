# Item 26. 로우 타입(raw type)은 사용하지 말라

## 로우 타입

- 제네릭을 지원하기 이전 코드와의 **호환성**을 위해 제네릭 타입에서 타입 매개변수를 생략한 상태의 타입
- 호환성을 위한 것일 뿐, 로우 타입은 `타입 불일치 예외를 컴파일 타임으로 가져오는 제네릭의 이점`을 누리지 못하게 만들기 때문에 사용하지 않는 것이 좋음
    - 예외는 최대한 런타임보다는 컴파일 타임에 발생하도록 하는 것이 좋음
    - 런타임에 발생한 에러는 원인을 추적하기 더 어렵고, 더 큰 손해를 불러올 수 있기 때문
- 타입을 확정지을 수 없어 로우 타입을 사용하려고 하는 경우에는, **와일드카드 타입**을 사용하는 것이 좋음

## 로우 타입 vs Object 타입 vs 와일드카드 타입

- 세 가지 모두 어떤 타입이든 저장할 수 있다는 점에서는 동일하지만, Object 타입과 와일드카드 타입은 안전

### 로우 타입

- 아예 제네릭 타입 시스템 자체에 속하지 않음
- 변수로 선언된 경우에도, 매개변수로 전달되는 경우에도 잘못된 제네릭 타입 지정에 의한 컴파일 에러가 발생하지 않음
    - 변수로 선언된 경우 - 컴파일 에러 없음
    - 매개변수로 전달되는 경우 - 컴파일 에러 없음
        
        ```java
        public static void main(String[] args) {
        		// 가능
            List list1 = new ArrayList();
            list1.add("string");
            list1.add(Integer.valueOf(1));
            list1.add(Boolean.valueOf(true));
            print(list1);
        }
        
        // 가능
        public static void print(List list) {
            list.forEach(System.out::println);
        }
        
        // 가능
        public static void print(List<String> list) {
            list.forEach(System.out::println);
        }
        ```
        

### Object 타입

- 어떤 타입의 데이터이든 담을 수 있으나, 다른 제네릭 타입으로 형변환은 불가능
    
    ```java
    public static void main(String[] args) {
    		// 가능
        List<Object> list1 = new ArrayList();
        list1.add("string");
        list1.add(Integer.valueOf(1));
        list1.add(Boolean.valueOf(true));
        print(list1);
    }
    
    // 불가능
    public static void print(List<String> list) {
        list.forEach(System.out::println);
    }
    ```
    

### 와일드카드 타입

- 제네릭 타입의 매개변수를 받고 싶으나 어떤 타입의 데이터가 들어올지 모를 때 사용
- Collection<?> 변수를 선언할 시 null 외의 어떤 데이터도 넣을 수 없음
    
    ```java
    public static void main(String[] args) {
    		// 불가능
        List<?> list1 = new ArrayList();
        list1.add("string");
        list1.add(Integer.valueOf(1));
        list1.add(Boolean.valueOf(true));
        print(list1);
    }
    
    // 어떤 타입의 변수든 가능
    public static void print(List<?> list) {
        list.forEach(System.out::println);
    }
    ```
    

## 그럼 언제 로우 타입을 사용?

### class 리터럴

- JVM이 생성해주는, 특정 객체의 클래스 객체를 반환하는 표현식
    - 해당 클래스의 정보를 가지고 있음
- class 리터럴에는 제네릭 타입을 사용할 수 없음
    - 정확히는, array 타입과 primitive 타입을 제외하고는 클래스 리터럴에 매개변수화 타입을 사용할 수 없음

### instanceof

- 런타임에 인스턴스의 타입을 체크하는 연산자
- 런타임에는 제네릭 타입의 정보가 없기 때문에(컴파일 과정에서 해당 타입에 대한 명시적 형변환 문으로 변경됨), 해당 연산자를 사용할 때에는 로우 타입을 사용해야 함
