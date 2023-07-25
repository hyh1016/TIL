# @RequestParam, @RequestBody, @ModelAttribute

## @RequestParam

* Query Parameter로 데이터를 받아오기 위해 사용하는 어노테이션
* 파라미터명을 직접 지정해줄 수도 있고, (아래의 name) 파라미터명과 동일한 변수명을 사용하여 자동으로 바인딩되도록 할 수도 있다. (아래의 password)
*   기본적으로 쿼리 파라미터는 필수로 전달되어야 하며 생략하면 400 에러를 발생시키지만, required의 값을 false로 설정하여 생략하도록 할 수 있다. (아래의 password)

    ```java
    // URL?name=yihyun&password=1234
    @RequestMapping("/")
    public String renderMyInformation(Model model,
                                    @RepuestParam("name") String myName,
                                    @RequestParam(required=false) String password) {
    	model.addAttribute("name", myName);
    	model.addAttribute("password", password);
    	return "render할 jsp 파일명";
    }
    ```
*   생성자를 통한 바인딩이 가능하다.

    ```java
    public class Person {

    	private String name;
    	private String password;

    	public Person(String name) {
    		this.name = name;
    		this.password = "0000";
    	}

    	public Person(String name, String password) {
    		this.name = name;
    		this.password = password;
    	}

    }
    ```

    위와 같은 객체를 @RequestParam으로 받고자 한다면, name만을 넘겨주거나 name과 password를 넘겨주면 된다.
* 전달되지 않은 경우 사용할 디폴트 값을 지정할 수 있다. `defaultValue` 옵션을 이용한다.

## @RequestBody

* JSON 형식으로 들어오는 데이터를 Java Object로 받아오기 위해 사용하는 어노테이션
* `HttpMessageReader`가 Request Body로 들어온 데이터를 @RequestBody 어노테이션이 붙은 객체로 역직렬화를 수행한다.
  * Spring에서 JSON의 역직렬화는 `Jackson2HttpMessageConverter`가 수행한다. 이 경우 Setter 대신 `Reflection`을 이용해서 값이 할당된다. 따라서 POST 방식으로 데이터를 받을 @RequestBody의 클래스는 Setter를 가지지 않아도 된다.
* GET과 같이 Request Body가 존재하지 않는 HTTP 메소드를 이용하면 데이터는 Query String으로 전달된다. 따라서 역직렬화가 수행되는 것이 아니라 `WebDataBinder`에 의해 바인딩된다. `WebDataBinder`는 Setter를 이용해서 바인딩을 수행한다.

## @ModelAttribute

* Model에 Attribute가 존재한다면 이에 접근할 수 있다.
* Http Servlet 요청 매개변수의 이름과 메서드 인자의 이름이 일치한다면 데이터 바인딩
  * 이 때 유효성 검사도 함께 수행 가능
  * 즉, 쿼리 파라미터의 개별 변환 작업 없이도 데이터 바인딩 가능
* 즉 @ModelAttribute로 선언한 변수에는 Query Parameter, Form Data, Multipart가 모두 바인딩된다.
  * 그러나 앞의 두 개는 @RequestParam, @RequestBody를 이용해 받을 수 있으므로 @ModelAttribute는 주로 파일(Multipart)을 받기 위해 사용한다.
* 다음과 같은 순서로 동작한다.
  1. ModelAttribute 인스턴스 생성
  2. `WebExchangeDataBinder`가 다음을 수행
     * Query Parameter와 Form Field의 이름을 바인딩할 Object 필드명과 비교
     * 일치한다면 바인딩 (이 과정에서 타입 변환이 필요하다면 변환)
  3. 바인딩에 실패하면 `WebExchangeBindException`이 발생한다. 이를 통해 유효성 검사 가능
