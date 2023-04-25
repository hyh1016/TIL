# 🗃 Row-Oriented vs Column-Oriented

## Row Oriented Database

- 데이터를 Row 단위로 저장
- 즉, 하나의 데이터 묶음 단위로 저장
    - Person이라는 테이블에 name, age, gender라는 정보가 저장된다면 (name, age, gender) 단위로 저장되는 것
- 데이터 단위로 다루어지기 때문에 저장 속도가 빠르다. 한 공간에 다 집어넣기 때문
- MySQL, PostgreSQL과 같은 대부분의 Major DBMS가 이 방식을 채택하고 있다.

## Column Oriented Database

- 데이터를 Column 단위로 저장
- 즉, 하나의 속성을 기준으로 저장
    - 위의 Person 기준 name에 대한 값을 쭉 저장하고 age에 대한 값을 쭉 저장하는 느낌
- 속성 단위로 다루어지므로 조회 시 특정 속성값 데이터만 꺼내오고자 한다면 더 빠른 속도로 얻어올 수 있다.
- 그러나 저장 속도가 Row-Oriented보다 느리고(속성별로 저장해야 하므로 하나의 데이터를 저장할 때 저장 지점을 여러 개 찾아야 함), 데이터 단위로 조회할 때에는 빠른 속도를 보장하기 어렵다.