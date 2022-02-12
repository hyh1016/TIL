# 정렬 알고리즘(Sorting Algorithm)

- 어떤 정렬을 쓰냐에 따라 프로그램의 효율성이 좌지우지될 수 있다.
- 정렬은 면접 단골 질문이기도 하다.
- **선택 정렬, 삽입 정렬, 퀵 정렬, 계수 정렬, 병합 정렬, 힙 정렬** 정도까지는 알고 있으면 좋다.

---

## 선택 정렬(Selection Sort)

> 순회하며 제일 작은 데이터를 맨 앞으로 옮김으로써 왼쪽부터 정렬을 완성해가는 방식
> 

### 코드

```python
def selection_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]

array = [7, 3, 1, 5, 9]
selection_sort(array)
print(array)  # [1, 3, 5, 7, 9]
```

### 시간 복잡도

다음과 같은 이유로 `O(N^2)`이다.

- (N-1) + (N-2) + ... + 2 = N(N+1)/2 라서
- 반복문이 두 번 중첩되었으므로

따라서 알고리즘 문제 풀이에 사용하기에는 조금 느리다.

---

## 삽입 정렬(Insertion Sort)

> 왼쪽의 데이터를 하나씩 확인하며 왼쪽으로 움직이다가(swap) 자신보다 작은 데이터 앞에서 멈춤으로써 왼쪽부터 정렬을 완성해가는 방식
> 

삽입 정렬은 `내 왼쪽 애들은 모두 정렬된 상태`라는 전제로 동작한다.

### 코드

```python
def insertion_sort(array):
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j] >= array[j - 1]:
                break
            array[j], array[j - 1] = array[j - 1], array[j]

array = [7, 3, 1, 5, 9]
insertion_sort(array)
print(array)  # [1, 3, 5, 7, 9]
```

### 시간복잡도

선택 정렬과 마찬가지로 `O(N^2)`이다.

그러나 최선의 시간복잡도는 `O(N)`이기 때문에 `거의 정렬된 상태의 자료에서 효율적`이다.

---

## 퀵 정렬(Quick Sort)

> 기준 데이터(피벗)를 설정하고 기준 데이터를 기점으로 왼쪽에는 보다 작은 데이터가, 오른쪽에는 보다 큰 데이터가 오게 하는 방식
> 

### 코드

1. 첫 번째 원소를 피벗으로 잡고 왼쪽에서부터 피벗보다 큰 데이터를, 오른쪽에서부터 피벗보다 작은 데이터를 찾는다.
2. 찾은 후 두 데이터가 엇갈리지 않았다면 swap, 엇갈렸다면 작은 데이터와 피벗의 위치를 바꾼다. 
3. 2번까지 수행하고나면 피벗을 기준으로 왼쪽은 보다 작은 데이터가, 오른쪽은 보다 큰 데이터가 존재하게 된다.

```python
def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    left, right = start + 1, end
    while True:
        while left <= end:
            if array[pivot] < array[left]:
                break
            left += 1
        while right > start:
            if array[pivot] >= array[right]:
                break
            right -= 1
        if left >= right:
            break
        array[left], array[right] = array[right], array[left]
		array[pivot], array[right] = array[right], array[pivot]
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

array = [6, 4, 1, 3, 5, 0]
quick_sort(array, 0, len(array) - 1)
print(array)
```

### 파이썬에 특화된 코드

어쨌든 피벗을 정하고 피벗보다 왼쪽에는 작은 데이터, 오른쪽에는 큰 데이터가 오게 만든 뒤 재귀로 각 배열에 대해 동일한 알고리즘을 적용한다면 퀵소트는 돌아간다.

아래는 이러한 점에서 착안한 파이썬에 특화된 코드이다.

위와 달리 **배열 자체를 정렬하는 것이 아니라 정렬한 배열을 반환한다.**

```python
def quick_sort(array):
		if len(array) <= 1: # 두 개부터 재귀에 들어가므로
				return array
		pivot = array[0]
		tail = array[1:] # 이 문장이 반드시 유효해지는 것 (1개 이하면 에러 발생)
		left = [i for i in tail if i < pivot]
		right = [i for i in tail if i >= pivot]
		return quick_sort(left) + [pivot] + quick_sort(right)
```

### 시간 복잡도

`최선의 경우`

- 항상 피벗이 정중앙에 위치하게 될 때
- 즉, 항상 정중앙을 기준으로 배열을 쪼개 재귀에 들어가는 경우
- 이 때 시간 복잡도는 `O(NlogN)`이다.

`최악의 경우`

- 배열이 한 쪽으로 치우쳐 쪼개져 데이터의 개수만큼 쪼개지는 경우
- 이 때 시간 복잡도는 `O(N^2)`이다.

따라서 위와 같이 피벗을 선정하는 경우 퀵 정렬은 오히려 정렬된 데이터에서 느리고, 무작위 데이터에서 빨라진다.

이를 보완하기 위해 별도의 피벗 선정 알고리즘을 이용하기도 한다.

---

## 계수 정렬

> 모든 데이터를 담을 수 있는 리스트를 선언해 등장 횟수를 세는 방식
> 

지금까지 본 선택, 삽입, 퀵 정렬은 `비교 기반의 정렬 알고리즘`이다.

계수 정렬은 데이터를 카운트할 뿐이기 때문에 비교 기반의 정렬 알고리즘이 아니다.

### 코드

```python
def counting_sort(array):
    new_array = []
    count = [0] * (max(array) + 1)
    for i in array:
        count[i] += 1
    for i in range(len(count)):
        for j in range(count[i]):
            new_array.append(i)
    return new_array
```

### 시간 복잡도

데이터의 개수 N과 최대값의 크기 K에 대하여 `O(N + K)`

### 공간 복잡도

0과 999,999 단 두 개의 데이터에 대한 정렬을 수행한다면 매우 비효율적인 알고리즘이 될 것이다.

따라서 `데이터의 크기가 작고 중복된 데이터가 많은 경우` 효율적인 알고리즘이다.

---

## 자주 등장하는 유형

### 리스트 자료가 주어지며 각 값이 `우선도`의 의미를 갖는 경우

정렬을 통해 우선순위를 기점으로 데이터를 처리해야 하는 문제에 해당한다.

### 리스트 내부의 리스트 or 튜플 (여러 개의 정렬 조건)

**시간 복잡도를 잘 고려**해야 한다. 내가 반복문 중첩을 해도 될지 아닐지 등을 잘 생각할 것

- 정렬 조건 간의 우선순위가 있는 경우 **역순으로 적용**한다.
    - 이유: 먼저 적용하는 조건에서 같은 우선도를 갖는 애들에 다음 조건을 적용하는 것이므로
    먼저 적용할 조건을 나중에 적용하면 앞에서 정렬된 (같은 우선도를 가질) 애들의 순서에는 영향을 미치지 않는다.
