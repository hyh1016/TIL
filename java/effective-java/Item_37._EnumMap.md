# Item 37. ordinal 인덱싱 대신 EnumMap을 사용하라

## ordinal 값을 인덱스로 하는 Enum 배열 생성

```java
class Student {
	enum Grade { A, B, C, D, E, F }

	final String studentId;
	final String name;
	final Grade grade;
}
```

- 위와 같이 학점이라는 열거형 멤버 변수를 갖는 학생 클래스에 대하여, 특정 학점을 받은 학생 데이터를 조회할 일이 생겼다고 가정
    - 각 열거 타입 상수에 대한 Student 객체의 Collection을 만들어야 할 것임
- 이를 ordinal index를 통해 해결하는 코드는 다음과 같이 생겼을 것
    
    ```java
    // 열거 상수의 수만큼 배열 생성하고 각 요소에 HashSet 할당
    Set<Student>[] studentGradeSet =
            (Set<Student>[]) new Set[Student.Grade.values().length];
    for (int i=0; i<studentGradeSet.length; i++) {
        studentGradeSet[i] = new HashSet<>();
    }
    
    // 학생 리스트를 순회하면서 학생의 학점에 해당하는 배열에 해당 학생을 저장
    for (Student s : studentList) {
        studentGradeSet[s.getGrade().ordinal()].add(s);
    }
    ```
    

### ordinal index array의 문제

- 비검사 형변환(Unchecked cast)을 수행하여 컴파일 워닝이 발생
- 잘못된 정수값을 사용해 이 배열에 접근하려 했다가 `ArrayIndexOutOfBounds` 예외를 만날 수 있음
- 목적은 `하나의 열거 타입 상수를 특정 값과 매핑하는 것`이므로, 열거 타입 상수 자체를 key로 갖는 Map으로 대체 가능
    - java의 util 라이브러리는 이를 위한 자료형인 `EnumMap`을 지원함

### EnumMap을 이용한 구현

```java
Map<Student.Grade, Student> studentByGrade = new EnumMap<>(Student.Grade.class);
for (Student s : studentList) {
    studentByGrade.put(s.getGrade(), s);
}
```

- `EnumMap`은 내부적으로 배열을 사용하기 때문에 ordinal 배열과 같은 성능을 누릴 수 있으나 구현을 내부로 숨김으로써 컴파일 타임에 발생하는 워닝은 숨길 수 있음
- 클라이언트는 put, get을 통해 데이터에 접근하니 배열 인덱스 관련 오류가 날 일도 없음
- **제네릭 타입 정보는 런타임에 소거되기 때문에, EnumMap은 런타임에 Key 값에 대한 타입 정보를 제공받기 위해 생성자로 해당 타입의 클래스 객체를 전달받음**
