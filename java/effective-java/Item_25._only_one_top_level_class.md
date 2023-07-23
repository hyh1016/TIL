# Top Level Class는 한 파일 당 하나만 선언하라

## 한 파일에 여러 Top Level Class를 선언하는 것의 위험성

- 파일의 컴파일 순서에 따라 다른 결과가 나올 수 있음

### 예시

- A, B 클래스를 선언한 파일 A.java와 B.java
- A, B 클래스를 사용한 파일 C.java
- C→A 순으로 컴파일하면 A.java 내 A, B 클래스를 사용
- B→C 순으로 컴파일하면 B.java 내 A, B 클래스를 사용

## 예방법

### 가장 좋은 것은 별도 파일로 분리하는 것

- 한 java 파일 내 하나의 클래스만 존재할 수 있도록 하는 것이 최고
- 두 클래스가 깊은 연관을 가져 하나의 파일 내에 위치시키고 싶다면, `정적 멤버 클래스`로 선언하는 것도 좋음