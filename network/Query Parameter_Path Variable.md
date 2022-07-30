# 🎈 Query Parameter, Path Variable

## Query Parameter

- URL을 통해 특정 정보를 전달하기 위해 사용한다. 주로 `필터링` 등의 기능에 사용된다.
- 정보의 Attribute name, value가 모두 URL에 포함된다.
- 생략할 시 400이 발생한다.

## Path Variable

- 리소스를 `식별`하기 위해 사용한다.
- 정보의 value만이 URL에 포함된다.
- 없는 자원일 시 404가 발생한다.
