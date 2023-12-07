# QueryDSL Setup

## QueryDSL

### DSL (도메인 특화 언어)

- 특정 도메인에서 발생하는 문제를 효과적으로 해결하기 위해 설계된 언어

### QueryDSL

- SQL Query에 특화된 언어
- SQL 형식의 쿼리는 단순 문자열에 불과함
    - 자바 코드 등에 섞이게 되면 type mismatch와 같은 상황을 컴파일 타임에 인지할 수 없게 만들어 런타임 에러를 발생시킴
- JPA 기반 모듈을 제공

## Gradle Setup

> spring 3.x (jakarta) 기반
> 

### 의존성 추가

```groovy
implementation 'com.querydsl:querydsl-jpa-{version}:jakarta'
```

### annotationProcessor 추가

```groovy
annotationProcessor "com.querydsl:querydsl-apt:${dependencyManagement.importedProperties['querydsl.version']}:jakarta"
annotationProcessor "jakarta.annotation:jakarta.annotation-api"
annotationProcessor "jakarta.persistence:jakarta.persistence-api"
```

- QueryDSL은 엔티티의 어노테이션 정보를 기반으로 QClass 라는 메타데이터 클래스를 생성
    - 쿼리의 타입 안전성을 보장하기 위한 메타데이터

### QClass가 생성될 디렉토리 명시적 지정

```groovy
def generated = 'src/main/generated'

// QClass 생성 경로를 명시적으로 지정
tasks.withType(JavaCompile).configureEach {
	options.getGeneratedSourceOutputDirectory().set(file(generated))
}

// gradle clean 호출 시 QClass 디렉토리 제거
clean {
	delete file(generated)
}
```

- 빌드/실행에 어떤 도구를 사용하냐에 따라 QClass가 저장되는 위치가 달라짐
    - Gradle을 사용하는 경우 build/generated
    - IntelliJ를 사용하는 경우 src/main/generated

### .gitignore 등록

```groovy
/src/main/generated/
```

- QClass 생성 경로는 git에 올리지 않도록 지정
- 버전에 따라 생김새가 자주 바뀌고, 빌드/실행 시점에 생성되는 만큼 올바르지 않은 상태의 파일이 올라갈 위험성도 무시할 수 없음
    - 메타데이터이기 때문에 구조가 복잡해 이를 개발자가 일일이 확인하기 어려움

## QueryDSL 사용

### jpa query factory bean 등록

```java
@Configuration
public class QueryDslConfig {
	@PersistenceContext
	private EntityManager entityManager;

	@Bean
	public JpaQueryFactory jpaQueryFactory() {
		return new JpaQueryFactory(entityManager);
	}
}
```

### Custom Repository 선언

```java
@Repository
@RequiredArgsConstructor
public class CustomEntityRepository {
	private final JpaQueryFactory jpaQueryFactory;
}
```

## Reference

[[10분 테코톡] 바론, 블랙캣의 Querydsl with JPA](https://youtu.be/Dz-46mPfkGo)
