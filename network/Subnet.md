# Subnet

## 서브넷

* 서브넷은 IP 주소에서 네트워크 영역을 부분적으로 나눈 부분 네트워크를 뜻한다.
* IPv4의 경우 32비트로 이루어져있어 그 수가 많지 않고, 따라서 IP를 절대적으로 고유하게 사용하면 금방 거덜나기 때문에 상대적인 IP 주소를 사용하는 것
*   서브넷은 서브넷 마스크를 통해 지정한다. 서브넷 마스크의 종류는 아래 3가지가 있다.

    ```
        A 클래스: 255.0.0.0
        B 클래스: 255.255.0.0
        C 클래스: 255.255.255.0
    ```

    * A\~D 클래스에 대해 255인 부분은 모든 비트가 1이다. 서브넷 마스크와 AND 연산을 하여 네트워크 영역을 구할 수 있다. (나머지는 호스트 영역)
    * IP 주소에 192.168.0.1/24 와 같이 슬래시 이후에 붙어있는 숫자가 왼쪽부터 1인 비트 수를 나타낸다. 따라서, /24는 C클래스까지 네트워크 영역이고 D클래스만 호스트 영역임을 나타낸다.
* 서브넷 마스크를 기준으로 네트워크 수, 서브넷 수를 유동적으로 조정하면 된다.

### 서브넷 예시

`192.168.1.0/24` 라는 하나의 네트워크가 존재한다고 하자. 네트워크 비트가 24이므로 호스트는 8, 즉 2^8=256(0\~255)에서 네트워크 주소인 0과 브로드캐스트 주소인 255를 제외한 254개 존재할 수 있다. 여기서 네트워크를 2개의 서브넷으로 분리하고자 한다면 다음과 같이 된다.

`192.168.1.0/25` ⇒ 2개의 서브넷, 각각 126개의 호스트.

서브넷 1: 0~~127인데 0과 127을 제외한 1~~126으로 126개

서브넷 2: 128~~255인데 128과 255를 제외한 129~~254로 126개
