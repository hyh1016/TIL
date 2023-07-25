# 자주 사용하는 Git 명령어 모음

> 아! 그거! 뭐였지! 의 `그거`를 바로바로 깨닫기 위해 정리해보았다. 밥먹듯이 쓰는 기본 명령어(add, commit, push, pull 등)들을 다루지는 않는다.

## Pull - 원격 저장소로부터 내려받을 때

### fetch-rebase

git pull과 마찬가지로 원격 저장소의 내용을 로컬에도 반영

혼자 작업하는 게 아니라면 branch가 무수히 많이 나뉘므로 fetch-rebase 방식을 사용하는 것이 `git pull`을 사용하는 것보다 graph가 깔끔해짐

```java
git fetch {원격} {브랜치명}
git rebase
```

### 이미 디렉토리 내에 무언가 있는데 clone 받고 싶을 때

그냥 받으면 already exist 오류가 뜬다.

이럴 때에는 직접 원격 저장소로 등록하고 임의로 pull을 받아야 한다.

```java
git remote add origin {repository url}
git pull origin {브랜치명}
```

### 변경 사항 스택에 저장

pull을 받거나 branch를 옮기는 등의 작업을 하려고 하는데 변경 사항 때문에 수행할 수 없을 때 주로 사용

```java
git stash // 현재 변경 사항을 stack에 보관
git stash pop // stack에서 다시 꺼냄
```

## Commit - 원격 저장소에 코드를 올릴 때

### git reset —soft head^

방금 커밋한 내용이 잘못했을 때 시간을 달려서 커밋을 되돌릴 수만 있다면

(거친 세상속에 내 손을 잡아주길\~)

```java
git commit // 문제

git reset --soft head^ // 직전의 커밋을 취소 (add는 유지)
```

### 원격 저장소에 올린 파일을 없애고 추적하지 않도록 하기

.gitignore에 포함되어야 하는데 원격 저장소에 올려버려서 추적 대상에 들어가버린 파일을 `원격 저장소에서도 지우고` `추적 대상에서도 제외`하고자 할 때 사용하는 방법

```java
git rm --cached {파일명}
git rm -r --cached {폴더명}
```

### 원격 저장소에 올린 파일을 유지하되 더이상 추적하지 않도록 하기

위와 달리 원격 저장소에 올라간 것은 그대로 두되 앞으로 추적 대상에서는 제외하고자 할 때 사용하는 방법

기본 틀만 github에 올려 놓고 내용물은 환경에 따라 달리하고 싶을 때 사용

즉, develop/production에 따라 값이 달라지는 환경 변수들을 관리할 때 사용

```java
git update-index --skip-worktree {파일명}
```

## Branch Management - 협업 시의 브랜치 관리

### 브랜치 생성 및 이동

```java
git checkout -b {브랜치명}
```
