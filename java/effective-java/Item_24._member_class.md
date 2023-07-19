# Item 24. 멤버 클래스는 되도록 static으로 만들라

## 중첩 클래스

- Static 멤버 클래스
- (Non-static) 멤버 클래스
- 익명 클래스
- 지역 클래스

## 멤버 클래스

### Static 멤버 클래스

- 바깥 클래스의 private 멤버에 접근할 수 있음
- 바깥 클래스와 연결되지는 않음

### Non-static 멤버 클래스

- 해당 클래스의 인스턴스는 바깥 클래스의 인스턴스가 먼저 생성된 후 생성되어야 함
- 바깥 클래스의 인스턴스와 연결됨
    - 바깥 클래스의 인스턴스의 참조를 가져올 수 있음

### Non-static 멤버 클래스의 단점

- 바깥 인스턴스와의 참조를 저장하기 위한 시간/메모리를 소모 (비효율적)
- GC가 바깥 클래스의 인스턴스의 수거 여부를 결정하기 어렵게 만듦 (메모리 누수 위험성)
- **따라서, 멤버 클래스에서 바깥 인스턴스에 접근해야 하는 게 아니라면 멤버 클래스는 static으로 만드는 것이 좋음**

## 익명 클래스와 지역 클래스

### 익명 클래스

- 선언 지점에서만 인스턴스를 만들 수 있는 클래스
- `람다`의 도입 이전에는 작은 메서드를 갖는 객체, 처리(process) 객체 등을 지원하고자 사용
    - 람다가 도입되면서 이 자리를 람다가 대체함

### 지역 클래스

- 지역변수를 선언하는 위치(메서드 내, block 내 등)에서 사용하는 클래스
- Non-static 멤버 클래스와 유사하나 선언 범위에 더 제약이 없음
- 잘 사용하지 않음

## 익명 클래스와 람다

### 익명 클래스

```java
MyClass class = new MyClass() {
		@Override
		public void add(int n1, int n2) {
				return n1 + n2;
		}
}
```

- 해당 스코프에서만 유효한 새로운 클래스를 만들어 이 클래스의 메서드를 호출

### 람다

```java
MyClass class = (n1, n2) -> n1 + n2;
```

- 클래스를 생성하는 대신, 메서드만을 구현
- 훨씬 가독성이 좋고 간결
- 클래스를 생성할 필요가 없음 (실제 바이트코드에서도 클래스를 생성하는 대신 메서드만 만듦)
- Java 8부터 사용 가능