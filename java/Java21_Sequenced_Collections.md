# Java 21 - Sequenced Collections

## Java 21?

- 2021년 출시된 Java 17 이후 2년만에 출시된 Java의 4번째 LTS(Long Term Support) 버전
- 주요 변화는 다음과 같다.
    - **Sequenced Collections**
    - [Virtual Thread](./Java21_Virtual_Thread.md)
    - [Record, Switch 개선](./Java21_Improvement_Record,_Switch.md)
- 이 글에서는 Sequenced Collections에 대해 다룬다.

## Sequenced Collections

### 기존 컬렉션은 `순서`를 다루기 불편함

- 기존 컬렉션 프레임워크는 컬렉션 내 원소들에 순서가 존재할 때 사용되는 문법이 제각각이고, 일부는 가독성도 좋지 않았다.
- 예를 들어, `List` 인터페이스의 첫 번째와 마지막 원소 접근 코드는 아래와 같다.
    
    ```java
    List<String> wordList = new ArrayList<>();
    String firstWord = wordList.get(0); // 첫 번째 원소
    String lastWord = wordList.get(wordList.size() - 1); // 마지막 원소
    ```
    
    마지막 원소 접근의 경우 리스트의 길이에서 1을 뺀 값이 마지막 원소의 인덱스이기 때문에 이를 이용해 획득하고 있음을 알 수 있다.
    
    알고리즘 문제를 많이 풀어 본 사람들에게는 익숙한 표현법이라 이상함을 느끼지 못할 수도 있겠지만, `메서드명과 파라미터 어디에도 마지막을 의미하는 표현이 없다`.
    
- 이와 달리 `Deque` 인터페이스의 첫 번째와 마지막 원소 접근 코드는 아래와 같다.
    
    ```java
    Deque<String> wordList = new ArrayDeque<>();
    wordList.getFirst();
    wordList.getLast();
    ```
    
    List와 달리 처음과 끝의 원소를 반환한다는 의미가 확실한 두 메서드를 지원하고 있다.
    
- **문제는, List 구현체를 사용하던 객체에 Deque 구현체를 할당하면서 발생한다.**
    - 기존에 get을 통해 원소를 획득하던 부분을 `모두 getFirst와 getLast로 바꿔주어야 한다`.
    - 이는 확장성 면에서 좋지 않은 변화를 일으킨다고 볼 수 있다.

### Sequenced Collections

- 위에서 설명한 바와 같이, 일부 인터페이스에서 가독성이 나쁜 문제도 있었지만 가장 큰 문제는 `원소를 다루는 방식이 일관되지 않다는 점`이다.
- 이러한 불편함을 해결하기 위해 Java 21에서 도입된 것이 바로 `Sequenced Collections`이다.
- 추가된 Sequenced Collections의 인터페이스 계층 구조는 아래와 같다.
    
    ![출처: openjdk docs](https://cr.openjdk.org/~smarks/collections/SequencedCollectionDiagram20220216.png)
    
    - 추가된 인터페이스가 기존 List, Deque와 같은 인터페이스의 공통 조상임을 알 수 있다.
- `SequencedCollection` 인터페이스는 아래와 같은 메서드를 제공한다.
    
    ```java
    interface SequencedCollection<E> extends Collection<E> {
        // 역순 조회
        SequencedCollection<E> reversed();
        
    		// 기존 Deque와 동일한 첫/마지막 원소의 생성, 조회, 삭제
        void addFirst(E);
        void addLast(E);
        E getFirst();
        E getLast();
        E removeFirst();
        E removeLast();
    }
    ```
    
- 따라서, 이제 아래와 같은 방식으로 List에서도 명시적으로 첫 번째와 마지막 원소에 접근 또는 추가/삭제가 가능하며, 추후 구현체를 다른 것으로 대체해도 메서드를 일일이 수정하지 않아도 되도록 개선되었다.
    
    ```java
    List<String> wordList = new ArrayList<>();
    
    // 생성
    wordList.addFirst(element);
    wordList.addLast(element);
    
    // 조회
    wordList.getFirst();
    wordList.getLast();
    
    // 삭제
    wordList.removeFirst();
    wordList.removeLast();
    ```
    

### 집합과 맵에 특화된 Sequenced Collections

- 위의 계층도를 확인해보면, 집합과 맵 관련된 인터페이스 2가지가 함께 추가되었음을 알 수 있다.
    
    ![출처: openjdk docs](https://cr.openjdk.org/~smarks/collections/SequencedCollectionDiagram20220216.png)
    
- `SequencedSet`은 단순히 역순 컬렉션 반환 메서드가 SequencedSet을 반환하도록 재정의하고 있다.
    
    ```java
    interface SequencedSet<E> extends Set<E>, SequencedCollection<E> {
        SequencedSet<E> reversed();
    }
    ```
    
- `SequencedMap`은 단순 원소가 아닌, key 값에 대한 순서를 다루기 위해 존재하며, 아래와 같은 메서드들을 제공한다.
    
    ```java
    interface SequencedMap<K,V> extends Map<K,V> {
    		// key 기준 역순 맵 반환
        SequencedMap<K,V> reversed();
    
    		// key 기준 순차적 key, value, entry에 대한 collection 반환
        SequencedSet<K> sequencedKeySet();
        SequencedCollection<V> sequencedValues();
        SequencedSet<Entry<K,V>> sequencedEntrySet();
    
    		// 첫 번째, 마지막 entry의 추가, 조회, 삭제
        V putFirst(K, V);
        V putLast(K, V);
        Entry<K, V> firstEntry();
        Entry<K, V> lastEntry();
        Entry<K, V> pollFirstEntry();
        Entry<K, V> pollLastEntry();
    }
    ```


### 주의할 점 - reversed()는 새로운 객체를 반환하는 것이 아님

- oracle 공식문서에서도 다음과 같이 명시하고 있다.
    
    > `reversed()` method provides a reverse-ordered view of the original collection. Any modifications to the original collection are visible in the view. (reversed() 메서드는 원본 컬렉션의 역순 view를 제공하는 것으로, 원본 컬렉션의 수정은 이 view에서도 확인할 수 있다.)
    > 
- 즉, 해당 메서드의 호출 시점에 새 역순 컬렉션 객체를 생성해 반환하는 것이 아니라, 단순히 역순 시점만 가진 동일 객체의 view를 반환하는 것이다.
- 따라서, 원본 객체의 수정이 reversed()를 통해 획득한 객체에도 반영됨을 주의해야 한다.


## 출처

[오라클 openjdk 공식 문서](https://openjdk.org/jeps/431)
