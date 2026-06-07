
## 개요
- 파드 할당 시 조건을 만족하는 노드에만 파드가 할당되도록 하는 기능들
- 특정 타입의 노드(CPU, GPU)에 할당되어야 하는 파드를 제어하거나, 파드들끼리 같은/서로 다른 노드에 할당하기 위해 사용
- 해당 문서에서 파드의 입장에서 할당할 노드 후보를 선정하는 기능들을 살펴본다면, [Taint_and_Toleration](Taint_and_Toleration.md) 에서는 노드의 입장에서 어떤 파드들만 선택적으로 수용할지를 살펴봄
능
## NodeName
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
  - name: nginx
    image: nginx
  nodeName: kube-01
```
- 해당 이름을 가진 노드에 할당
- 스케줄러를 우회하여 강제하는 방법이기 때문에 해당 노드가 이용 불가능한 경우 파드 할당에 실패

## NodeSelector
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
  labels:
    env: test
spec:
  containers:
  - name: nginx
    image: nginx
    imagePullPolicy: IfNotPresent
  nodeSelector:
    disktype: ssd
```
- 해당 레이블을 가진 노드에 할당
- 완전 일치의 경우에만 할당되기 때문에 유연성이 떨어짐. 더 복잡한 할당 조건을 사용하려면 `Affinity`기능을 사용

## Affinity
- 한국말로 하자면 '선호'. 즉, 선호하는 노드 후보에 우선적으로 배치될 수 있도록 목표함
### Node Affinity
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: with-node-affinity
spec:
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
        - matchExpressions:
          - key: topology.kubernetes.io/zone
            operator: In
            values:
            - antarctica-east1
            - antarctica-west1
      preferredDuringSchedulingIgnoredDuringExecution:
      - weight: 1
        preference:
          matchExpressions:
          - key: another-node-label-key
            operator: In
            values:
            - another-node-label-value
  containers:
  - name: with-node-affinity
    image: registry.k8s.io/pause:3.8
```
- Node Selector와 마찬가지로 노드를 레이블 기반으로 평가
- 반드시 충족(Hard) 조건과 선호(Soft) 조건을 지정 가능 (둘 중 1개 이상 지정 가능)
	- `requiredDuringSchedulingIgnoredDuringExecution` (Hard)
		- 파드가 노드에 할당하기 위해 (노드가) 필수로 충족해야 하는 조건
	- `preferredDuringSchedulingIgnoredDuringExecution` (Soft)
		- 충족하면 좋고, 아니면 말고 - 충족하는 노드에 가중치(우선도)를 부여하는 조건
### Pod Affinity
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: with-pod-affinity
spec:
  affinity:
    podAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
      - labelSelector:
          matchExpressions:
          - key: security
            operator: In
            values:
            - S1
        topologyKey: topology.kubernetes.io/zone
    podAntiAffinity:
      preferredDuringSchedulingIgnoredDuringExecution:
      - weight: 100
        podAffinityTerm:
          labelSelector:
            matchExpressions:
            - key: security
              operator: In
              values:
              - S2
          topologyKey: topology.kubernetes.io/zone
  containers:
  - name: with-pod-affinity
    image: registry.k8s.io/pause:3.8
```
- 위의 Node Affinity가 노드 레이블 기준이었다면 이 조건은 "해당 노드에서 이미 실행 중인" 파드의 레이블을 기준으로 함
- 조건을 만족하는 파드가 있는 노드에 배치하거나, 이러한 파드가 없는 노드에 배치하거나를 선택 가능
	- 파드 어피니티 (Affinity)
		- 조건을 만족하는 파드가 있는 노드에 배치
		- ex) 통신 빈도가 높은 웹 서버 파드와 캐시 파드를 동일한 노드에 배치하여 네트워크 지연 최소화
	- 파드 안티-어피니티 (Anti-affinity)
		- 조건을 만족하는 파드가 없는 노드에 배치
		- ex) 웹 서버 파드들을 여러 노드에 분산시켜 특정 노드 다운 시 발생하는 단일 장애점(SPOF) 방지
