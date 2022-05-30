# 📜 Builder Pattern

## Builder Pattern (빌더 패턴)

![Builder-Pattern](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/1c7e8012-fdc4-4c07-a9a8-3fcbc877aa4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220530%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220530T021615Z&X-Amz-Expires=86400&X-Amz-Signature=7f791ed8c8d381be2fcfdc30d9634071bc7be06a4295548fce98a3e236a1f375&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

일반적으로 객체를 생성할 때에는 생성자(constructor)가 제공되며 new 문법을 통해 생성자를 이용한다.

그러나 객체에 너무 많은 생성자가 선언되면 객체 내부에 있는 객체 생성 로직이 길어져 코드가 지저분해지고, 책임이 분리되지 않는다.

또한, 기존 방식의 가장 치명적인 문제점은, 모든 데이터가 한 번에 준비되지 않아 일부 데이터만 제공된 상태로 객체를 생성할 때 해당 생성 과정이 유효한지 판단하는 로직이 없다는 것이다.

이러한 기존 생성자의 문제점을 해결하기 위해 사용하는 것이 `빌더 패턴`이다.

### 구성 요소

- `Director` - Builder를 이용해 Product를 생성하는 클래스
- `Builder` - Builder에 다형성을 적용하기 위한 인터페이스 (Builder가 하나 뿐이라면 생략 가능)
- `ConcreteBuilder` - 만들고자 하는 객체(Product)에 대해 점증적으로 값을 받고 이를 생성하여 반환하는 클래스
- `Product` - Builder가 만들어내는(반환하는) 결과물

### 구현 방법

- Builder 클래스는 Java에서는 주로 `public static class`로 선언된다.
    
    ```java
    public class ProductFactory {
    
    	private String name;
    	private int price;
    
    	public static class Builder {
    		
    	}
    
    	private ProductFactory(Builder builder) {
    		this.name = builder.name;
    		this.price = builder.price;
    	}
    }
    ```
    
- 필요한 데이터를 받는 메소드들은 다음과 같이 구현된다.
    
    ```java
    public Builder name(String name) {
    	this.name = name;
    	return this;
    }
    
    public Builder price(int price) {
    	this.price= price;
    	return this;
    }
    ```
    
    이는 다음과 같이 체인을 이어가 점증적으로 데이터를 채워나가기 위함이다.
    
    ```java
    // in Director
    Product product = ProductFactory.builder()
    										.name("Milk")
    										.price(2900)
    										.build();
    ```
    
- Product를 생성하는 메소드 `build`는 다음과 같이 구현된다.
    
    ```java
    public Product build() {
    	return new Product(this);
    }
    ```
    
    왜 이렇게 작동하는 것이 가능한가? 이는 Product 클래스에서 다음과 같은 프라이빗 생성자를 구현하기 때문이다.
    
    ```java
    private ProductFactory(Builder builder) {
    	this.name = builder.name;
    	this.price = builder.price;
    }
    ```
    
    이는 외부에서 호출할 수는 없으나 Product의 inner class인 Builder에서는 호출할 수 있다.
    
    따라서 Builder의 사용자는 직접 Product를 생성할 수는 없고 Builder를 통해 Product를 생성하는 것이다.
