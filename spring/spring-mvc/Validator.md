
# 🍃 Validator

## 정의

```java
public interface Validator {
	boolean supports(Class<?> clazz); // 검증 가능 여부 확인
	void validate(Object target,Errors errors); // 검증
}
```

요청 파라미터에 대해 검증 가능한 객체인지 확인하고 검증하는 역할을 수행하기 위한 인터페이스

두 가지 방법을 사용할 수 있다.

1. 전역 범위에 대한 검증을 수행
2. 일부(컨트롤러) 범위에 대한 검증을 수행

## 구현

Validator 인터페이스를 구현하는 클래스를 선언한다.

```java
import org.springframework.validation.Errors;
import org.springframework.validation.Validator;

public class RegisterRequestValidator implements Validator {

    @Override
    public boolean supports(Class<?> clazz) {
        System.out.println("clazz: " + clazz.toString());
        return true;
    }

    @Override
    public void validate(Object target, Errors errors) {
        System.out.println("target: " + target.toString());
        System.out.println("errors: " + errors.toString());
    }

}
```

## 전역 범위의 Validator

Validator를 통해 전역 범위에 대한 검증을 수행하기 위해서 다음과 같이 이름이 정해진 빈으로 등록한다.

### 1. @Configuration 내 Bean으로 직접 등록 (getValidator 메소드를 오버라이딩해야 함)

```java
@Override
public Validator getValidator() {
    return new RegisterRequestValidator();
}
```

### 2. 검증이 필요한 컨트롤러 내 메소드에 @Valid 어노테이션 사용

```java
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.Errors;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

import javax.validation.Valid;

@Controller
public class HelloController {

    @GetMapping("/valid")
    @ResponseBody
    public String valid(@Valid ValidDto dto, Errors errors) {
        if (errors.hasErrors()) System.out.println("has error!");
        return "validation OK";
    }

}
```

## 컨트롤러 범위의 Validator

Validator를 통해 컨트롤러 범위에 대한 검증을 수행하기 위해서 @InitBinder 어노테이션을 사용한다.

```java
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.Errors;
import org.springframework.web.bind.WebDataBinder;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.InitBinder;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

import javax.validation.Valid;

@Controller
public class HelloController {

    @GetMapping("/valid")
    @ResponseBody
    public String valid(@Valid ValidDto dto, Errors errors) {
        if (errors.hasErrors()) System.out.println("has error!");
        return "validation OK";
    }

    @InitBinder
    protected void initBinder(WebDataBinder binder) {
        binder.setValidator(new RegisterRequestValidator());
    }

}
```

해당 컨트롤러 내 모든 메서드에 Validation이 적용된다.