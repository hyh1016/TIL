# Reflection을 통한 메서드 호출

## Method

### 메서드 획득

#### public 메서드 획득 (Class.getMethod)

```java
public Method getMethod(String name, Class<?>... parameterTypes)
```

- 첫 번째 인자가 메서드명, 두 번째 인자부터는 메서드의 파라미터 타입

#### 모든 접근 제어 레벨의 메서드 획득 (Class.getDeclaredMethod)

```java
public Method getDeclaredMethod(String name, Class<?>... parameterTypes)
```

- public, protected, package, private 메서드 모두 획득 가능

### 메서드 호출

#### 메서드 호출 (Method.invoke)

```java
public Object invoke(Object obj, Object... args)
```

- 첫 번째 인자 obj 는 메서드를 호출할 인스턴스
- 두 번째 인자부터는 인스턴스의 인자
- **instance 부분을 null로 설정하면 static 메서드로 취급**

### 메서드 접근성 제어

#### 접근 가능 설정 (Method.setAccessible)

```java
public void setAccessible(boolean flag)
```

- 접근 불가능한 메서드를 접근 가능하도록 설정

#### 접근 가능 변경 시도 (Method.trySetAccessible)

```java
public final boolean trySetAccessible()
```

- 접근 불가능한 메서드를 접근 가능하도록 설정하고, 실패하면 예외를 전파

### Reference

- [https://www.baeldung.com/java-method-reflection](https://www.baeldung.com/java-method-reflection)