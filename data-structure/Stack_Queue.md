# Stack, Queue (스택, 큐)

## Stack

후입선출(LIFO)로 동작하는 자료구조. 나중에 들어온 게 먼저 나간다.

파이썬에서는 다음과 같이 리스트 자료형을 통해 사용할 수 있다.

## Queue

선입선출(FIFO) 구조라고도 한다. 먼저 들어온 게 먼저 나간다.

## 파이썬에서의 스택, 큐

### 스택

파이썬에서 스택은 다음과 같이 리스트 자료형을 통해 사용할 수 있다.

```python
stack = []
stack.append(0) # push [0]
stack.append(1) # push [0, 1]
stack.pop() # pop [0] 반환값은 1
```

### 큐 (덱)

파이썬에서는 collections 모듈의 deque(덱)을 이용해 큐처럼 사용한다.

**덱**이란, 스택과 큐를 합친 자료구조로 양 방향에서 삽입/삭제가 가능하다.

```python
from collections import deque

queue = deque()
queue.append(0) # push [0]
queue.append(1) # push [0, 1]
queue.popleft() # pop [1] 반환값은 0
```
