# 파이썬의 재귀 제한(Recursion Limit)

## 파이썬의 재귀 함수 호출 횟수 제한

함수는 실행되면 메모리 공간 중 스택(stack) 영역에 저장되고, 실행이 종료되면 stack에서 제거된다.

그러나 재귀 함수는 일반적인 함수들과 달리 `함수가 종료되지 않고 계속해서 중첩`되기 때문에 stack에서 제거되지 않는다. 즉, stack에 함수가 계속해서 쌓여 간다는 뜻이다.

따라서 이렇게 함수가 쌓이다가 허용된 stack의 크기를 초과하게 되면, `stack overflow`가 발생한다. python에서는 이를 방지하기 위해 재귀 함수의 중첩 호출 횟수에 제한을 두고 있다.

## Control Recursion Limit

python의 재귀 제한은 system 관련 행위를 수행하는 모듈인 sys를 호출하여 제어할 수 있다.

```python
import sys
sys.setrecursionlimit(재귀 제한)
```

default value는 1000이다.

```python
print(sys.getrecursionlimit()) # 1000
```

## 실제 재귀 제한만큼 재귀에 진입할 수 있는가?

아래 코드와 같이 재귀 제한을 10으로 설정하고 10번의 재귀를 수행해보았다.

```python
import sys
sys.setrecursionlimit(10)

def recursion(n):
    if n == 0:
        return
    print(f"{n}번째 재귀")
    recursion(n-1)

recursion(10)
```

결과는 아래와 같았다.

```python
10번째 재귀
9번째 재귀
8번째 재귀
7번째 재귀
6번째 재귀
5번째 재귀
RecursionError: maximum recursion depth exceeded while calling a Python object
```

파이썬이 코드를 수행하기 위해 내부적으로 5번의 함수 스택을 쌓기 때문에 다음과 같이 동작하는 것 같다.

recursion limit을 15로 높여준 뒤 다시 코드를 실행하자 모든 재귀가 성공적으로 호출되었다.

### 넓이 X, 깊이 O

그렇다면, 다음과 같이 한 재귀 함수가 자기 자신을 여러 번 호출한다면 어떻게 될까?

```python
import sys
sys.setrecursionlimit(15)

def recursion(n):
    if n == 0:
        return
    print(f"{n}번째 재귀")
    recursion(n-1)
    recursion(n-1)

recursion(10)
```

한 번의 호출에 대해 stack도 두 배로 차지할 것이므로, 오류가 발생할 것이라고 생각했다.

그러나 성공적으로 수행되었다.

따라서 setrecursionlimit 함수는 `넓이에 상관 없이 중첩되는 깊이에만 관여`함을 알 수 있었다.
