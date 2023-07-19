# 🗂 Normalization (정규화)

## 정규화란

- 데이터베이스의 `유연성`을 높이고 `무결성`을 보장하기 위해 데이터의 `중복`, 잘못된 `종속성`을 제거하는 작업

### 중복을 제거하는 이유

- 하나의 데이터를 저장하는 지점이 여러 개가 되면, 그 중 일부 데이터만 수정되어 `같은 데이터임에도 다른 값을 갖는 문제`가 발생할 수 있음

### 잘못된 종속성을 제거하는 이유

- 데이터 간 연결이 잘못 설정되어 있게 되어, 원하는 데이터를 찾는 데에 어려움을 겪을 수 있음
- 또한 잘못된 종속성이 중복을 야기하기도 함

## 제 1 정규화 (1NF)

- 하나의 컬럼에 복수 개의 데이터를 저장하지 않아야 함
- 복수 개 데이터를 취급하게 되는 컬럼이라면, 이를 별도 레코드로 분리하거나 별도 테이블로 분리하고 릴레이션을 맺도록 구성해야 함
    - 별도 레코드로 분리하는 것은 복수 개의 데이터를 갖는 컬럼 이외의 컬럼이 `중복`되게 되므로 좋은 해결법은 아님

### 제 1 정규화를 하지 않으면 생기는 문제

| 수강과목 | 수강자 |
| --- | --- |
| 수학 | 홍길동 |
| 과학 | 임꺽정, 신사임당 |
| 사회 | 홍길동, 임꺽정 |
- 복수 컬럼의 일부 데이터만을 WHERE 조건으로 이용할 경우 잘못된 삭제/수정이 발생할 수 있음
    - 홍길동의 과목을 사회에서 역사로 변경하면 임꺽정의 과목도 함께 바뀜
    - 임꺽정이 전 과목 수강 취소를 해 임꺽정이 포함된 컬럼을 모두 지우고자 하면 신사임당, 홍길동에 대한 정보도 함께 삭제됨

## 제 2 정규화 (2NF)

- 테이블 내 특정 컬럼은 기본 키 이외의 어떤 항목에도 종속되어서는 안 됨
- 이 경우 이 종속성을 갖는 테이블을 별도 테이블로 분리하여 제 2 정규형을 만족
    - PK가 아닌 X에 대하여 X → Y 가 존재하면, X가 PK이고 Y를 컬럼으로 갖는 새 테이블을 생성한 뒤 기존 테이블에서는 Y를 제거해야 하는 것
- 이 과정을 `부분적 함수 종속`을 제거한다고도 말함

### 제 2 정규화를 하지 않으면 생기는 문제

| 학번 | 이름 | 소속학과 | 학과장 |
| --- | --- | --- | --- |
| 1901 | 홍길동 | 컴퓨터과 | 김교수 |
| 1845 | 임꺽정 | 전자과 | 박교수 |
| 1706 | 신사임당 | 기계과 | 천교수 |
| 1925 | 장영실 | 컴퓨터과 | 김교수 |
- PK는 학번
- 하지만 소속학과와 학과장은 서로를 결정지을 수 있음
- 이 경우 (소속학과, 학과장)을 별도 테이블로 분리하지 않으면 다음의 문제가 발생
    - 학생이 추가될 때마다 학과장 데이터가 불필요하게 중복
    - 학과장이 변경되면 여러 개 데이터가 수정되어야 함
    - 학생 데이터가 제거될 때 학과장 데이터도 유실될 수 있음

## 제 3 정규화

- X→Y, Y→Z일 때 X→Z인 관계를 제거
- X,Y를 갖는 테이블, Y,Z를 갖는 테이블로 분리함으로써 제거
- 이 과정을 `이행적 함수 종속`을 제거한다고도 말함
- **일반적으로 3정규형 까지 보장하면 중복/유효하지 않은 종속성에 의해 발생하는 치명적 문제들을 해결할 수 있음**

### 제 3 정규화를 하지 않으면 생기는 문제

| 학번 | 이름 | 소속학과 | 대학 |
| --- | --- | --- | --- |
| 1901 | 홍길동 | 컴퓨터과 | 공대 |
| 1845 | 임꺽정 | 전자과 | 공대 |
| 1706 | 신사임당 | 경제 | 상경 |
| 1925 | 장영실 | 경영 | 상경 |
- 학번→소속학과, 소속학과→대학이면 학번→대학이 가능
- 대학 정보가 매우 중복됨
- 특정 대학명이 바뀌는 경우 여러 데이터를 수정해야 함
- 학생 데이터가 제거될 때 대학 데이터도 유실될 수 있음

## BCNF

- candidate key가 아님에도 결정자 역할을 하는 것을 제거
- 테이블 내 특정 컬럼을 결정지음에도 모든 컬럼을 결정지을 수 있는 컬럼(후보키)이 아닌 경우 이를 별도 테이블로 분리해야 함

## 4NF

- `다치 종속성`을 제거해야 함