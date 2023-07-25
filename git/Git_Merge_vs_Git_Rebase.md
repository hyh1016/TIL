# Git Merge vs Git Rebase

## Merge, Rebase

### 공통점

* 서로 다른 두 브랜치의 내용을 모두 반영

### 차이점

* Merge는 두 브랜치의 변경 사항을 모두 반영한 새로운 커밋을 생성 (머지 커밋)
* Rebase는 이를 호출한 브랜치에서 다른 브랜치로 base를 변경하는 것으로 새로운 커밋을 생성하지 않고 변경 사항 반영

## Merge

```java
git merge {머지할 브랜치}
```

* 호출한 브랜치에 머지할 브랜치의 변경 사항을 반영

### 장점

* Rebase에서 발생할 수 있는 위험성은 없음

### 단점

* 항상 두 브랜치의 변경 사항을 모두 반영한 새 커밋이 생김
* 따라서 커밋 내역과 Git Graph가 지저분해질 수 있음

## Rebase

### 장점

* 별도의 새 커밋 없이 양 쪽의 변경사항을 모두 반영할 수 있음
* 내가 마치 상대방이 작업한 이후에 작업한 것처럼 히스토리가 기록되기 때문에 브랜치 그래프를 깔끔하게 관리할 수 있음

### 단점

* **리베이스의 동작 원리에 의한 위험성**
  * 머지는 그냥 현재 브랜치에서 머지할 브랜치와의 변경 내역을 반영한 새 커밋 찍고 끝
  * 리베이스는 현재 브랜치에서 리베이스할 브랜치를 patch로 만들고 여기서 현재 브랜치의 작업내용을 그대로 다시 커밋하는 방식으로 동작
    * 즉, base를 리베이스할 브랜치의 마지막 커밋으로 옮긴 이후 시점의 `모든 커밋이 새로 작성됨`
      * `커밋 해시가 변경`되고, 리베이스 이전의 커밋과 `완전히 다른 커밋으로 간주`됨
  * 따라서 다음과 같이 이미 원격 저장소에 push한 커밋을 rebase 해서는 안 됨
    1. 내 작업에 대한 커밋 A, B를 origin에 push
    2. 다른 사람의 작업 내용을 반영하고자 rebase
       * base가 재설정되며 이후의 작업물인 A, B 커밋은 A’, B’ 커밋으로 변경됨
    3. 이후 다른 작업 C를 수행해 커밋하고 origin에 push
    4. **기존의 A, B와 A’, B’는 같은 작업임에도 다른 커밋으로 간주됨**

### Rebase 문제점 예시

1.  마스터에서 브랜치 a로 체크아웃하고 새 커밋을 생성

    ```java
    commit f132497e029781371a1fb6602a27d44947327be7 (HEAD, master, a)
    Author: ~
    Date:   ~

        a commit (1)

    commit 2a56f8e097407782b80d01b963b51a5da52052eb
    Author: ~
    Date:   ~

        Initial commit
    ```
2.  마스터에서 브랜치 b로 체크아웃하고 두 개의 새 커밋을 생성

    ```java
    commit 5c966a660743e97751b2cc3a02dbb6af52742c95 (HEAD -> b)
    Author: ~
    Date:   ~

        b commit (2)

    commit 9d2628054585e816abb2d3c1e1e4805cd2fa0c58
    Author: ~
    Date:   ~

        b commit (1)

    commit 2a56f8e097407782b80d01b963b51a5da52052eb (master)
    Author: ~
    Date:   ~

        Initial commit
    ```
3. 마스터가 a를 리베이스하고(충돌 없음), b로 이동해 마스터를 리베이스(a, b간 작업 내용 충돌)
4.  충돌 해결 후 `git rebase --continue` 명령을 통해 리베이스를 수행

    ```java
    commit **9d4cf26dcbd273d3ebae0417c105c400f131b333** (HEAD -> b)
    Author: ~
    Date:   ~

        b commit (2)

    commit **bfa0260647e48ec204a450c459a1164a14f98e94**
    Author: ~
    Date:   ~

        b commit (1)

    commit f132497e029781371a1fb6602a27d44947327be7 (master, a)
    Author: ~
    Date:   ~

        a commit (1)

    commit 2a56f8e097407782b80d01b963b51a5da52052eb
    Author: ~
    Date:   ~

        Initial commit
    ```

    * master의 base(시작점)가 b에서의 master의 위치(Initial Commit)에서 리베이스를 시도한 master(a commit (1))로 이동
    * 그 이후의 b의 커밋의 커밋 해시가 모두 바뀜
      * 복사한 브랜치에 커밋을 새로 쓰고 이를 새 b 브랜치로 간주하므로
    * 만약 원격에 앞선 b의 커밋 내역이 반영되어 있었다면 4번의 깃 히스토리를 푸시할 시 문제가 발생

## 외부 저장소의 코드를 pull하는 경우

### fetch?

```bash
git fetch {원격저장소 별칭} {원격저장소 브랜치}
```

* FETCH\_HEAD라는 브랜치에 해당 원격 브랜치의 변경 사항을 반영

### fetch-merge (default pull)

```bash
# 1
git config pull.rebase false  # merge (the default strategy)
git pull origin {branch}

# 2
git fetch origin {branch}
git merge FETCH_HEAD
```

### fetch-rebase

```bash
# 1
git config pull.rebase true   # change strategy to rebase
git pull origin {branch}

# 2
git fetch origin {branch}
git rebase FETCH_HEAD
```

## Merge, Rebase 전략 결론

* 기본 전략은 rebase로 하되 외부에 PR을 올려놓고 추가 작업 하는 경우에는 직접 fetch-merge 수행
* 만약 실수로 외부에 PR 있는데 git pull 해서 rebase를 시도한 경우 `git rebase --abort`로 리베이스 취소하고 다시 fetch-merge
