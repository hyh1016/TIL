# Floyd-Warshall Algorithm (플로이드-워셜 알고리즘)

> #### Shortest-Path Algorithm (최단경로 알고리즘)
>
> 1. [다익스트라 알고리즘 (한 지점에서 다른 모든 지점까지의 최단경로)](Dijkstra.md)
> 2. 플로이드-워셜 알고리즘 (모든 지점에서 다른 모든 지점까지의 최단경로)
> 3. 벨만포드 알고리즘 (한 지점에서 음수 가중치를 포함하는 다른 모든 지점까지의 최단경로)

## 정의

모든 노드에서 다른 모든 노드로 가는 최단경로를 구하는 알고리즘

## 동작 흐름

1. 모든 노드에서 모든 노드로 가는 거리를 담을 이차원 배열 shortest를 선언한다.
2. 각 노드에 대하여 자기 자신으로 가는 거리를 0으로 초기화한다.
3. 각 노드에 대하여 연결된 정점으로 가는 거리를 초기화한다.
4. 모든 노드에 대한 `해당 노드를 중간 지점으로 거쳐갈 때와 거쳐가지 않을 때의 거리를 비교`하여 더 짧은 값으로 테이블을 갱신한다.

## 구현

```python
INF = int(1e9)

def floyd_warshall(graph, shortest):
    for i in range(1, len(graph)):
        shortest[i][i] = 0
        for j in graph[i]:
            shortest[i][j[0]] = j[1]
    for k in range(1, len(graph)):
        for i in range(1, len(graph)):
            for j in range(1, len(graph)):
                shortest[i][j] = min(shortest[i][j], shortest[i][k] + shortest[k][j])

node, edge = 6, 11
start = 1
graph = [[] for _ in range(node+1)]
shortest = [[INF]*(node+1) for _ in range(node+1)]

data = [
    (1, 2, 2),  # 1번에서 2번으로 가는 비용이 2
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
for i in data:
    a, b, c = i
    graph[a].append((b, c))
floyd_warshall(graph, shortest)
for i in range(1, node+1):
    for j in range(1, node+1):
        print(format(shortest[i][j], "3") if shortest[i][j] != INF else 'INF', end=" ")
    print()
```

```python
# 결과
  0   2   3   1   2   4 
INF   0   3   2   3   5 
INF   3   0   5   6   5
INF   5   2   0   1   3
INF   4   1   6   0   2
INF INF INF INF INF   0
```

## 시간 복잡도

모든 노드를 중간 지점으로 잡으므로 O(N), 순서를 고려하여 시작 지점이 될 노드와 끝 지점이 될 노드를 정하는 것이 nP2 = O(N^2).

따라서 `O(N^3)`이다.
