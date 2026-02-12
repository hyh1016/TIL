# Redis Sentinel

## Redis의 고가용성(HA)과 확장성

- 한 대의 Redis 서버만 사용하게 되면(Standalone) 이 서버가 죽었을 때 레디스를 사용할 수 없게 됨 (고가용성 필요)
- 또한 Redis는 In-Memory DB인 만큼 데이터 증가에 의한 Scale-Up이 비용적인 측면에서 RDB보다 더 빠르게 한계가 찾아옴 (확장성 필요)
- **고가용성이 필요하다면 Sentinel을 도입할 수 있음**
- **고가용성과 확장성이 모두 필요하다면 [Cluster](./Redis_Cluster.md)를 도입할 수 있음**

## Redis Sentinel

https://redis.io/docs/latest/operate/oss_and_stack/management/sentinel/

### 동작 방식

- 다수 개의 Sentinel 노드가 Master, Replica 노드를 감시
- Master가 다운되면 Sentinel들이 투표를 통해 Master로 승격할 Replica를 정해 승격시킴

### 왜 쓰는가?

- Redis Standalone 방식은 마스터가 죽으면 서비스 전체가 중단되고, 자동회복(failover) 불가능
- Sentinel을 사용하면 합의를 통해 새 마스터를 정하고 승격시켜 **자동회복 가능**
- 즉, **고가용성**을 위해 사용

### Sentinel의 주요 기능

- **Monitoring**: Master, Replica가 정상 동작하는지 모니터링
- **Notification**: 문제가 생긴 Redis 인스턴스 발견 시 알림
- **Automatic failover**: Master의 이상을 감지하면 Replica를 Master로 승격하고 다른 Replica들에게 이를 알림
- **Configuration provider**: 클라이언트에게 구성 정보를 전달하는 주체로, 클라이언트는 마스터 노드 변경을 직접 추적할 필요 없이 Sentinel 에게 물어보고 전달받으면 됨

### Master가 다운되면 벌어지는 일

- 각 센티넬은 마스터가 정해진 시간동안 응답하지 않으므로 마스터의 장애를 의심 (SDOWN)
- 각 센티넬들이 서로에게 마스터의 장애 여부를 묻고, **정족수** 만큼의 마스터가 장애라고 답하면 마스터의 장애 상황이라고 결정 (ODOWN)
- ODOWN 상태가 되고, 과반수 센티넬이 마스터 교체에 동의하면 리더 센티넬이 기존 Master의 다운을 인정하고 새 Master 승격
    - 마스터의 장애를 인지하는 정족수(Quorum), 실제 교체를 수행하는 과반수(Majority)는 서로 다른 값일 수 있음
    - ‘과반수 동의’를 기준으로 동작하기 때문에 Sentinel 수는 홀수로 두는 편이 좋음

### Sentinel 간 소통 방식

- 센티넬들끼리는 개별 소통이 필요한 이슈는 RPC, 정보 전파가 필요한 이슈는 Redis Pub/Sub으로 통신함
    - Pub/Sub은 fire-and-forget 이므로 각 센티넬들이 정보를 성공적으로 수신하는지 보지 않음
    - 합의와 같이 응답이 필요하고 응답에 따라 동작이 달라지는 경우에는 RPC
- 새로운 센티넬의 추가, 마스터의 변경 등은 Pub/Sub (정보 전파)
    - 새로운 센티넬의 추가: `sentinel:hello` 라는 채널에 자신의 number, address를 보내 다른 센티넬이 이를 인지할 수 있도록 함
    - 마스터의 변경: `sentinel:hello` 채널에 변경된 마스터를 공지 (이때 버전 정보인 epoch를 함께 알리는데, 이 값이 높을 수록 최신의 것으로 간주하고 사용)
- 개별 논의가 필요한 마스터 다운 여부 결정은 RPC (합의)
