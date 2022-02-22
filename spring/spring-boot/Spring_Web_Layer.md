
# ✔ Spring Web Layer (스프링 웹 계층)

![web-layer](https://user-images.githubusercontent.com/59721541/147876412-acb9cfe8-4357-4647-a274-033f7b5841b6.png)

### Web Layer
- 컨트롤러(`@Controller`)와 뷰 템플릿 등을 포함하는 영역
- 데이터는 DTO 형태로 존재
- 클라이언트의 요청과 이에 대한 응답을 처리
- 필터, 인터셉터, 예외 처리 등 요청/응답 처리 과정에서의 이슈를 다룸

### Service Layer
  - `@Service` 객체가 포함되는 영역
  - 컨트롤러가 포함된 웹 레이어 계층과 데이터 접근을 수행하는 리포지토리 계층을 중재
      - DTO ↔ Domain Model
  - 트랜잭션이 관리되는 부분

### Repository Layer
  - 데이터 저장소에 접근하는 영역
  - 데이터는 도메인 모델(Entity) 형태로 존재

### DTO
  - 계층 간 데이터 교환을 위한 객체
  - 별도의 로직을 갖지 않고 Getter, Setter만을 포함한다.

### Domain Model
  - 실제 테이블과 매치되는 객체들을 말함
  - DAO, VO 등이 이에 해당
  - 영속성(Persistence)을 유지해야 함
    - 이유는 JPA가 [Dirty Checking](../jpa/Dirty_Checking.md)이 적용되기 때문

### 비즈니스 로직을 처리하는 부분은?
  - Domain
  - Service에서 처리하면 Domain이 의미가 없어진다. Service는 단순히 Domain이 제공하는 메소드의 순서, 트랜잭션을 다룬다.

### Spring에서의 처리 흐름
1. Request가 들어오면 Controller가 이를 받아 Service를 호출한다.
   이 과정에서 데이터는 DTO 형태로 Service Layer에 제공된다.
2. Service는 DTO를 받아 Entity로 변환하고, Domain이 제공하는 메소드를 순서에 맞게 호출한다.
   필요하다면 `@Transaction`이 적용된다.
3. Domain 내 메소드에서는 Entity에 대한 CRUD를 처리한다.

