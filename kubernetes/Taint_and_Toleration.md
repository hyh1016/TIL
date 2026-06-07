
## 개요
- 노드에 원하지 않는 파드가 할당되는 것을 방지하는 기능
- [노드에_파드_할당하기_(Node_Selector,_Affinity)](노드에_파드_할당하기_(Node_Selector,_Affinity).md) 참고
	- 위 문서에서 다룬 Affinity는 파드를 특정 노드에 배치하기 위한 기능이었다면 이 기능은 '의도하지 않은 파드가 특정 노드에 배치되는 것을 막는' 기능

## 사용법
아래와 같이 특정 노드에 taint를 추가할 수 있음
```shell
kubectl taint nodes node1 key1=value1:NoSchedule
```
이 taint와 일치하는 toleration을 가진 파드만이 해당 노드에 배치될 자격을 얻음
toleartion 부여는 아래와 같이 `spec.tolerations` 파트에 명시
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
  tolerations:
  - key: "example-key"
    operator: "Exists"
    effect: "NoSchedule"

```
operator의 종류는 아래와 같음
- Exists: 해당 key가 존재하는 노드에 할당 가능해짐 (면역력을 가짐)
	- key 란을 비워두면 어디든 할당 가능한 만능 면역 노드를 만들 수 있다.
		- 이게 '보안 이슈'가 될 수 있지 않나? 라고 생각했는데, 애당초 Taint & Toleration은 스케줄링 도구이지 보안 목적의 도구가 아니기 때문에 관심 대상이 아님. 이걸 보안 측면에서 막기 위해서는 Admission Controller 같은 도구를 통해 개발자가 이 기능을 악용하려 할 때 사전 차단 하는 방식을 사용해야 함
- Equals: key-value 쌍이 노드의 taint와 정확히 일치할 때 할당 가능해짐
effect의 종류는 아래와 같음
- NoSchedule: 절대 스케줄링하지 않음. 단, taint 추가 이전에 동작하던 파드들은 이 조건을 만족하지 못해도 방출하진 않음
- PreferNoSchedule: 가급적 스케줄링하지 않음. 할당 가능한 노드가 이 노드 뿐일 때에는 배치
- NoExecute: 스케줄링하지 않을 뿐 아니라, 기존 파드들도 조건을 만족하지 않으면 퇴출

## 사용 사례
- 고비용 하드웨어 격리: 비싼 GPU 노드에 Taint를 걸어 일반 웹 애플리케이션 파드들은 GPU 노드에 할당되지 않으며, GPU 연산이 필요한 AI 모델 파드에만 Toleration을 부여하여 해당 노드를 쓰게 만듦
- 컨트롤 플레인 보호: 쿠버네티스 마스터(컨트롤 플레인) 노드에는 기본적으로 Taint가 걸려 있어, 사용자가 배포한 일반 파드들이 마스터 노드의 자원을 갉아먹는 것을 방지
- 노드 유지보수 및 장애 처리: 특정 노드에 장애가 발생하거나 점검이 필요할 때 `NoExecute` Taint를 부여하면, 해당 노드에서 돌고 있던 기존 파드들이 즉각적으로 쫓겨나(Eviction) 다른 건강한 노드로 재배치됨

## Affinity와 함께 사용할 것
- 두 기능 모두 사용해야 '의도한 노드에 의도한 파드를 배치'를 완성할 수 있음
- Taint & Toleration만 사용하면: 노드는 파드를 막을 수 있으나 파드가 알맞은 노드로 배치되도록 하지는 못함
- Affinity만 사용하면: 파드는 알맞은 후보를 고를 수 있으나 잘못 선정되어 노드가 의도하지 않은 파드를 할당받을 수 있음
