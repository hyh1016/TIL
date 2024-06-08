# Statement vs Prepared Statement

> 예시 코드와 여기서 지칭하는 클래스는 JDBC API 기반

## Statement

### 정의

```java
String query = "INSERT INTO member(id, name) VALUES(%s, %s)".formatted(id, name);
```

- String 기반의 SQL 쿼리

### 장점

- 단순함

### 단점

- 단순 문자열이므로 가독성이 떨어짐
- 데이터베이스 엔진이 쿼리 최적화나 캐싱 등을 수행하지 않음
- **SQL Injection 공격에 취약**

### SQL Injection 공격에 취약한 이유?

- 단순 문자열이고, 입력을 검증하지 않기 때문
- 위의 id, name으로 사용자가 정상적인 값이 아닌 공격을 위한 쿼리문을 넣어도 DB에서 검증하지 않는다는 것

### 언제 사용?

- 반복적으로 실행되는 경우 성능 면에서 좋지 않고, 사용자의 입력을 받는 경우 공격에 취약하다는 단점이 있었음
- 따라서, 위의 두 가지가 아닌 **내부적으로 실행되는 DDL 문(CREATE, ALTER, DROP)**에 알맞음

## Prepared Statement

### 정의

```java
String query = "INSERT INTO member(id, name) VALUES(?, ?)";

PreparedStatement preparedStatement = connection.preparedStatement(query);
preparedStatement.setInt(1, id);
preparedStatement.setString(2, name);
preparedStatement.executeUpdate();
```

- 미리 준비된 쿼리에 입력값을 채워넣는 방식으로 동작하며, 입력값에 대한 검증을 수행
- Java 기준 Statement를 상속하며, 내부적으로 타입 검증을 수행

### 장점

- 데이터베이스 엔진이 쿼리에 대한 캐싱을 수행
    - 쿼리에 대한 컴파일/실행 계획이 데이터베이스에 저장됨
- JVM과 DB 간 통신 속도도 빠름
    - 전체 쿼리를 모두 전송하는 대신 바인딩된 파라미터 값만 전송하는 방식으로 오버헤드 감소
    - 예를 들어 Statement가 쿼리를 아래와 같은 방식으로 전달한다면,
        
        ```java
        SELECT * FROM users WHERE id = 1;
        ```
        
    - Prepared Statement는 쿼리를 아래와 같은 방식으로 전달하는 것
        
        ```java
        Query ID: 0x03
        Parameters: [int: 1]
        ```
        
- batch 작업을 위한 명령을 제공
- BLOB/CLOB 데이터를 간편하게 다룰 수 있게 함
- 메타데이터를 통해 수행 결과에 대한 정보를 볼 수 있게 함

### 언제 사용?

- 바인딩 파라미터가 사용자 등 외부로부터 오는 값이라 검증이 필요한 경우
- 동일 쿼리가 여러 번 실행될 예정인 경우
- 일회성 DDL 쿼리들을 제외하고는 일반적으로 사용되는 대부분의 쿼리가 이에 적합함
