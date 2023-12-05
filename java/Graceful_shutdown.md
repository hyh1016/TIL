# Graceful Shutdown

## Graceful Shutdown

- 직역하면 `우아한 종료`
- 애플리케이션이 현재 처리 중이던 일을 무시하고 급하게 강제종료하는 대신 처리 중이던 일을 모두 마무리하고 우아하게 정상 종료하는 것
- spring은 기본적으로 graceful shutdown을 사용하지 않으며, 이 경우 `정상 종료 시에도 처리 중이던 일은 모두 중단되고 종료`

### graceful shutdown 활성화

- 다음과 같이 환경 변수를 설정하면 활성화됨
    
    ```yaml
    server:
    	shutdown: graceful
    ```
    
- 활성화하면 `정상 종료 시그널에 대해서는 처리 중이던 일을 모두 마무리하고 종료`
- 추가 요청의 거부 방식은 웹 서버마다 상이
    - Spring과 함께 주로 사용되는 tomcat의 경우 네트워크 계층에서 새 커넥션이 맺어지는 것을 거부

### graceful shutdown timeout

- 모든 일을 처리하고 종료
- 처리 중인 일이 영영 끝나지 않는다면? (데드락)
- 위와 같은 상황을 방지하기 위해 처리 중이던 작업 종료를 기다리는 데에도 `timeout`을 설정해야 함
- 아래와 같은 환경 변수를 추하면 됨
    
    ```yaml
    spring:
      lifecycle:
        timeout-per-shutdown-phase: "20s"
    ```
    

## Reference

- [스프링 공식문서 - graceful shutdown](https://docs.spring.io/spring-boot/docs/current/reference/html/web.html#web.graceful-shutdown)
