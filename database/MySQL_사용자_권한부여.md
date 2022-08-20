# ✔ MySQL 사용자 권한부여

## 사용자 생성
```sql
create user 사용자명@서버명;
create user 사용자명@서버명 identified by '비밀번호';
```

### 서버명이란?
- localhost: 로컬에서만 접속 가능
- '%': 로컬, 리모트에서 접속 가능
- 사용자 생성 시의 서버명은 생략 가능하며 생략 시 자동으로 '%'로 지정

## 사용자 삭제
```sql
drop user 사용자명@서버명;
```

## 권한 부여 (없는 사용자면 생성?)
```sql
-- privileges는 생략 가능 (grant all on~으로도 사용 가능)
grant all privileges on 데이터베이스명.테이블명 to 사용자명@서버명;
```

## 변경 사항 적용
```sql
flush privileges;
```

## 부여된 권한 조회
```sql
show grants for 사용자명@서버명
```

## 권한 삭제
```sql
revoke all on 데이터베이스명.테이블명 from 사용자명@서버명
```
