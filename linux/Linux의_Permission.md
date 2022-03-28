
# ⚠ Linux의 Permission

## Permission Error

Linux OS에서 작업을 해 본 사람이라면 한 번쯤 아래 오류를 만나본 적이 있을 것이다.

```shell
Permission denied.
```

이는 현재 해당 쉘을 사용하고 있는 사용자가 `해당 파일에 대한 해당 권한이 없기 때문에` 발생하는 오류이다.

이 오류를 해결하기 위해서는 Linux의 권한 체계에 대한 이해가 필요하다.

## Linux의 권한 체계

Linux에서는 파일별로, 사용자별로 권한의 종류별로 권한을 관리한다.

각 권한은 아래와 같이 사용자별(파일 오너, 오너가 속한 그룹, 나머지 사용자들)에 따라 3비트의 2진수로 부여되고 확인할 수 있다.

![Linux Permission Structure](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/e05bd834-0c1c-4be6-b999-57e942a981f6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220327%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220327T123550Z&X-Amz-Expires=86400&X-Amz-Signature=972555a4857531cea3143036966451aa6fcba1fe32723a7d06f9fa092c09d5cf&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

이렇게 부여된 권한을 확인하고자 한다면 `ls -l` 명령을 이용하면 된다.

![ls -l](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/a06a6b2d-8d84-46ac-a23a-7670ddc5b0a1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220327%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220327T123614Z&X-Amz-Expires=86400&X-Amz-Signature=cca5e716b572e754095642a5da25637a0735371760bca3a867e7aed2a5eb2c2b&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

위의 파일들은 다음과 같은 권한을 소유한다.

- `rootexecfile`: owner인 root는 읽고, 쓰고, 실행할 수 있으며 나머지는 읽고, 실행할 수는 있지만 쓸 수는(내용을 변경할 수는) 없다.
- `yhfile`: owner인 yihyun은 읽고, 쓰고, 실행할 수 있으며 나머지는 읽을 수만 있다.

## Super User인 `root`

root는 모든 권한을 무시할 수 있다. 예를 들어, 아래와 같이 동작한다.

- 다른 사용자로 로그인하기 위해서는 해당 사용자의 비밀번호를 입력해야 한다. 그러나 root는 비밀번호를 입력하지 않고도 해당 사용자로 로그인할 수 있다.
- root는 owner 이외에 부여되지 않은 permission이 있어도 이와 상관 없이 파일을 읽고, 변경하고, 실행할 수 있다.

때문에 `root 권한을 관리하는 것은 아주 중요`하다. root 권한이 아무에게나 주어지지 않도록 유의해야 한다.

## 권한 부여 명령어 `chmod`

파일의 권한을 변경하기 위해 chmod 명령을 사용할 수 있다.

### 숫자로 부여

```java
// chmod {owner}{group}{other}
chmod 755 {filename} // rwx r-x r-x
chmod 744 {filename} // rwx r-- r--
```

모든 사용자의 모든 권한을 한 번에 설정할 수 있기 때문에 전체 권한을 설정할 때에 용이하다.

### 문자로 부여

```java
// chmod {u/g/o/a}{+/=/-}{r/w/x}
chmod u+w {filename}
chmod g+r {filename}
```

일부 권한을 설정하는 경우 용이하다.

- u/g/o/a: 각각 user(owner), group, other, all을 뜻한다.
- +/=/-: 각각 권한의 추가, 지정, 삭제를 뜻한다.
- r/w/x: 읽기, 쓰기, 실행 권한을 뜻한다. (뒤에서 나올 특수 권한도 이 자리에 올 수 있다.)

## 특별한 모드

User(Owner), Group, Other에 대한 권한 비트 이외에도 특별한 모드를 위한 비트가 존재한다.

이 비트는 4, 2, 1의 값을 가질 수 있으며 각각은 다음을 의미한다.

- 4: 해당 파일을 setuid 파일로 선언한다.
- 2: 해당 파일을 setgid 파일로 선언한다.
- 1: 해당 디렉토리에 sticky bit를 적용한다.

### setuid

해당 파일의 실행 도중 owner 권한이 필요한 동작을 수행하기 위해 실행자에게 owner 권한을 부여하는 기능이다.

setuid 프로그램은 실행 중에는 EUID(Effective User ID)가 파일의 owner로 변경된다. 즉, 파일 실행 중에는 파일 소유자의 권한을 얻는 것이다.

때문에 root 소유의 파일을 setuid 프로그램으로 만드는 것은 매우 주의해야 한다.

### setgid

해당 파일의 실행자에게 해당 파일의 group 권한을 부여하는 기능이다.

### sticky bit

`공용 디렉토리`를 선언하기 위한 비트. 디렉토리에만 적용 가능하며 나머지에 적용할 시 무시된다.

해당 특수 권한 비트가 적용된 디렉토리는 누구든 상관없이 파일/디렉토리를 생성할 수 있으나 해당 파일/디렉토리의 소유자 또는 root가 아니라면 수정과 삭제는 불가능하다.

아래와 같이 Others의 실행 권한이 표기되는 위치에 소문자 t가 표기되는 경우 sticky bit가 적용된 것이다.

![Sticky Bits](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/350dab82-3acc-4746-a43d-97c640445eb7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220328%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220328T062044Z&X-Amz-Expires=86400&X-Amz-Signature=26ee4f1ecb1f7059b804ca48cda17de89a4f4447ea235f284146289882fa28f7&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)
