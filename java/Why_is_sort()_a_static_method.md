# 왜 Java의 정렬 함수 sort()는 static 메소드일까?

## Introduction

최근에 Python으로 알고리즘 문제 풀이를 하다가, Java로 코딩 테스트를 준비할 일이 있었다.

준비를 위해 Java에서 주로 사용되는 알고리즘 문제 풀이 문법을 정리하다가 의문점이 생겼다.

왜 자바는 정렬을 array.sort()가 아닌 Array.sort(array)로 지원하는 걸까?

이에 대해 조사해보았다.


## 내장 함수 vs 스태틱 함수

보통 Python 등의 언어에서는 정렬 등의 동작이 객체 내부 함수를 통해 이루어진다.

```python
list = [3, 1, 4, 5, 2]
list.sort()
print(list) # [1, 2, 3, 4, 5]
```

그러나 Java에서는 배열/리스트를 다루는 클래스에서 static 함수로 정렬 기능을 제공한다.

```java
import java.util.Arrays;

public class Example
{
    public static void main(String[] args)
    {
        int[] numArray = {3, 1, 4, 5, 2};
        Arrays.sort(numArray);
        System.out.println(Arrays.toString(numArray)); // [1, 2, 3, 4, 5]
    }
}
```

심지어 객체를 문자열로 변환하는 toString조차 Arrays 클래스에서 제공하는 static 함수를 이용하고 있다.

그렇다면 왜 각 객체에서 직접 내장된 sort를 정의하고 호출하는 대신 위와 같은 방법을 택한 것일까?


## 구글링

[해당 질문]([https://teamtreehouse.com/community/why-is-the-sort-a-static-method-instead-of-an-instance-method](https://teamtreehouse.com/community/why-is-the-sort-a-static-method-instead-of-an-instance-method))과 같이 나와 같은 의문을 제기한 사람이 있었고, 그에 달린 답변은 다음과 같았다.

> One possible reason for the Java designers is that sort() isn't always necessary for arrays so **they didn't want to force developers to always make sure that it is accurately implemented.**
> 

즉, 모든 array에 정렬 기능이 필요하지 않을 수 있기 때문에, 정렬을 구현하도록 강제하지 않고자 함이 하나의 이유일 수 있다는 것이다.

배열을 정렬할 책임을 Arrys 클래스로 넘김으로써, 배열과 관련된 새로운 클래스를 선언하고 기존의 클래스를 상속할 때에도 sort를 반드시 구현할 필요가 없게 되었다. 만약 sort가 내장 함수이고 이것이 상속/구현을 통해 강제된다면, 정렬이 필요하지 않은 새로운 배열을 선언할 때에도 반드시 sort를 구현할 의무를 가지게 된다.

이는 Java에서 중요시 여기는 SOLID 원칙에서 ‘S(SRP, 단일 책임 원칙)’와도 관련이 있는 것 같다. 배열 객체에는 단순히 자료를 저장할 책임만을 부여하고, 이러한 자료를 제어할 책임을 별도로 분리함으로써 단순히 자료를 저장만 하면 되는 새로운 객체가 추가될 때에 불필요하게 자료를 제어할 책임이 함께 부여되지 않도록 하였다.

앞으로 새로운 객체를 구현할 때에도 이러한 요소를 잘 고려해서 기존의 설계 의도를 해치지 않도록 해야 할 것 같다.
