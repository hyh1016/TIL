# Block vs Non-block, Sync vs Async

> 이 글에서는 두 함수(또는 프로세스)가 존재한다고 치고, 둘을 A와 B라고 칭하며,
> A가 B를 호출하는 경우의 동작 과정을 Block/Non-block, Sync/Async로 나누어 정리 

## Block vs Non-Block (블락과 논블락)

함수가 종료될 때까지 `제어권을 누가 갖느냐`에 따라 결정됨

말 그대로 호출되는 함수가 `제어권을 빼앗아` 호출자가 다른 일을 하지 못하게 하면 Block

### Block

- 호출된 함수가 종료될 때까지 호출한 함수는 기다림(wait)
- ex) A가 B를 호출하면 B가 끝날 때까지 A는 자신이 처리해야 할 이후의 일들을 처리하지 않고 대기

### Non-block

- 호출된 함수는 제어권을 바로 호출자에게 넘겨주고 자신의 일을 수행
- 호출한 함수도 Non-block 함수를 호출만 하고 자신의 일을 이어서 수행
- Non-block 방식을 이용하면 어쨌든 제어권이 호출자에게 넘어가므로 A와 B가 병렬적으로 수행됨
- A는 B를 호출한 뒤 자신의 일을 이어서 수행

## Sync vs Async (동기와 비동기)

동기와 비동기는 `순서가 반드시 지켜져야 하는가`에 따라 결정됨

### Synchronous (동기)

- 호출한 함수의 결과를 처리한 후 다음 동작으로 넘어가야 하는 것이 동기
- A는B가 완료된 후 결과를 반환하면 이후의 일을 수행

### Asynchronous (비동기)

- 호출당한 함수가 결과를 처리하고 처리했다고만 알림 (callback)
- 호출한 함수는 callback이 올 때까지 free한 상태가 됨. callback이 왔을 때 후속 처리가 필요하면 처리
    - 그러나 이 경우 호출된 함수가 Block이면 A는 free함에도 아무 일도 못 하는 상태가 되는데, 이것이 가장 안티 패턴 (`Block & Asynchronous`)

## 4가지 경우의 수에 따른 동작

### block & Synchronous

- A가 B를 호출하며 제어권을 넘겨주고, A는 B가 끝날 때까지 대기하며 B의 완료 여부를 체크
- B가 완료되면 제어권을 넘겨받고, 결과를 처리
- Sync를 요구하는 작업은 block으로 처리하는 것이 자연스러움 (Good)

### block & Asynchronous

- A는 B의 동작과 상관 없이 이후의 일들을 처리할 수 있으나, B를 호출하며 제어권을 넘겨주었기 때문에 이후의 일들을 처리하지 못하고 대기
- A가 자신의 일을 처리할 수 있는데도 못 하고 있음 (Bad)
    - ⭐ B 동작을 별도 스레드에서 처리하게 하는 방식 등을 통해 A가 호출 후 바로 제어권을 얻어올 수 있게 하는 Non-block으로 처리하면 성능 개선 가능!

### Non-block & Synchronous

- A는 B가 완료된 후 나머지를 처리하기 위해 B의 완료 여부를 계속 체크해야 하기 때문에, B가 A에게 제어권을 넘겨준다 해도 A는 B의 응답을 받기 전에 처리할 수 없는 것들을 처리할 수 없음
- 순서가 보장되어야 하기 때문에 Block이든 Non-block이든 어쩔 수 없음 (Bad)
    - 최대한 이 순서와 관계 없는 것들을 별도 작업으로 뺌으로써 성능 개선 가능할 듯

### Non-block & Asynchronous

- A는 B를 호출한 후 자기 할 일 처리
- 병렬 처리가 일어나는 것이므로 성능 면에서는 최고 (Good)

## 출처

[https://musma.github.io/2019/04/17/blocking-and-synchronous.html](https://musma.github.io/2019/04/17/blocking-and-synchronous.html)