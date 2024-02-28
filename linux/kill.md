# kill

## Kill

- 프로세스에게 `종료 신호`를 전송하는 명령
- PID(프로세스 아이디)를 기반으로 동작

### SIGTERM (default)

```bash
kill {pid}
kill -15 {pid}
```

- 프로세스에 정상 종료(하던 일을 모두 마무리한 뒤 종료) 시그널을 전송
- 프로세스에 해당 신호를 받았을 때 수행할 동작(핸들러)을 등록할 수 있음
    - 파일 쓰기(저장) 등

### SIGKILL

```bash
kill -9 {pid}
```

- 강제 종료(즉시 종료)
- 신호를 받는 즉시 종료되기 때문에 별도 핸들러를 등록할 수 없음

## PID 찾기

### 이름으로 찾기

```bash
ps -ef | grep {name}
```

### 포트 번호로 찾기

```bash
lsof -i :{port number}
```
