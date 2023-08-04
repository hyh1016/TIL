# 🐘 Gradle

## Gradle

- 범용 빌드 도구
- 멀티 모듈 빌드 가능
- Groovy/Kotlin 기반의 DSL(도메인 특화 언어)를 사용해 구성

## Gradle의 생명 주기

```java
Initialization(초기화) -> Configuration(구성) -> Execution(실행)
```

### Initialization(초기화)

- `settings.gradle` 파일을 참조해 빌드 과정에 포함시킬 프로젝트를 결정
- 포함할 프로젝트 내에 존재하는 각 `build.gradle` 파일에 대한 인스턴스를 생성

### Configuration(구성)

- `settings.gradle`을 통해 지정된 범위 내의 `build.gradle` 파일 내에 정의된 태스크들을 실행
- task 객체를 생성하고, task 그래프를 확립
    - 사용자 정의 task이고 doFirst()가 존재한다면 이 단계에서 실행됨

### Execution(실행)

- graph에서 명령을 통해 실행하고자 했던 task 기반으로 해당되는 task들을 순차적으로 실행