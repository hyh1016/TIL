# 🚀 Dijkstra Algorithm (다익스트라 알고리즘)

> ### Shortest-Path Algorithm (최단경로 알고리즘)
> 1. [다익스트라 알고리즘 (한 지점에서 다른 모든 지점까지의 최단경로)](Dijkstra.md)
> 2. 플로이드-워셜 알고리즘 (모든 지점에서 다른 모든 지점까지의 최단경로)
> 3. 벨만포드 알고리즘 (한 지점에서 음수 가중치를 포함하는 다른 모든 지점까지의 최단경로)

## 정의

**특정 노드에서** **다른 모든 노드로 가는 최단경로**를 구하는 알고리즘
음의 간선이 없을 경우에만 동작한다.

## 동작 흐름

1. **출발 노드 설정**
2. **최단 거리 테이블을 초기화**
3. **방문하지 않은 노드 중 최단 거리가 가장 짧은 노드를 선택**
    - 이 때 해당 노드의 최단 거리는 확정된다.
    - 왜냐하면, 다른 노드를 거쳐 해당 노드로 가는 거리를 구해도 `해당 노드까지의 최단 거리가 최소`인 이상 `더 작은 값으로 갱신될 여지가 없기 때문`이다.
4. **해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블 갱신**
    - 매번 현재 처리중인 노드를 기준으로 최단 경로인지 확인하는 `그리디`를 이용
    - 매번 계산된 특정 노드까지의 거리를 이용하여 다른 노드까지의 거리를 구하므로 중복 연산을 방지하는 `다이나믹 프로그래밍`을 이용

---

## 구현1 - 순차 탐색을 이용한 다익스트라

최단 거리 테이블 **shortest**와 방문 여부를 저장하는 리스트 **visited**를 이용한다.

```python
INF = int(1e9)

def get_smallest_node(shortest, visited):
    value = INF
    index = 0
    for i in range(1, node + 1):
        if shortest[i] < value and not visited[i]:
            value = shortest[i]
            index = i
    return index

def dijkstra(graph, start, shortest, visited):

		# 시작 노드에 대해 방문 처리 후 최초 갱신
    visited[start] = True
    shortest[start] = 0
    for j in graph[start]:
        shortest[j[0]] = j[1]

		# 나머지 노드에 대해 최단 거리가 최소인 노드를 구해 방문/갱신 반복
    for i in range(node - 1):
        index = get_smallest_node(shortest, visited)
        visited[index] = True
        for j in graph[index]:
            cost = shortest[index] + j[1]
            shortest[j[0]] = min(shortest[j[0]], cost)

node, edge = 6, 11
start = 1
graph = [[] for _ in range(node + 1)]
shortest = [INF] * (node + 1)
visited = [False] * (node + 1)

data = [
    (1, 2, 2), # 1번에서 2번으로 가는 비용이 2
    (1, 3, 5),
    (1, 4, 1),
    (2, 3, 3),
    (2, 4, 2),
    (3, 2, 3),
    (3, 6, 5),
    (4, 3, 3),
    (4, 5, 1),
    (5, 3, 1),
    (5, 6, 2)
]

# graph는 (도착 노드, 거리)로 구성
for i in data:
    a, b, c = i
    graph[a].append((b, c))

dijkstra(graph, 1, shortest, visited)
for i in range(1, node + 1):
    print(shortest[i], end=" ") # 0 2 3 1 2 4 
```

### 동작 흐름

1. start node에 대해 방문 처리
2. start node 자신의 최단 거리를 0으로 갱신하고 각 노드를 방문해 최단 거리를 갱신한다.
3. 나머지 노드에서 대해 최단 거리 테이블에서 가장 최단거리가 짧은 노드를 선택한다.
(get_smallest_node)
4.  해당 노드에 대해 1, 2번 과정을 반복한다.

### 시간 복잡도

노드를 선택하는 데에 N, 선택한 노드가 나머지 노드의 최단 거리를 구하는 데에 N이므로
시간 복잡도는 `O(N^2)`

컴퓨터는 1초에 1억 번 정도의 연산을 수행할 수 있으므로 노드의 개수가 5,000개 이하인 경우에는
위와 같은 선형 탐색 방식을 이용해도 된다.

그러나 노드의 개수가 10,000개를 넘어간다면 시간 초과가 날 수 있다.
따라서 더 간단하고 효율적인 `우선순위 큐를 이용한 구현`을 이용하는 것이 좋다.

---

## 구현2 - 힙(Heap) 자료구조를 이용한 다익스트라

최소 힙 구조 라이브러리인 heapq를 이용한다.
힙에 들어가는 튜플 (가치, 데이터) 를 **(최단거리, 인덱스)**로 저장한다.

```python
import heapq
INF = int(1e9)

def dijkstra(graph, start, shortest):
    shortest[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if shortest[now] < dist: # 꺼낸 값이 더 크다면 갱신하지 않으므로 버림
            continue
        for i in graph[now]:
            new_cost = dist + i[1]
            if new_cost < shortest[i[0]]:
                shortest[i[0]] = new_cost
                heapq.heappush(q, (new_cost, i[0]))

node, edge = 6, 11
start = 1
graph = [[] for _ in range(node + 1)]
shortest = [INF] * (node + 1)

data = [
    (1, 2, 2), # 1번에서 2번으로 가는 비용이 2
    (1, 3, 5),
    (1, 4, 1),
    (2, 3, 3),
    (2, 4, 2),
    (3, 2, 3),
    (3, 6, 5),
    (4, 3, 3),
    (4, 5, 1),
    (5, 3, 1),
    (5, 6, 2)
]

# graph는 (도착 노드, 거리)로 구성
for i in data:
    a, b, c = i
    graph[a].append((b, c))

dijkstra(graph, 1, shortest)
for i in range(1, node + 1):
    print(shortest[i], end=" ") # 0 2 3 1 2 4 
```

### 동작 흐름

1. start node의 최단거리인 0과 인덱스를 heapq에 저장한다.
2. heapq에서 데이터를 꺼낸다. 꺼내지는 데이터는 이 안의 데이터 중 최단거리가 가장 짧은 데이터이다.
    - 최소 힙 큐이기 때문
    - 최단거리가 최소인 것이 여러 개라면, 인덱스가 작은 순서대로 꺼내질 것이다.
    (튜플의 첫 번째 원소가 같으면 두 번째 원소를 기준으로 정렬되기 때문)
3. 2번에서 꺼낸 데이터의 인덱스의 현재 최단거리가 더 짧다면 이 데이터는 버린다. (힙에 넣지 않는다!)
    - 따라서 visited를 선언할 필요는 없다.
    - 데이터를 버리는 과정에서 방문한 노드를 다시 들르는 경우가 걸러지기 때문
4. 현재 최단거리보다 꺼낸 데이터의 최단거리가 더 짧다면 갱신한 뒤 heapq에 넣는다.

### 시간 복잡도

heapq는 **N개의 우선순위**에 대하여 삽입과 삭제 모두 `O(logN)`의 시간복잡도를 갖는다.

따라서 최악의 경우인 항상 갱신되는 경우(모든 간선이 버림 없이 고려되는 경우)
**간선의 수만큼 데이터를 넣었다 빼므로** `2ElogN`이다.

따라서 시간 복잡도는 `O(ElogN)`이다.

이 알고리즘을 이용하면 200,000만 정도의 노드에 대해서도 1초 이하의 시간으로
최단 거리를 구할 수 있다.
