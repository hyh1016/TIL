# Heap

## 정의

* `우선순위 큐`를 위한 자료구조.
* 우선순위 큐는 스케줄링(ex: CPU 스케줄링)에 주로 쓰인다.
* 가장 큰 데이터부터 나오면 Max Heap(최대 힙), 가장 작은 데이터부터 나오면 Min Heap(최소 힙)이라고 한다.

## 구현(Python) - Max Heap

다음의 변수들이 존재한다고 가정한다.

```python
HEAP_SIZE = 0 # 힙에 존재하는 요소의 개수를 저장할 변수
heap = [None] # 힙 (0번 인덱스 미사용)
```

### 삽입

```python
# 힙에 삽입 시. 반복 인덱스 i는 방금 들어간 데이터의 인덱스부터 루트의 자식까지
# 1. 마지막 노드에 새 데이터를 삽입
# 2. (최대 힙 기준) 부모와 비교해서 부모보다 크면 부모와 swap
# 3. 부모가 더 큰 값일 때까지 2번을 반복
def push(data):
    global HEAP_SIZE
    HEAP_SIZE += 1
    heap.append(data)
    i = HEAP_SIZE
    while i > 1:
        parent = i//2
        if heap[i] <= heap[parent]:
            break
        heap[i], heap[parent] = heap[parent], heap[i]
        i = parent
```

### 삭제

```python
# 힙에서 삭제 시. 정확히는 우선순위 큐에서의 pop. 가장 큰 요소를 꺼내는 것
# 1. 루트 노드 데이터를 꺼내고 루트 노드 위치에 마지막 노드 값을 넣는다.
# 2. 마지막 노드를 삭제 처리(힙 크기를 1 줄인다).
# 3. 힙을 재정렬한다.
def pop():
    global HEAP_SIZE
    data = heap[1]
    heap[1] = heap[HEAP_SIZE]
    heap.pop()
    HEAP_SIZE -= 1
    sort()
    return data

# 재정렬: 루트부터 시작해서 마지막 노드까지 비교하며 swap
# 내가 가장 크면 내비두고, 나보다 큰 자식이 있다면 더 큰 자식이랑 swap한다.
# 두 자식이 모두 나보다 크다면 둘 중 더 큰 자식을 위로 올려야 max heap이 유지된다.
def sort():
    global HEAP_SIZE
    i = 1
    while i*2 <= HEAP_SIZE:
        max_index = i
        if heap[max_index] < heap[i*2]:
            max_index = i*2
        if i*2 < HEAP_SIZE and heap[max_index] < heap[i*2+1]:
            max_index = i*2+1
        if max_index == i:
            break
        heap[max_index], heap[i] = heap[i], heap[max_index]
        i = max_index
```

## 시간복잡도

* 삽입은 맨 밑에서 맨 위까지 올라오는 과정이므로 O(logN)이다.
* 삭제는 삭제 자체는 O(1)이지만 재정렬 과정이 필요하다. 재정렬은 루트가 최대 마지막 노드까지 검사하는 과정이므로 맨 위에서 맨 밑까지 올라오는 과정이다. 따라서, O(logN)이다.
