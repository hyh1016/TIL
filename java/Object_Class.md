# Object Class

## Object

모든 클래스의 부모 클래스. 즉, 최고 조상 클래스

어떠한 필드 값도 가지지 않으며, 모든 객체가 행할 수 있는 행동들을 정의한 메소드들만을 갖는다.

## Object의 주요 메소드

### Equals

* 객체 자신(this)과 주어진 객체(obj)를 비교해서 같으면 true, 다르면 false 반환
* Object 클래스에 포함되며 객체의 주소를 비교

### hashCode

* 객체의 `해시코드`를 반환하는 메소드
* Object 클래스에 포함되며 `객체의 주소를 int로 변환`해서 반환
* equals를 오버라이딩하면 hashCode도 오버라이딩해야 함
  * `⭐ equals의 결과가 true인 두 객체의 해시코드는 같아야 하기 때문`
*   만약 특정 클래스에서 인스턴스들이 필드값이 일치한 경우 동일한 객체로 간주하려고 한다면 equals와 hashCode 메소드를 다음과 같이 오버라이딩하면 된다.

    ```java
    class Product {
        String name;
        int price;

        @Overriding
        // 오버라이딩이기 때문에 parameter type은 변경 불가
        public boolean equals(Object obj) {
            // 별도로 타입 체크 예외처리 해야 함
            if (!(obj instanceof Product))
                return false;

            Product other = (Product) obj;
            return this.name.equals(obj.name) && this.price == obj.price;
        }

        @Overriding
        // equals가 동일 필드에서 true이므로
        // hashCode도 필드가 같으면 동일한 결과가 나오도록 오버라이딩
        public int hashCode() {
            return Objects.hash(name, price);
        }
    }
    ```

### toString

* 객체를 문자열로 변환하여 반환
* `클래스명@16진수주소값` 으로 이루어짐 (Object의 toString)
* stdout으로 출력 시 호출됨

### getClass

* 해당 객체의 클래스 타입을 반환한다.

### clone

* 해당 객체를 복사한 새로운 객체를 반환한다.
* Object에 정의된 clone 메소드는 단순히 기본형 자료형의 필드 값만을 복사하기 때문에, 참조형 필드를 포함하는 클래스에서 clone 메소드를 호출하고자 한다면 clone 메소드를 재정의(Overriding)해야 한다.
