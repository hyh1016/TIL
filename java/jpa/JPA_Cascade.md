# JPA Cascade

## Cascade

- 단어의 의미는 `폭포`, `폭포처럼 떨어지다`를 의미
    - 한 곳에서 일어난 사건이 다른 곳에까지 영향을 미치게 된다는 느낌으로 사용된듯
- DB의 cascade는 부모 레코드의 수정/삭제가 자식 레코드에도 영향을 주도록 하는 옵션
    - update cascade - 부모 레코드에 업데이트가 일어나면 업데이트가 일어난 컬럼을 참조하고 있던 자식 레코드에도 반영
    - delete cascade - 부모 레코드가 삭제되면 이를 참조하는 자식 레코드도 삭제
- 위와 같이 cascade 옵션이 존재하는 이유는 `참조 무결성` 보장을 위함
    - 부모 레코드의 PK를 A→B로 업데이트해주면 A는 존재하지 않는 값이 됨. 이를 FK로 참조하고 있는 자식 레코드의 값이 그대로 A로 유지된다면 존재하지 않는 FK를 참조하는 것이므로 참조 무결성이 깨지게 됨
    - 부모 레코드가 제거되어 PK가 유효하지 않은 것이 되는 경우에도 마찬가지임

## JPA Cascade

- 부모 엔티티에 특정 사항이 적용되면 이를 자식 이벤트에도 반영하겠다는 의미는 DB의 cascade와 동일
- 하지만 JPA는 영속성이라는 개념이 존재하기 때문에 단순히 데이터 자체의 수정, 삭제를 반영하는 DB cascade보다 더 다양한 옵션이 제공됨

### JPA Cascade Type

cascade type은 0개 이상이 지정될 수 있으며, default 설정은 아무것도 적용되지 않은 빈 배열임

1. **Persist (영속)**
    - 연관된 엔티티도 함께 영속화
    - 일대다 관계에서 단일인 쪽(부모)의 엔티티가 다수인 쪽(자식) 엔티티를 리스트로 소유한 채 persist의 인자로 넘겨지면 두 쪽 모두 영속화됨
2. **Merge (병합)**
    - 엔티티 상태를 병합(업데이트)할 때 연관된 엔티티도 함께 반영
    - 영속이 insert 시점에 부모자식 모두를 반영하는 방법이라면, 병합은 update 시점에도 부모자식 모두를 반영
3. **Remove (제거)**
    - 부모 엔티티를 제거하면 자식 엔티티도 함께 제거
4. **Refresh (갱신)**
    - 엔티티를 새로고침할 때 연관된 엔티티들도 함께 새로고침
        - 새로고침이란? 캐시 값을 사용하는 대신 DB에서 실제 값을 로딩하는 행위
5. **Detach (분리)**
    - 엔티티를 영속성 컨텍스트로부터 분리할 때 연관된 엔티티도 함께 분리
6. **All (전체 적용)**
    - 1번부터 5번까지의 모든 속성을 적용
