# 📜 Iterator Pattern

## Iterator Pattern (반복자 패턴)

`반복자 패턴`은 객체 집합의 요소들을 일괄적으로, 순차적으로 접근하도록 하기 위해 사용하는 패턴이다.

사용하는 자료구조의 변경이 관계 없는 부분의 변경을 초래하지 않도록 하기 위해 집합의 요소를 별도의 관리 객체(Iterator) 안에 캡슐화한다. 즉, Iterator는 클라이언트와 데이터 간 중재자 역할을 하게 되는 것이다.

### 예시

클라이언트가 기존에 아래와 같이 LinkedList 자료구조를 통해 데이터 집합을 처리하고 있었다고 하자.

![Use-Linked-List](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/f7ed1358-0699-4fd6-9913-70becb001b49/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220606%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220606T125344Z&X-Amz-Expires=86400&X-Amz-Signature=afda0f204514c0b1f5b7ce695720b9058bfcff51e4b3d877fdead955cd759a16&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

그러다가 요구의 변경에 의해 자료구조를 BalancedTree로 변경하게 되었다. 그렇다면 기존에 LinkedList를 사용하여 구현된 코드들에 모두 변화가 일어나게 된다.

![Use-Balanced-Tree](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/967be07d-6e5e-419d-980c-3d2c2d84c972/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220606%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220606T125345Z&X-Amz-Expires=86400&X-Amz-Signature=2efa8febc7454deb3aa41cf409ee500894f8adebebb1165cc9a0e6ca26a1f257&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

두 개는 서로 다른 자료형임은 물론이고, 서로 다른 메소드를 가질 것이므로 이 변화의 크기는 매우 커질 수 있다.

이러한 사태를 막기 위해, 어떤 자료구조를 사용하는지 은닉하고 이들의 공통 기능을 정의한 관리 객체를 이용하도록 한다.

### 구성 요소

![Iterator-Pattern](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/ab149170-6185-49eb-96c5-9f0d4e5bcd93/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220606%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220606T125431Z&X-Amz-Expires=86400&X-Amz-Signature=3a0183268b0d75b1c9fafbd1c462645578ab73d9b71bc348dfaaa13f92e711b1&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

- `Aggregate` - 요소들의 집합을 다루기 위한 공통 기능을 정의한 인터페이스
- `ConcreteAggregate` - 요소들의 집합을 다루는 클래스 (ArrayList 등)
- `Iterator` - 요소들의 집합을 일괄적으로 다루기 위한 인터페이스
- `ConcreteIterator` - Iterator를 구현하는 클래스로, Aggregate와 일대일 대응하며 Aggregate에 의해 생성된다. (ex: LinkedList.iterator()를 통해 연결 리스트의 이터레이터 생성)
- `Client` - Aggregate를 만들고 이로부터 Iterator를 생성해내는 클래스

### 특징

- Java 기준 대부분의 기본 자료구조에 Iterator를 반환하는 메소드가 정의되어 있다.
