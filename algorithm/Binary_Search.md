# Binary Search (이진 탐색)

## 순차 탐색

> 앞에서부터 하나씩 차례대로 탐색하는 방법

```python
array = [3, 1, 7, 5, 9]
for i in range(len(array)):
    if array[i] == 7:
        print(i)
```

리스트를 차례대로 순회하므로 `시간 복잡도는 O(N)`이다.

## 이진 탐색

> 정렬된 리스트에 대하여 찾으려는 데이터와 중간 지점의 데이터를 비교해나가며 탐색하는 방법

순차 탐색과 달리 **정렬이 되어 있어야 사용할 수 있다.**

중간이 정확히 안 나누어질 때는 소수점 이하를 버린다.

`시간 복잡도는 O(logN)`이다.

### 구현 - 반복문 (권장)

```python
def binary_search(array, target, start, end):
    while start <= end:
        middle = (start + end) // 2
        if target > array[middle]:
            start = middle + 1
        elif target < array[middle]:
            end = middle - 1
        else:
            return middle
    return None

array = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
target = int(input())
index = binary_search(array, target, 0, len(array) - 1)
print(index) if index != None else print("원소가 존재하지 않습니다.")
```

### 구현 - 재귀함수

```python
def binary_search(array, target, start, end):
    if start > end:
        return None
    middle = (start + end) // 2
    if target > array[middle]:
        return binary_search(array, target, middle + 1, end)
    elif target < array[middle]:
        return binary_search(array, target, start, middle - 1)
    else:
        return middle

array = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
target = int(input())
index = binary_search(array, target, 0, len(array) - 1)
print(index) if index != None else print("원소가 존재하지 않습니다.")
```

## 이진 탐색을 사용하는 경우

### 찾아야 할 자료가 여러 개인 경우

총 데이터 수가 N개, 찾아야 할 자료가 M개일 때 순차 탐색을 이용하면 `O(M * N)`만큼의 시간이 걸린다. 그러나 이진 탐색을 이용하면 정렬에 `O(NlogN)`, 탐색에 `O(MlogN)`만큼의 시간이 걸리므로 총 `O((M + N)logN)` 만큼의 시간이 걸린다. 따라서 M의 값이 커질수록 이진 탐색을 이용한 탐색이 더 효율적이게 된다.

위의 경우 **값의 범위가 크지 않은 경우에는 계수 정렬을 이용할 수도 있다.**

### 최적화 문제를 결정 문제로 바꾸는 `파라매트릭 서치` 문제

정답이 될 수 있는 수의 범위를 정하고 이 범위 내에서 이진 탐색을 수행한다.

**원리**

1. 자동 정렬이 되어있다는 장점
   * 수의 범위만 정하기 때문.
   * 1부터 100까지 라고 정하면 \[1, 2, 3, ... , 99, 100] 이라는 가상의 배열이 있다고 가정
2. 항상 최적의 값에 가까워진다는 점을 이용

**사용법**

* 최적에 가까운 유효한 값을 얻을 때마다 반환할 결과값을 갱신한다.
  * N이 최적값이고 N보다 큰 값을 허용한다면 N보다 큰 유효값을 만날 때마다 갱신
* 파라매트릭 서치는 타겟값을 찾아도 바로 반환하면 안 된다.
  * 타겟값이 최적값이라는 보장이 없기 때문
