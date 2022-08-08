# ❓ VARCHAR의 길이제한

클라이언트에서도 데이터베이스에서 길이 제한 오류가 나지 않도록 문자열 길이에 제한을 둘 필요가 있다.

보통 한글과 같은 문자는 1 Byte가 아닌 2 또는 3 Bytes로 이루어진다. (주로 사용하는 UTF-8은 한글을 3 Bytes로 표현한다.)

따라서, VARCHAR가 Byte를 기준으로 한다면 VARCHAR의 길이 제한은 어떤 것을 입력하는지, 어떤 인코딩 방식을 사용하는지에 따라 달라질 것이다.

이를 모르고 사용하면 추후에 이슈가 생길 수도 있고, 데이터베이스 마이그레이션 시 문제가 발생할 여지도 있을 것 같아 주로 사용하는 DBMS 종류별로 정리해보았다.

## VARCHAR의 기준 - MySQL

버전 4.1 이전까지는 Bytes를 사용했다가 4.1부터는 Character를 사용한다고 한다. 즉, 어떤 문자든 종류에 상관없이 1개당 1로 인식한다.

## VARCHAR의 기준 - Oracle

Bytes를 사용할지 Character를 사용할지 지정이 가능하다. 디폴트(지정하지 않음)는 Bytes이다.

```sql
varchar2(10) // 10 Bytes 저장 가능
varchar2(10 byte) // 10 Bytes 저장 가능
varchar2(10 char) // 10 Character 저장 가능
```

## VARCHAR의 기준 - PostgreSQL

Character를 기준으로 한다.

## 출처

[https://dung-beetle.tistory.com/26](https://dung-beetle.tistory.com/26)

[https://mentha2.tistory.com/195](https://mentha2.tistory.com/195)

[https://www.postgresql.org/docs/current/datatype-character.html](https://www.postgresql.org/docs/current/datatype-character.html)
