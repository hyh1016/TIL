# 📝 String, StringBuilder, StringBuffer

## String

- 불변(immutable) 객체이다.
    - 즉, 문자열을 수정할 시 기존의 값이 변경되는 것이 아니라 참조가 변경된다. (기존 메모리는 GC에 의한 제거 대상이 됨)
- 참조형 타입임에도 literal로 선언할 수 있다.
    - 기본 자료형(primitive) 변수를 선언하듯 new 없이 값을 할당할 수 있다는 의미
    - 이 경우 new 문법을 통한 동적 할당과는 다르게 동작한다.

### String의 리터럴 할당과 동적 할당

- 리터럴 할당
    - Heap 영역의 String constant pool 내에 데이터가 생성된다.
    - 이 경우 pool 내에 생성하려는 것과 같은 데이터가 있으면 생성하는 대신 해당 데이터를 참조한다.
    - 코드 상에서는 String을 literal로 할당 시 내부적으로 String.intern()이 호출되는데, 이는 pool 내에 데이터가 존재하는지 탐색하고 있다면 해당 주소값을, 없다면 데이터 생성 후 생성된 데이터의 주소값을 반환한다.
- 동적 할당
    - Heap 내에 데이터가 생성된다.
    - 새로운 메모리 공간을 할당받는 것으로, 동일 데이터가 있어도 새 데이터가 생성된다.

## StringBuilder

- 가변(mutable) 객체이다.
- append를 통해 문자열을 더할 수 있고 이 경우 주소값이 변경되지 않는다.

## StringBuffer

- 가변 객체이고 append를 통해 데이터를 변경하는 것은 Builder와 동일하다.
- StringBuilder와 달리 멀티 스레드 환경에서의 데이터 무결성 보장을 위한 처리가 되어 있다.
- 속도 면에서는 String, StringBuilder보다 느리다.

## 정리

- String은 불변 객체이며, 동일 값을 갖는 경우 동일 주소를 참조한다. 이것을 가능하게 하는 것은 Heap 영역의 String constant pool이다.
- StringBuilder와 StringBuffer는 가변 객체이며, 사용법은 동일하나, StringBuffer는 멀티 스레드 환경을 위한 동기화를 지원한다.
- 따라서 문자열 변동이 잦아 String을 사용하면 Memory Leak이 발생할 것 같을 때에는 StringBuilder를, 그 중에서도 동기화를 요구하는 작업이라면 StringBuffer를 사용하는 것이 좋다.
- 가장 속도가 빠른 것은 String이기 때문에, 문자열 변경이 잦지 않다면 String을 사용하는 것이 좋다.
