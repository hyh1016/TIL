# 📜 Observer Pattern

## Observer Pattern (옵서버 패턴)

클래스 A와 B가 서로 통보하고 통보받는 관계를 가졌다고 하자. A는 B에게 통보하기 위해 B를 참조하고 B는 A에게 통보받기 위해 A를 참조한다. 이러한 양방향 결합은 강한 결합을 형성한다.

여기서 통보받는 클래스 B가 새로운 버전 C로 업데이트된다고 하자. 그러면 A 또한 B가 아닌 C를 참조하기 위해 변경이 일어난다. 이는 OCP를 위배하는 것이다.

또한, 만약 A가 B와 C에게 동시에 통보해야 한다면? 더 많은 객체에 통보하게 된다면? 그 때마다 A를 변경하는 것은 비효율적이고, 각 객체를 은닉하지 않은 채 개개의 것으로 다루는 것 또한 비효율적이다. 이러한 문제를 해결하기 위해 등장한 `가장 대표적인 행위 패턴`이 바로 `Observer Pattern(옵서버 패턴)`이다.

### Class Diagram

![Observer-Class-Diagram](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/cd8a1672-bcce-4937-b642-5a2c33523b5b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220419%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220419T015353Z&X-Amz-Expires=86400&X-Amz-Signature=1d09f3612e45a7841b48260b8a1e3d3a1cc2a0bc0c18147ba4e681ce62bb5ef1&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

- `Subject` - 자신의 변화를 관찰자에게 통보하는 객체이다.
- `Observer` - 관찰자로, 서브젝트의 변화를 통보받고 변화를 반영한다.

```java
※ Observer Pattern을 적용할 때에는 가급적 주어진 메서드명
(attach, detach, notify, update 등)을 그대로 사용하는 것이 좋다.
다른 사람이 코드를 읽을 때 Observer Pattern을 적용했음을 알기 쉽게 하기 위함이다.
```

### State Diagram

![Observer-Sequence-Diagram](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/d8f1045f-4908-4b40-867f-2822edde1f5a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220419%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220419T015402Z&X-Amz-Expires=86400&X-Amz-Signature=bd6304f53ad4ddc1d3e5a8cbeb96c09774806f350d933acb17ff56168c6a4365&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

### 장점

서브젝트는 단지 단일 옵서버 또는 옵서버의 리스트만을 가질 뿐 해당 옵서버가 무슨 옵서버인지는 모른다. 따라서 서브젝트와 옵서버는 서로 독립적으로 변경, 확장될 수 있다. (느슨한 결합)
