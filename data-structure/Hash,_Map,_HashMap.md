# Hash, Map, HashMap

## Hash

### 해시 함수 (해시 알고리즘)

* 임의 길이 데이터를 고정된 길이의 데이터로 매핑(변환)하는 함수
* 결과값을 `해시` 또는 `해시값` 이라고 부른다.

### 해시 테이블

* 해시 함수의 용도 중 하나로, 데이터를 저장하는 자료 구조
* 빠른 탐색 시간을 보장한다.
* Key-Value 구조를 가지며 해시값을 Key, 원래 값을 Value로 한다.
* 서로 다른 Value에 대해 해시 함수가 동일한 Key를 생성해내는 경우, 이를 `해시 충돌`이라고 한다. 해시 충돌의 해결법으로는 다른 장소를 찾는 법, 링크드리스트를 통해 같은 Key에 여러 Value를 연결하는 법이 있다.

## Map

* Key와 Value로 이루어진 자료구조
* Key의 중복을 허용하지 않는다.
* O(1)의 시간 복잡도를 보장한다.

## HashMap

* Map은 key,value 쌍을 저장하는 방법에 따라 다양한 구현 방법을 가진다. 그 중 `해싱을 이용해 저장 위치를 결정하는 방법`을 사용해 구현된 자료구조가 바로 `HashMap`이다.
* HashMap은 key값에 해시 함수를 적용한 값을 인덱스로 사용하며, 실제 값이 저장되는 공간을 버킷(Bucket)이라고 부른다.
* HashMap은 해시 함수를 통해 (key, value) 쌍이 저장될 위치를 결정하기 때문에 삽입 순서와 위치가 관련이 없으며, 사용자는 그 위치를 알 수 없다.

## 출처

[https://tecoble.techcourse.co.kr/post/2021-11-05-hash-hashmap/](https://tecoble.techcourse.co.kr/post/2021-11-05-hash-hashmap/)

[https://coding-factory.tistory.com/556](https://coding-factory.tistory.com/556)
