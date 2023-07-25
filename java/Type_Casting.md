# Type Casting

### 기본형 → 문자열: `parse~(str)`

```java
// 문자열 -> 기본형: Wrapper자료형.parse자료형(문자열)
int primNum = Integer.parseInt(str);
double primDoub = Double.parseDouble(str);
```

### 문자열 → 기본형: `String.valueOf(val)`

```java
// 기본형 -> 문자열: String.valueOf(자료형)
String primNumStr = String.valueOf(primNum);
String primDoubStr = String.valueOf(primDoub);
```

### Wrapper 객체 → 문자열: `valueOf(str)`

```java
// 문자열 -> Wrapper 자료형: Wrapper자료형.valueOf(문자열)
Integer wrapNum = Integer.valueOf(str);
Double wrapDoub = Double.valueOf(str);
```

### 문자열 → Wrapper 객체: `String.valueOf(Val)`

```java
// Wrapper 자료형 -> 문자열: String.valueOf(자료형)
String wrapNumStr = String.valueOf(wrapNum);
String wrapDoubStr = String.valueOf(wrapDoub);
```

### 10진수 숫자형 → 2, 8, 16진수 문자열: `toString(값, 진수)`

```java
// 10진수 숫자 -> 2, 8, 16진수 문자열: String.valueOf(
int dec = 16;
String bin = Integer.toString(dec, 2); // 10000
String bin2 = Integer.toBinaryString(dec); // 10000

String oct = Integer.toString(dec, 8); // 20
String oct2 = Integer.toOctalString(dec); // 20

String hex = Integer.toString(dec, 16); // 10
String hex2 = Integer.toHexString(dec); // 10
```

### 2, 8, 16진수 문자열 → 10진수 숫자형: `parseInt(값, 진수)`

```java
// 2, 8, 16진수 문자열 -> 10진수 숫자: Integer.parseInt(문자열, 진수)
int binToDec = Integer.parseInt(bin, 2);
int binToOct = Integer.parseInt(oct, 8);
int binToHex = Integer.parseInt(hex, 16);
```
