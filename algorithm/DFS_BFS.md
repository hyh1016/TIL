# DFS와 BFS

## 사전 지식

### 탐색

많은 양의 데이터 중 원하는 데이터를 찾는 과정

### 스택과 큐

[다음 문서](../data-structure/stack-queue.md)를 참조

### 재귀 함수

자기 자신을 호출하는 함수. `수학의 점화식을 코드화한 것`

* 점화식: 특정 함수를 자기보다 더 작은 변수와 함수의 관계로 표현한 것
* 재귀 함수는 `점점 작아지는 자기 자신` + `종료 조건`을 통해 동작한다.

### 그래프

* vertex(정점)과 edge(간선)으로 이루어진 자료구조
* 프로그래밍에서 이를 표현하는 방식으로는 `인접 행렬`과 `인접 리스트`가 있다.

### 인접 행렬

2차원 배열로 그래프의 연결 관계를 표현한 것

```python
INF = 987654321
graph = [
	[0, 7, 5],
	[7, 0, INF],
	[5, INF, 0]
]

# 0과 1의 연결 관계
graph[0][1] ( == graph[1][0])
```

### 인접 리스트

연결 리스트 자료구조로 그래프의 연결 관계 표현

```python
vertex = 3
graph = [[] for i in range(vertex)]

# 0번 노드와의 연결 정보
graph[0].append((1, 7))
graph[0].append((2, 5))

# 1번 노드와의 연결 정보
graph[1].append((0, 7))

# 2번 노드와의 연결 정보
graph[2].append((0, 5))

# 0번과 1번의 노드의 연결 관계 탐색
graph[0].find
```

### 인접 행렬 vs 인접 리스트

* 인접 행렬
  * 장점: 두 노드 간 연결 여부 확인이 쉽고 정보를 얻는 속도가 빠름
  * 단점: 불필요한 메모리 낭비
* 인접 리스트
  * 장점: 메모리를 효율적으로 사용 (자기 자신과의 관계 저장 X, 필요한 노드의 관계만 저장)
  * 단점: 연결 여부 확인을 위해 순회를 해야 한다. (정보 얻는 속도 느림)
* 따라서 노드의 개수에 비해 간선이 확연히 적을 때(sparse graph)에는 인접 리스트, 아닌 경우에는 인접 행렬을 사용하는 것이 좋다.



## ✅ DFS (깊이 우선 탐색, Depth-First Search)

### 정의

더 이상 방문하지 않은 노드가 없을 때까지 인접 노드를 선택하여 탐색하는 방식

인접 노드간에는 정해진 우선 순위가 있지는 않으나 보통 크기가 작은 순서대로 탐색

### 구현

스택과 재귀함수를 이용하여 구현하는 것이 일반적이다.

방문한 노드, 인접한 노드를 스택에 추가하고 인접 노드 중 미방문인 노드가 없을 시 꺼낸다.

나는 `가중치가 있는 경우 인접 행렬`을, `없는 경우 인접 리스트`를 이용한다.

#### 인접 행렬

```python
INF = 987654321

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")
    for i in range(len(graph[0])):
        if graph[v][i] != 0 and graph[v][i] != INF and not visited[i]:
            dfs(graph, i, visited)

graph = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]
visited = [False] * len(graph[0])
start = 1

dfs(graph, start, visited)

```

#### 인접 리스트

```python
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

vertex = 4
graph = [
    [2, 3],
    [2],
    [0, 1],
    [0]
]
start = 1
visited = [False] * vertex

dfs(graph, start, visited)
```

### 시간 복잡도

dfs 함수(곧 반복문)는 정점의 개수만큼 호출되고, 반복문은 graph\[v] == 간선의 개수만큼 순회하므로 인접 행렬의 경우 `O(V + E)`, 인접 그래프의 경우 `O(V^2)`이다.



## ✅ BFS(너비 우선 탐색, Breadth-First Search)

### 정의

인접 노드를 모두 방문한 뒤 그 중 가장 먼저 방문한 인접 노드의 인접 노드를 방문하는 방식

### 구현

큐를 이용하여 구현하는 것이 일반적이다.

큐에서 꺼낸 노드의 인접 노드를 순회하며 미방문된 노드를 큐에 넣는다.

마찬가지로 `가중치가 있는 경우 인접 행렬`을, `없는 경우 인접 리스트`를 이용한다.

#### 인접 행렬

```python
from collections import deque

INF = 987654321

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in range(len(graph[0])):
            if graph[v][i] != 0 and graph[v][i] != INF and not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]
start = 1
visited = [False] * len(graph[0])

bfs(graph, start, visited)

```

#### 인접 리스트

```python
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

vertex = 4
graph = [
    [2, 3],
    [2],
    [0, 1],
    [0]
]
start = 1
visited = [False] * vertex

bfs(graph, start, visited)

```

### 시간 복잡도

마찬가지로 반복문은 노드의 개수만큼, 순회 횟수는 간선의 수만큼이므로 `O(V+E)`또는 `O(V^2`이지만 DFS보다 조금 더 빠르다고 한다.
