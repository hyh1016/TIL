# Gradle daemon

## Gradle Daemon 이란?

- 백그라운드 프로세스로 실행되는 프로그램
- gradle은 초기화 시점에 JVM 실행, 라이브러리 사용 등 여러 가지 일을 수행하며, 이 때문에 최초 시작 수행 속도는 느릴 수 있음
- Gradle Daemon을 통해 위 과정을 백그라운드에서 동작시키고 유효하도록 유지함으로써 빌드 시간을 단축할 수 있음
    - 유지를 한다고? 캐싱을 통해 환경을 저장
    - 파일시스템을 추적하여 재빌드할 필요가 없는 것들은 재사용하는 방식 등을 이용하게 됨
- Gradle 3.0 이전에는 daemon을 사용하고 싶으면 직접 설정해줘야 했지만, 3.0부터는 자동으로 daemon을 사용하도록 설정됨
- Gradle JVM Client는 daemon에 빌드를 위한 정보를 제공
    - 커맨드라인 인자, 환경변수
    - 프로젝트의 파일구조
- Gradle JVM Client와 Gradle daemon 간 통신은 소켓 연결에 의해 이루어짐
- Daemon은 자바 프로그램의 실행할 때 아래와 같은 최소/최대 힙 크기를 사용
    - 최소 힙 크기: JVM의 기본 최소 힙 크기
    - 최대 힙 크기: 512MB (대부분의 빌드 환경에 적합한 크기)
- 만약 더 큰 프로젝트여서 512MB의 힙 사이즈 이상이 필요하게 되면 직접 이를 조정해줘야 함

## 출처

[Gradle Daemon](https://docs.gradle.org/current/userguide/gradle_daemon.html)
