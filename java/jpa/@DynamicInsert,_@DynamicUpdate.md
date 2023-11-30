# @DynamicInsert, @DynamicUpdate

## JPA의 데이터 삽입

- JPA는 기본적으로 엔티티를 생성 또는 수정할 때 `모든 column을 업데이트하는 동일한 쿼리를 수행`
- 이는 Hibernate에서 제공하는 성능 최적화 전략
    - 엔티티의 어떤 속성이 변경되었는지 확인하고 이에 따른 쿼리를 생성하는 대신 미리 단일 INSERT, UPDATE 쿼리를 준비해두고 재사용하는 편이 더 효율적이기 때문

### 기본 동작

- 아래와 같은 엔티티가 존재한다고 가정
    
    ```java
    @Entity
    public class MyEntity {
    
    	@Id
      @GeneratedValue(strategy = GenerationType.IDENTITY)
      private Long id;
    
    	@Column
    	private String name;
    
    	@Column
    	private String description;
    
    	@Column
    	private LocalDate createdAt;
    
    }
    ```
    
- 아래와 같이 엔티티의 생성 과정에서 일부 데이터만 설정
    
    ```java
    MyEntity entity = new MyEntity();
    entity.setName("name");
    ```
    
- 수행되는 쿼리를 로그로 출력해 확인해보면 아래와 같음
    
    ```java
    insert into my_entity (name, description, createdAt) values (?, ?, ?)
    ```
    
    - 즉, 모든 컬럼을 업데이트하고 있음을 알 수 있음
    - 위에서 명시적으로 setter를 통해 값을 초기화하지 않은 필드값은 모두 null과 같은 기본값으로 초기화되어 데이터베이스에 저장됨

### 기본 동작의 문제점

- 기본 동작은 insert/update 시점에 null 값을 갖는 필드들은 null로 초기화 또는 수정함
- 경우에 따라 원하지 않는 컬럼이 null로 초기화/수정되는 일이 발생할 수 있음
- 위와 같이 전체 데이터를 생성/수정하되 세팅하지 않을 컬럼이 null로 초기화되는 것을 방지하고 싶다면 `@DynamicInsert`, `@DynamicUpdate` 어노테이션을 이용할 수 있음

## @DynamicInsert, @DynamicUpdate

- insert/update 쿼리를 실행할 때, 모든 컬럼을 insert/update하는 쿼리를 재사용하지 않고 세팅된 값만 대상 컬럼에 포함하는 쿼리를 생성해 실행

### 언제 사용?

- 데이터에 엔티티 생성/수정이 아닌 `다른 방식으로 값을 주입하고자 할 때` 해당 어노테이션을 생략하면 주입하려는 값 대신 엔티티에 세팅된 null이 덮어씌워져 값이 소실될 수 있음
- 이를 방지하고자 사용하며, 주로 아래와 같은 기능들과 함께 사용
    1. JPA의 EntityListener
        - 엔티티의 변화를 감지해 특정 시점 이후 데이터를 조작하는 리스너
        - 데이터 조작이 null 필드의 반영보다 먼저 일어나면 값이 덮어씌워지게 됨
            - 위의 createdAt과 같은 날짜 데이터를 초기화하는 경우에서 이런 실수가 빈번하게 발생
    2. @ColumnDefault
        - 특정 필드에 default 값을 설정하는 어노테이션
        - 마찬가지로 쿼리에 의한 null 값 반영에 의해 값이 덮어씌워지게 됨

### 주의할 점

- 앞서 말했듯 Hibernate가 모든 컬럼을 업데이트하는 것은 동일 쿼리를 재사용함으로서 성능 최적화를 하기 위함
- @DynamicInsert, @DynamicUpdate를 사용하게 되면 해당 엔티티 클래스의 insert/update 작업이 기본 전략을 사용하는 것보다 느려짐
