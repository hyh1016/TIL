# Interactive Rebase

## Interactive Rebase

```shell
git rebase -i {커밋 해시}
git rebase -i HEAD~{포함할 커밋 개수}
```

- Interactive는 대화형을 의미
- 커밋 히스토리를 수정할 건데, 커밋마다 수정 방식을 사용자가 지정하여 리베이스를 수행

### 화면

인터렉티브 리베이스를 수행하면 아래와 같은 화면이 콘솔에 출력

```shell
pick {commit hash} {commit message}
pick {commit hash} {commit message}

# Rebase {hash}..{hash} onto {hash} (2 commands)
#
# Commands:
# p, pick <commit> = use commit
# r, reword <commit> = use commit, but edit the commit message
# e, edit <commit> = use commit, but stop for amending
# s, squash <commit> = use commit, but meld into previous commit
# f, fixup [-C | -c] <commit> = like "squash" but keep only the previous
#                    commit's log message, unless -C is used, in which case
#                    keep only this commit's message; -c is same as -C but
#                    opens the editor
# x, exec <command> = run command (the rest of the line) using shell
# b, break = stop here (continue rebase later with 'git rebase --continue')
# d, drop <commit> = remove commit
# l, label <label> = label current HEAD with a name
# t, reset <label> = reset HEAD to a label
# m, merge [-C <commit> | -c <commit>] <label> [# <oneline>]
#         create a merge commit using the original merge commit's
#         message (or the oneline, if no original merge commit was
#         specified); use -c <commit> to reword the commit message
# u, update-ref <ref> = track a placeholder for the <ref> to be updated
#                       to this position in the new commits. The <ref> is
#                       updated at the end of the rebase
#
# These lines can be re-ordered; they are executed from top to bottom.
#
# If you remove a line here THAT COMMIT WILL BE LOST.
#
# However, if you remove everything, the rebase will be aborted.
```

- 각 커밋의 커맨드(가장 왼쪽에 위치한 pick)를 수정해 커밋별 수행할 동작을 지정 가능
- 커밋의 위치를 바꾸거나 제거하여 커밋 순서를 변경하거나 커밋을 제거할 수 있음

### Command

잘 사용하지 않는 일부 커맨드는 생략

- `pick`: 해당 커밋을 그대로 사용
- `reword`: 커밋 메시지를 수정
- `edit`: 커밋 자체를 수정
- `squash`: 커밋 메시지를 병합 (모든 커밋 메시지 반영)
- `fixup`: 커밋 메시지를 병합하되 병합되는 커밋의 메시지는 제거
- `exec`: 리베이스 도중 실행할 shell 기반 커맨드를 지정할 수 있
