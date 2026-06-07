
## 개요
- 파드들을 여러 토폴로지 도메인에 고르게 분산시켜 단일 장애점을 막고 고가용성을 높이기 위한 기능
- 토폴로지 도메인 이란?
	- 토폴로지: CS(특히 네트워크, 분산 시스템 이론)에서는 주로 컴퓨터나 장비들이 물리적/논리적으로 배치되고 연결된 구조를 의미 (ex: Star Topology, Ring Topology, ...)
	- 도메인: 인프라 관점에서는 주로 '장애 발생 시 영향 범위'를 기준으로 분리한 영역을 의미함.
	- 정리하자면 토폴로지 도메인은 전체 클러스터 인프라를 지리적, 물리적, 혹은 네트워크 구조상 **특정 기준(장애 범위나 물리적 위치)으로 묶은 하나의 구역**을 의미한다고 볼 수 있다.

## 사용법
```yaml
---
apiVersion: v1
kind: Pod
metadata:
  name: example-pod
spec:
  # Configure a topology spread constraint
  topologySpreadConstraints:
    - maxSkew: <integer>
      minDomains: <integer> # optional
      topologyKey: <string>
      whenUnsatisfiable: <string>
      labelSelector: <object>
      matchLabelKeys: <list> # optional; beta since v1.27
      nodeAffinityPolicy: [Honor|Ignore] # optional; beta since v1.26
      nodeTaintsPolicy: [Honor|Ignore] # optional; beta since v1.26
  ### other Pod fields go here
```
- `maxSkew`: 서로 다른 토폴로지 도메인 간에 허용되는 파드 수의 최대 차이 (N 이면 도메인 간 파드 개수 차이가 N보다 커질 수 없음)
- `topologyKey`: 노드를 그룹화하는 기준이 되는 노드 레이블의 키
	- topology.kubernetes.io/zone: 가용 영역(AZ)을 의미. 특정 데이터센터에 문제가 생겨도 여러 AZ에 분산되어 있으면 다른 데이터센터를 통해 서비스를 제공할 수 있다.
	- kubernetes.io/hostname: 개별 노드를 의미
- `whenUnsatisfiable`: 조건 불만족 시(제약 조건을 만족하면서 파드를 배치할 공간이 없을 때) 스케줄러의 동작을 결정
    - `DoNotSchedule`: 파드를 스케줄링하지 않고 Pending 유지 (Hard 제약)
    - `ScheduleAnyway`: Skew(편차)를 최소화하는 방향으로 일단 파드를 스케줄링 (Soft 제약)
- `labelSelector`: 분산 규칙을 적용할 대상 파드들을 식별하기 위한 레이블 조건

## Pod Affinity 기능과의 차이점
- [노드에_파드_할당하기_(Node_Selector,_Affinity)](노드에_파드_할당하기_(Node_Selector,_Affinity).md) 참고
- 둘 다 파드들을 분산하기 위한 기능이라는 공통점은 있지만 Pod Affinity가 파드들끼리 못 붙도록, 즉 노드에 단 하나의 파드만 존재하도록 하는 게 목표라면 Affinity는 밀어내기보다 "분산"이 목적임
- 즉 아래와 같이 나눌 수 있다.
	- Pod Affinity: 파드 간 상호 배타적 격리 (같이 있으면 안 됨)
	- Topology Spread: 균형 잡힌 리소스 배분 (로드 밸런싱, 고가용성/성능 확보)
