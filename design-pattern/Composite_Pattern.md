# Composite Pattern

## Composite Pattern (컴포지트 패턴)

![Composite-Pattern](imgs/composite-pattern-\(0\).png)

Part-Whole(부분-전체) 계층 구조를 표현하기 위해 객체들을 트리 구조로 구성하는 패턴

Client가 개개의 객체(부분 객체)와 그룹 객체(전체 객체)를 동일하게 취급할 수 있도록 한다.

### 구성

* `Component` - 부분 객체와 전체 객체의 공통 인터페이스로 Child 객체에 접근하고 관리하기 위함
* `Leaf` - 부분 클래스로, Composite 객체의 부품으로 설정되며 Child 객체를 가지지 않음
* `Composite` - 전체 클래스로, 복수 개의 Component를 가질 수 있으며 본인 또한 Component의 파생 클래스이다. 따라서, Child로 복수 개의 Leaf와 복수 개의 Composite를 가질 수 있다.
* `Client` - 모든 객체들을 부분-전체 여부와 관계 없이 Component 객체를 통해 이용하는 객체

### 예시

*   리눅스의 디렉토리-파일 구조

    ![Composite-Pattern-Example](imgs/composite-pattern-\(1\).png)

    리눅스는 디렉토리, 일반 파일(텍스트, 이미지, 실행 파일 등)들을 모두 `파일`로 취급한다. 따라서 디렉토리는 본인도 파일임과 동시에 파일을 포함할 수 있다.

    여기서 이들을 모두 통칭하는 File이 Component, File에 포함되며 File을 가질 수 있는 Directory가 Composite, 일반적인 File에 해당하는 CommonFile이 Leaf가 될 수 있다.
