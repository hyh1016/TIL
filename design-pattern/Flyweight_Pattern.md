# 📜 Flyweight Pattern

## Flyweight Pattern (플라이웨이트 패턴)

![Flyweight-Pattern](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/4750a67f-9757-46ca-994f-1b37a0ed08ac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220520%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220520T143033Z&X-Amz-Expires=86400&X-Amz-Signature=ec174e1368fa292d5d868bfa595ced11242adfe9d12ab9a5a0bf4c1f3b79bd07&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

개발하려는 응용 프로그램이 특정 클래스에 대해 아주 많은 객체를 필요로 한다고 가정하자. 객체의 크기가 커지면 커질수록 저장 공간에 대한 부담이 커질 것이다.

(게임의 캐릭터 객체가 가장 이해하기 쉬운 예시가 될 수 있다. 전사, 궁수, 마법사 객체는 해당 직업의 캐릭터 하나를 만들고자 할 때마다 생성되어야 한다.)

위와 같은 경우 객체의 크기를 줄이고자 `객체마다 가져야 할 데이터(Extrinsic Data)`와 `객체 간에 공유되는 데이터(Intrinsic Data)`를 구분하여 관리하도록 하는 패턴이 바로 플라이웨이트 패턴이다.

### 구성 요소

- `Client` - 공유되지 않는 데이터를 보관하거나 Flyweight에게 전달한다.
- `FlyweightFactory` - Flyweight 객체를 생성하고 공유한다.
- `Flyweight` - 공유에 사용할 클래스들의 인터페이스를 선언
- `ConcreteFlyweight` - 공유 가능한 객체들에 해당한다.
- `UnsharedConcreteFlyweight` - 공유할 수 없지만 공유 객체들과 함께 취급되는 객체들에 해당한다.

### 특징

- SRP를 위배한다. SRP를 만족하기 위해서는 Intrinsic, Extrinsic Data가 한 클래스에 존재해야 하기 때문이다. 따라서 SRP를 위배하는만큼 얻는 이익(감소되는 필요 자원의 양)이 클 때만 사용해야 한다.

### 함께 사용되는 패턴

- `Factory Pattern` - flyweight 객체를 관리하기 위해 Factory Pattern을 이용한다.
- `Singleton Pattern` - Factory는 하나만 존재하면 되기 때문에, Factory를 Singleton으로 생성한다.
