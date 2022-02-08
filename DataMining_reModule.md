# Data Mining : .re module



## .re module : 패턴 매칭 함수

* pattern을 지정하고 그에 해당하는 문자열이 있는지를 파악
  * 단, 문자열 맨 앞에 있어야 하고 대소문자가 구분된다.



### 1. 검색 패턴을 미리 컴파일 하는 방법

* 여러번 사용하는 경우 패턴을 매번 새로 지정하지 않아도 되서 편함.
* 검색 속도가 빠른 편

```python
import re

pattern = "kor"

sentence1 = "I am a korean"
sentence2 = "korean boy"
sentence3 = "Korean boy"
sentence4 = "korea vs korean 차이는?"


sp = re.compile(pattern) # using same pattern
result_matchObj_1 = sp.match(sentence1) # match 결과는 matchObject 인스턴스 객체 반환
result_matchObj_2 = sp.match(sentence2)
result_matchObj_3 = sp.match(sentence3)
result_matchObj_4 = sp.match(sentence4)

print("1번 문장의 패턴 매칭 결과 :",result_matchObj_1)
print("2번 문장의 패턴 매칭 결과 :",result_matchObj_2)
print("3번 문장의 패턴 매칭 결과 :",result_matchObj_3)
print("4번 문장의 패턴 매칭 결과 :",result_matchObj_4)

print(type(result_matchObj_1))
```

> 1번 문장의 패턴 매칭 결과 : None
> 
> 2번 문장의 패턴 매칭 결과 : <re.Match object; span=(0, 3), match='kor'>
> 
> 3번 문장의 패턴 매칭 결과 : None
> 
> 4번 문장의 패턴 매칭 결과 : <re.Match object; span=(0, 3), match='kor'>
>
> <class 'NoneType'>



* 매칭 결과의 정보가 묶여서 출력됨을 확인할 수 있다.
* 매칭된 값에대한 정보만 원한다면 .group() 매서드를 사용한다.

```python
result_matchObj_2 = sp.match(sentence2).group()
print("2번 문장의 패턴 매칭 값 :",result_matchObj_2)
```

> 2번 문장의 패턴 매칭 값 : kor



## match()의 인자

### re.match(패턴 문자열, 검색 문자열, 옵션)

```python
result_matchObj = re.match('kor', 'korea')
result_matchObj2 = re.match('한국', '한국은 아름답다')

# 출력
print(result_matchObj.group())
print(result_matchObj2.group())
```

> kor
> 한국



### match()의 세번째 인자

#### 1. 대소문자 무시

* [1] re.I

  ```python
  rst_matchObj1 = re.match('kor', 'Korea', re.I) #re.I : Ignore
  print('1. re.I:', rst_matchObj1)
  ```

* [2] 인라인 방식 : (?i)

  ```python
  # rst_matchObj2 = re.match((?i)'kor', 'Korea') << 오류
  rst_matchObj2 = re.match('(?i)kor', 'Korea') # in line 방식
  print('2. 인라인 방식:', rst_matchObj2)
  ```

* [3] re.IGNORECASE

  ```python
  rst_matchObj3 = re.match('kor', 'Korea', re.IGNORECASE)
  print('3. IGNORECASE:', rst_matchObj3)
  ```

  

#### 2. 마침표와 개행문자 일치

* [1] re.S

  ```python
  rst_matchObj2 = re.findall('k.', 'kor k k\n ks', re.S)
  ```

* [2] 인라인 방식 : (?s)

  ```python
  re.findall('(?s)k.', 'kor k k\n ks')
  ```

* [3] re.DOTALL

  ```python
  re.findall('k.', 'kor k k\n ks', re.DOTALL)
  ```

  > re 출력 결과 : ['ko', 'k ', 'ks']
  >
  > re.S 출력결과 :  ['ko', 'k ', 'k\n', 'ks']



## group() 메서드

* 그룹별 문자열 반환이 가능해짐

```python
import re

# 문자열
text = "상품구매와 관련한 사항은 010-1234-4987987567 번호로 문의주세요!"

# 검색 패턴 매치 - 전화번호만 발췌
# sp = re.compile(r"(\d\d\d)-(\d\d\d)-(\d\d\d\d)")   << 그룹 내의 문자 갯수가 명시됨
sp = re.compile(r"(\d+)-(\d+)-(\d+)")              # << 그룹 내의 문자 갯수 무시
rst_matchObj = sp.search(text)
print(rst_matchObj.group())
```

> 010-1234-4987987567

```python
result_0 = rst_matchObj.group(0)
result_1 = rst_matchObj.group(1)
result_2 = rst_matchObj.group(2)
result_3 = rst_matchObj.group(3)

print("group(0) :", result_0)
print("group(1) :", result_1)
print("group(2) :", result_2)
print("group(3) :", result_3)
```

> group(0) : 010-1234-4987987567 
> group(1) : 010
> group(2) : 1234
> group(3) : 4987987567

* group(0)은 match 함수로 찾은 문자열 전체
* 그 뒤로 괄호로 묶은 순서대로 그룹 번호가 지정됨을 확인할 수 있다.



## re.findall / match / search

#### findall

* 대상 문자열에서 패턴 조건에 맞는 문자열을 찾아서 그 값을 **리스트**로 반환함

* 검색 패턴이 겹치지 않게 탐색함

```python
rst_matchObj1 = re.findall("k2k", "k2k2k2k")
print("findall 검색 결과: ", rst_matchObj1)
```

> findall 검색 결과:  ['k2k', 'k2k']

#### search

* match와 마찬가지로 처음부터 매칭을 하지만, 조건에 맞는 패턴이 발견되면 더 이상 찾지 않는다.
* 물론 search는 발견될 때까지 찾는다
  * 따라서 처음 매칭되는 패턴이 나오면 결과는 match()와 동일하다.

```python
rst_matchObj2 = re.match('k2k', 'k2k2k2k2')
rst_matchObj3 = re.search('k2k', 'k2k2k2k2')

print("match 결과: ", rst_matchObj2)
print("search 결과: ", rst_matchObj3)

#-----------------------

rst_matchObj4 = re.match('k2k', '2k2k2k2k2')
rst_matchObj5 = re.search('k2k', '2k2k2k2k2')

print("match 결과: ", rst_matchObj4)
print("search 결과: ", rst_matchObj5)
```

> match 결과:  <re.Match object; span=(0, 3), match='k2k'>
> search 결과:  <re.Match object; span=(0, 3), match='k2k'>
>
>
> match 결과:  None 
> search 결과:  <re.Match object; span=(1, 4), match='k2k'>





## 정규식 특수문자, 메타문자

* 대문자는 소문자의 반대되는 개념이라고 생각하면 편하다. (비- 를 앞에 붙여서 생각)

### \d

* \d : 정수형(숫자 하나)
* \d+ : 정수형 숫자 하나 이상

### \D

* \d가 아닌 것 > 숫자가 아닌 것 > 문자



### \w

* 숫자와 문자

### \W

* 문자가 아닌 것 > 비문자 > 공백, 개행, 탭, 기호



### \s

* 공백문자, 탭

### \S

* 공백, 탭 재외. 비공백문자



### \b

* 단어(문자)의 경계 > 단어의 앞(시작) 또는 끝을 의미.

### \B

* 단어나 문자의 경계가 아닌 곳 > 비단어문자의 경계



```Python
rst_matchObj = re.findall('\D', 'Korea 20대 청년이여 힘내라~') # K, o, r, e, a ...
print("\\D 검색 결과: ", rst_matchObj) # 공백도 포함이 된다..

print("\\w 검색 결과: ", re.findall('\w', 'Korea 20대 청년이여 힘내라~'))
print("\\W 검색 결과: ", re.findall('\W', 'Korea 20대 청년이여 힘내라~'))

print("\\s 검색 결과: ", re.findall('\s', 'Korea 20대 청년이여 힘내라~'))
print("\\S 검색 결과: ", re.findall('\S', 'Korea 20대 청년이여 힘내라~'))

print("\\b 검색 결과: ", re.findall('\b', 'Korea 20대 청년이여 힘내라~'))
print("\\B 검색 결과: ", re.findall('\B', 'Korea 20대 청년이여 힘내라~'))
```

> \D 검색 결과:  ['K', 'o', 'r', 'e', 'a', ' ', '대', ' ', '청', '년', '이', '여', ' ', '힘', '내', '라', '~']
>
> \w 검색 결과:  ['K', 'o', 'r', 'e', 'a', '2', '0', '대', '청', '년', '이', '여', '힘', '내', '라']
> \W 검색 결과:  [' ', ' ', ' ', '~']
>
> \s 검색 결과:  [' ', ' ', ' ']
> \S 검색 결과:  ['K', 'o', 'r', 'e', 'a', '2', '0', '대', '청', '년', '이', '여', '힘', '내', '라', '~']
>
> \b 검색 결과:  []
> \B 검색 결과:  ['', '', '', '', '', '', '', '', '', '', '', '']





## 정규식 raw string

* re 모듈에서 \는 중요한 의미를 갖는다.

  * \뒤에 다양한 특수문자를 넣기도 하고, string에 \를 이용해 특수문자의 역할을 빼기도 한다.

    > ex) \d 는 십진수를 의미하지만 \\\\d 는 말 그대로 '역슬래쉬 + 문자 d'를 의미하게 된다.

* 파이썬 내부 엔진의 문자열 리터럴 규칙에 따라 문자열에 들어간 \는 짝수개로 들어가게 된다.

  > '\\', '\\\\'      >> '\\\\'
  >
  > '\\\\\\', '\\\\\\\\' >> '\\\\\\\\'

* 따라서 정규식으로 '\\'를 검색하기 위해서는 다음과 같은 논리를 따라야 한다.

  1. 리터럴 엔진에 따라 변경된 '\\'의 개수를 알아내고
  2. 리터럴 엔진에 전달된 개수에 맞게 '\\'를 반복해서 compile 해줘야 한다.
     * 이 때 정규식 엔진에서 컴파일 될 때 리터럴 엔진의 역방향으로 '\\'의 개수가 변환된다.

  글로만 보면 전혀 이해가 가지 않을 것이다. 예제를 보자.

#### 예제 1

```python
text = '\superman'
pattern = re.compile('\superman')
rst = re.search(pattern, text)
print(rst)
```

> 파이썬 내부의 리터럴 엔진 : text = '\\\\superman'
>
> 파이썬 내부의 리터럴 엔진 : pattern = '\\\\superman'
>
> 정규식 엔진 : pattern = '\\superman'
>
> \>> 매칭되지 않음

* 즉, 정규식 엔진에서 파이썬 리터럴 엔진에 맞게 컴파일 되게끔 하도록 pattern을 맞춰주어야 한다.
  * text = '\\\\superman' 이니
    pattern = '\\\\\\\\superman'으로 해야 정규식 내부에서 '\\\\superman'으로 변환이 되서 매칭이 가능해진다.

* 슬슬 감이 잡히는 것 같다. 예제 하나만 더 보자

#### 예제 2

```python
text = '\\\superman' 											# \ 3개
pattern = re.compile('\\\\\\\\superman')  # \ 8개
rst = re.search(pattern, text)
print(rst)
```

> 파이썬 내부의 리터럴 엔진 : text = '\\\\\\\\superman'
>
> 파이썬 내부의 리터럴 엔진 : pattern = '\\\\\\\\\\\\\\\\superman'
>
> 정규식 엔진 : pattern = '\\\\\\\superman'
>
> \>> 매칭 성공.

> MatchObj : <re.Match object; span=(0, 10), match='\\\\\\\\superman'>
> group()  : \\\\superman

* 하지만 matchObject는 '\\\\\\\\superman'
             group() 결과는 '\\\\superman'
  \>> 우리가 원하는 결과가 정확히 나왔다고 하긴 힘들다. 원래 택스트에서 \는 3개니까..



### raw string 모듈의 사용

* raw string은 문자열 앞에 r을 붙여주는 것이다.

  ```python
  text = r'\\abc'
  ```

  이런 식으로 말이다.

  * '\\' 1개를 '\\' 2개의 효과가 나도록 하는 것이다.

    * 다시 말하면 보이는 그대로 컴파일이 되도록, 엔진 내부에서 처리가 되도록 하는 것이다.

    > '\\\\' == r'\\'   일 것이며
    >
    > '\\\\\\\\' == r'\\\\'    일 것이다.
    >
    > 눈에 보이는 그대로 컴파일을 해주게 하니 \ 한개가 \\\\의 기능을 하게 해준다는 것이다.

  * 

* 앞서 살펴본 **예제2**를 raw string을 이용해 확인해보자

  ```python
  text = r'\\\superman'
  pattern = re.compile(r'\\\\\\superman')
  rst = re.search(pattern, text)
  print("MatchObj  :", rst)
  print("group()   :", rst.group())
  ```

  * text와 pattern의 ' 앞에 r을 붙여주기만 하면 된다.

  * 그 상황에서 text \의 개수는 현재 화면에 눈에 보이는 개수 그대로 서칭이 되며,
    pattern에는 text의 개수 * 2 개를 넣어주면 된다.

    > MatchObj : <re.Match object; span=(0, 11), match='\\\\\\\\\\\\superman'>
    > group()  : \\\\\superman

    * 우리가 원하는 대로 group에서 3개의 \가 포함된 \\\\\\superman이 매칭이 된 것을 확인할 수 있다.
    * 직관적으로 2배... 훨씬 편하다.



* 마지막 종합 예제를 확인하자.

  ```python
  text3 = r"superman 단어 앞에다 백슬래쉬를 붙이면 \\superman 이렇게 됩니다."
  pattern3 = re.compile('\\\\superman')
  
  rst3 = re.search(pattern3, text3)
  print("[3] search  :", rst3)
  print("    group() :", rst3.group())
  ```

  > [3]   search  : <re.Match object; span=(27, 36), match='\\superman'>
  >        group() : \superman

  * text3는 raw string임으로 \가 4개가 되어 '\\\\\\\\superman'
    pattern3는 컴파일될 때 \ 2개가 1개로 합쳐짐으로 '\\\\superman'
    * 이후 pattern3는 서칭할 때 '\\superman'으로 서칭이 들어가게 되어 group()에서 \\superman이 나온다.
  * 만약 pattern3에도 raw string을 사용한다면 \\\\superman을 찾을 수 있게되는 것 이다.
