# 🗂 Class Diagram

> 다이어그램
> 
> - **Class Diagram**
> - Use Case Diagram
> - Sequence Diagram

## 클래스 다이어그램

### 정의

시스템의 정적인 면을 표현하기 위해 주로 사용되는 UML 구조 다이어그램

클래스, 클래스 간 관계를 보여준다.

### 표현 예시

- 객체명
    
    ![객체명](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/d54feaf2-2edf-411c-95f3-7fbd90e5289f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220417%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220417T141832Z&X-Amz-Expires=86400&X-Amz-Signature=e9dca8dc212d5ff7332854b842559d9ed90fca116b9fd38786d6d61bcc1aa34e&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)
    
- 객체명 + 필드
    
    ![객체명+필드](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/5435320b-75d0-4e1e-8c41-0ad72011a233/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220417%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220417T141857Z&X-Amz-Expires=86400&X-Amz-Signature=1a1cd4a6e6bbc91ab968fb88f827f19fc9feeea03bbb6ae6a2dd5f8ab7ffddb2&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)
    
- 객체명 + 메서드
    
    ![객체명+메서드](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/7a64c671-3484-4ba4-9893-026944eb3ba5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220417%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220417T141912Z&X-Amz-Expires=86400&X-Amz-Signature=ab56decf2cbf7c3165619f7ac754bb3b95bfaa3411128143a5f1c1f40a927d17&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)
    
- 객체명 + 필드 + 메서드
    
    ![객체명+필드+메서드](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/c9929945-b5e8-4a14-b8ef-c6a7074d049a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220417%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220417T141924Z&X-Amz-Expires=86400&X-Amz-Signature=da6f1ac82328ed4b2ae26fed189f42688b8ba3e3739556dcfc2fe5fd22b6af99&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)
    

### 용도에 따른 표현 예시

- 분석 단계: 타입(자료형), 가시화 정보(접근 제어자) 생략
    
    ![분석단계](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/9cdc1f70-1172-4aba-afa8-c027918e8717/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220417%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220417T141939Z&X-Amz-Expires=86400&X-Amz-Signature=0d15fdf34636c0a2f0cb07671306138af919410afc023c356c4a2b6faf55e29b&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)
    
- 설계 단계: 타입(자료형), 가시화 정보(접근 제어자) 포함
    
    ![설계단계](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/dee9174b-8a47-4f2e-b42e-fc5eb7c5c8d9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220417%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220417T141952Z&X-Amz-Expires=86400&X-Amz-Signature=9d187077f30792a5d82b3023a11a80770efa8ebfb405d9875e03fdc6837d8926&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)
    

### 클래스 간 관계 표현법

1. **연관 (Association)** - 한 클래스가 다른 클래스를 `사용`
2. **일반화 (Generalization)** - 상속 관계
3. **집합**
    
    3-1. **집약 (Aggregation)** - 포함 관계를 가지지만 독립적 라이프타임을 가짐
    
    3-2. **합성 (Composition)** - 포함 관계를 가지며 의존적 라이프타임을 가짐
    
4. **의존 (Dependency)** - 한 클래스가 다른 클래스를 `인자로 받아 사용`
5. **실체화 (Realization)** - 인터페이스의 구현

## 연관 (Association)

### 방향성

클래스 간 연관 관계는 양방향이거나 단방향이다.

양방향은 `선(—)`, 단방향은 `화살표(→)`로 표기한다.

- 양방향
    
    ![양방향](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/6100fafe-cde0-474b-8a47-802d652b9e3e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220417%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220417T142029Z&X-Amz-Expires=86400&X-Amz-Signature=8696ebe0cb7f9627918adfc554f6659253816f513477b531b342e063cfd3cecb&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)
    
- 단방향
    
    ![단방향](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/b09ca1a1-798d-4993-82a7-2a5c8f341129/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220417%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220417T142042Z&X-Amz-Expires=86400&X-Amz-Signature=c7445eb018a6b69e23e24d97b38e88c60e3bf837ddee7e81f29918a35b9de1b3&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)
    
    단방향인 경우 A→B이면 A만 B를 참조하고 B는 A에 대해 알지 못함을 뜻한다.
    

### 다중성

클래스 간 연간 관계는 일대일, 일대다, 다대다 관계를 갖는다.

- 일대일 (1:1)
    
    ![1:1](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/28cd2e63-19df-4bf9-8fd1-ab4e26093a3d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220417%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220417T142100Z&X-Amz-Expires=86400&X-Amz-Signature=f8b6e83f0fe900d1c764add42a624d207d6cec72bd16ba51d3ee45c571872743&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)
    
- 일대다 (1:N)
    
    ![1:N](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/7d1bc68d-b155-4516-b7ea-a740fdd19908/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220417%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220417T142112Z&X-Amz-Expires=86400&X-Amz-Signature=6fce9491c39550ef75935478c5a2ee11c76f54f5b7b365f85d429c48d6fb1237&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)
    
- 다대다 (N:M)
    
    ![N:M](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/3ba97963-4195-4738-a0a4-d3d3ebb33536/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220417%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220417T142124Z&X-Amz-Expires=86400&X-Amz-Signature=4aafe6f51f1f26817b5d1a1b8c51a312a5867bb9a631ddb57b4dee8726f94efa&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)
    
    다대다는 연관 클래스를 만들어 두 개의 일대다 관계로 만들 수 있다.
    
    ![N:M(2)](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/4c558e5c-f4f9-43be-938c-0ab44ed93fe2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220417%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220417T142144Z&X-Amz-Expires=86400&X-Amz-Signature=fd8859e374891e7560839089242005d087f7fd7ea3a3facbfea88033481fe0ca&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)
    

### 재귀

- 클래스가 재귀적으로 연관되나 사이클이 발생하지는 않는다.
    
    ![재귀](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/253ba05f-ed5f-4f5a-9de0-66238f028392/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220417%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220417T142219Z&X-Amz-Expires=86400&X-Amz-Signature=d74c78af6fe886c482190fedba84af7ddfe79fc66aa3a4932537315127c9656c&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)
    
- 리눅스의 파일 계층 구조가 이에 해당한다.

## 일반화 (Generalization)

### 정의

공통된 특징을 묶어 추상클래스 또는 인터페이스로 정의한 뒤 상속 또는 구현을 이용하는 것

`속이 빈 실선 화살표`로 표기한다.

### 예시

- 가전제품에는 다양한 제품이 포함되고, 해당 제품 또한 세부적인 카테고리를 가질 수 있다.
    
    ![Generalization](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/a84177a2-c406-4bac-84f2-67b7721bf322/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220417%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220417T142237Z&X-Amz-Expires=86400&X-Amz-Signature=6269a1e451ba7a92a88b7d84d0196746b3c87b80a3c3826e4465aef9bfdad61a&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)
    

## 집합 (Aggregation, Composition)

### 정의

- 한 객체가 다른 하나를 포함
- 각 객체의 라이프타임의 독립 의존 여부에 따라 집약, 합성으로 나뉜다.
- 집합은 연관(Association)의 특수한 경우에 해당한다. 즉, 연관에 포함된다.

### 집약 (Aggregation)

- 전체 객체와 부분 객체의 라이프타임이 독립적인 포함 구조
- 전체 객체가 사라져도 부분 객체는 유효하여 사라지지 않는다.
- 부분 객체를 여러 전체 객체가 공유할 수 있다.
- 구현 단계에서는 부분 객체를 별도로 생성하고 파라미터로 받는다.
- `빈 마름모`로 표기한다.
    
    ![Aggregation](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/99a0d600-f398-40a9-9074-9900289895f5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220417%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220417T142300Z&X-Amz-Expires=86400&X-Amz-Signature=8bea7dc477d9a71343825572d7d1ad9e1bdbac080452126691ebcdd37c63c370&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)
    

### 합성 (Composition)

- 전체 객체와 부분 객체의 라이프타임이 의존적인 포함 구조
- 전체 객체가 사라지면 부분 객체는 불유효해져 사라진다.
- 부분 객체를 여러 전체 객체가 공유할 수 없다.
- 구현 단계에서는 부분 객체를 전체 객체 내부의 필드로 생성한다.
- `꽉 찬 마름모`로 표기한다.
    
    ![Composition](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/2edacb1e-3390-43af-bf02-4233ee9e54d4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220417%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220417T142313Z&X-Amz-Expires=86400&X-Amz-Signature=f8f5feddb44aeb8b5841581c988be563418bba70655029125e8512cf278e2cba&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)
    

## 의존 (Dependency)

### 정의

클래스가 다른 클래스를 사용하는 세 가지 방법이 있다.

1. 클래스의 필드로 참조 할당
2. 연산의 인자(parameter)로 사용
3. 메서드 내부의 지역 객체

여기서 1번이 연관, 2번이 의존, 3번이 합성에 해당한다.

`점선 화살표`로 표기한다.

### 예시

- 누군가 출근하면서 자동차를 타고 주유소를 이용한다고 하면, 다음과 같은 클래스 다이어그램을 그릴 수 있다.
    
    ![Dependency](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/8041ce33-6c69-490a-a2c0-42c9442f7c28/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220417%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220417T142326Z&X-Amz-Expires=86400&X-Amz-Signature=592120279dd0d067d25efb4b39566c7bf3f713a54c7227101d3c2a4e86d14eec&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)
    
    - 사람은 자동차를 이용하되, 항상 같은 차를 이용한다. 자동차를 바꾸는 일은 거의 없다.
    - 자동차는 주유할 때 특정 주유기만을 고집하지 않는다. 매번 다른 주유기를 이용할 수 있다.
    - 따라서 사람은 자동차를 필드로 소유하고(사용), 자동차는 주유소에 의존한다.

## 실체화 (Realization)

### 정의

어떤 객체들의 공통되는 능력, 특징 들을 모아 인터페이스-구현 구조를 형성

### 예시

- 비행기와 새는 날 수 있다는 공통점이 있다. 이를 추상화하고 구현하면 다음과 같다.
    
    ![Realization](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/ec0a5a81-b496-4bcf-94ce-ca51802bb098/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220417%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220417T142346Z&X-Amz-Expires=86400&X-Amz-Signature=202a7eb4c1693a390bae2343632df3b0bc7b6209af4f98011989d3c6dee8afbf&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)
