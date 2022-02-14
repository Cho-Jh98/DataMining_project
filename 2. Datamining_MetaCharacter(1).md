# re 모듈 메타문자



## 1. \d 정수형을 표현하는 메타문자

* 먼저 파이썬과 정규식에서 '\\'를 해석하는 방법에 차이가 있다는 점을 알아야 한다.

  * 파이썬은 '\\'를 일반 문자로 해석
  * 정규식은 '\\'를 특수한 문자(메타문자)로 해석

* 따라서 아래와 같은 결과가 나타난다.

  ```python
  import re
  
  rst_matchObj1 = re.search(r'a\\d', '여기에 긴 문자열이 있고 이런 a\\d 문자열을 검색하고자 한다면')
  print('출력결과 :', rst_matchObj1.group())
  ```

  > 출력결과 : a\d

  * text(a\\\\d) = 'a\d' 로 출력
  * pattern(a\\\\d) 도 마찬가지로 'a\d' 로 컴파일 되기 때문



### 정수 찾기 vs 문자열 \\d 찾기

* 정규식에서 \\d는 정수를 의미한다. 숫자 하나하나를 다 찾아버린다.

  ```python
  text = '정규식에서 \d는 숫자를 의미한다. 숫자란 123, 456, 789 이런걸 말한다.'
  pattern1 = re.compile(r'\d')
  
  rst_matchList1 = re.findall(pattern1, text)
  print(rst_matchList1)
  ```

  > ['1', '2', '3', '4', '5', '6', '7', '8', '9']

  * 역시나 list로 반환되는 것을 확인할 수 있다.



* 만약 숫자가 아닌 문자 그대로의 \\d 를 찾고 싶다면 패턴 컴파일에 raw string을 적용하면 된다.

  ```python
  text = r'정규식에서 \d는 숫자를 의미한다. 숫자란 123, 456, 789 이런걸 말한다.'
  pattern2 = re.compile(r'\\d')
  
  rst_matchList = re.findall(pattern, text)
  print(rst_matchList)
  ```

  > \d

  * 이 전에 살펴본 것 처럼 택스트와 패턴 모두 raw string을 적용하고, \의 개수를 2배로 맞춰주면 된다.

  * raw string을 사용하지 않는다면 아래와 같이 패턴을 설정하자..(근데 굳이?)

    ```python
    pattern = re.compile('\\\\d')
    ```

    > 정말 굳이긴 하다. 뒤로 가면 볼 수 있듯이 raw string은 그냥 하는게 편하다.



### 정수를 찾는 개수 설정

* 숫자 3개와 콤마(,) 구성을 찾는다면? 단, 콤마가 없는 경우도 찾아야 한다.

  ```python
  text = "돈을 0~9로 표현할 땐, 3자리마다 콤마(,)를 찍어준다. 예를 들면 123,456,789 이렇게."
  pattern1 = re.compile(r"\d{3},|\d{3}") # {} 안에 앞서 적은 메타문자의 반복 횟수를 넣는다.
  
  rst_matchList = re.findall(pattern1, text)
  print(rst_matchList)
  ```

  > ['123,', '456,', '789']

  * {}는 바로 앞에 적인 문자나 메타문자의 반복 횟수를 의미한한다.

  * | 는 or의 개념으로 앞선 문자열 패턴부터 검색을 하고, 뒤에 나온 문자열은 나중에 한다.

    > C에서 배우는 and, or 연산과 같은 개념임



### 메타문자 |, w, +

* 앞서 한번씩 본 메타문자를 활용해보자.

  ```python
  text = "red box, blue box, yellow box, huge tissue, thick book, white phone"
  pattern = re.compile(r"\w+ box|w+ tissue|w+ phone")
  
  rst_matchList = re.findall(pattern, text)
  print(rst_matchList)
  ```

  > ['red box', 'blue box', 'yellow box', 'tissue', 'phone']

  * 문자열 + 공백 + ('box' or 'tissue' or 'phone') 을 찾는 패턴이 되겠다.

  * 아래와 같은 패턴은 우리가 원하는 결과를 가져다주지 않는다.

    ```python
    pattern = re.compile(r"\w+ [box|tissue|phone]+")
    pattern = re.compile(r"\w+ box|tissue|phone")
    ```

    이유는 찬찬히 생각해보자.



### 숫자, 문자의 범위 지정

* 숫자나 문자의 범위 지정이 가능하다.

* 사용하는 메타문자는 '-' 이다. 아래와 같이 사용하면 된다.

  ```python
  text = "123, 456, 789"
  pattern = re.compile(r'[0-5]')
  rst_matchList = re.findall(pattern, text)
  print(rst_matchList)
  ```

  > ['1', '2', '3', '4', '5']

  * 패턴은 0~5 사이의 숫자 하나만 들어가면 된다는 의미의 메타문자를 사용하였다.

    * '[]' 역시 or의 개념으로 사용한다.

  * 아래 코드는 3자리씩 끊어서 출력하는 방법이다.. 참고만 해두자

    ```python
    cnt = 0
    for i in rst_matchList:
      if cnt == 0:
        print('4)', i, end=' ') # 4)는 몇번째 문자열인지 알려주는 것으로 사용자 임의로 변경 가능.
      else:
        print(i, end=' ')
      cnt += 1
    ```

    > 4\) 123 456 789 



## 2. \b, \B 경계를 표현하는 메타문자

* \b는 단어와 단어 사이의 경계지점을 의미한다.

  * 특수문자로 표현된 단어(공백으로 구분됨)의 경우는 포함하지 않는다.

    ex) '~~ ### !!!' 와 같은 문자열은 \b로 검색해도 결과는 0이다. 

  * 이 때 단어의 시작과 끝을 포함하며, 문장의 시작과 끝을 포함한다

    물론, 이 때 문장의 시작과 끝은 문자형이어야 한다.

* \B는 단어의 경계가 아닌 문자의 경계를 의미한다.

```python
rst_list1 = re.findall(r'\b', "welcom to seoul.") # 6개
rst_list2 = re.findall(r'\B', "welcom to seoul.") # 11개
rst_list3 = re.findall(r'\B', "Welcome to Seoul.") # 12개
# \B는 알파벳 문자 사이 사이 경계의 개수를 반환한다
print(r'\b의 결과 :', len(rst_list1), '개')
print(r'\B의 결과 :', len(rst_list2), '개')
print(r'\B의 결과 :', len(rst_list3), '개')
```

> \b의 결과 : 6 개 
> \B의 결과 : 11 개
> \B의 결과 : 12 개



* 좀 더 긴 예시를 보면 다음과 같다.

  ```python
  print(len(re.findall(r'\b', "Every single Korean should be wering a mask when they...")))
  print(len(re.findall(r'\B', "Every single Korean should be wering a mask when they...")))
  ```

  * \b의 경우 단어가 총 10개로 양 끝 경계는 총 20개로 나온다.
  * \B의 경우 문자 사이사이의 경계로 총 37개이다

  > 20
  >
  > 37

* 다만 특수문자는...

  * 문자가 아니기에 양쪽 끝은 \b로 탐색이 되지 않는다.
  * 반면 공백을 포함해서 모든 특수문자 사이와 양쪽 끝은 \B로 탐색이 가능하다.
  * 다만 햇갈릴 수 있는게 공백이 문자 사이에 있을 때는 공백은 특수문자로 취급되지 않는다.

  ```python
  print(len(re.findall(r'\b', "~~")))
  print(len(re.findall(r'\B', "~~")))
  print(len(re.findall(r'\b', " ~~ ")))
  print(len(re.findall(r'\B', " ~~ ")))
  print(len(re.findall(r'\b', "~ sdf sDF ~")))
  print(len(re.findall(r'\B', "~ sdf sDF ~")))
  ```

  > 0
  >
  > 3
  >
  > 0
  >
  > 5
  >
  > 4
  >
  > 8



### \b, \B를 이용해 단어 찾기



* kor에는 매칭이 되지만, korea, korean에는 매칭이 되지 않는 패턴
  * 다시말해 'kor'에만 매칭이 되는 패턴ㅇ

* 잘못 만든 패턴

  ```python
  text1 = 'Qeustion) kor에는 매칭이 되지만, korea, korean에는 매칭이 되지 않는 패턴'
  pattern1 = re.compile(r'[kor]')
  
  rst_matchList1 = re.findall(pattern1, text1)
  print(rst_matchList1)
  ```

  > ['o', 'k', 'o', 'r', 'k', 'o', 'r', 'k', 'o', 'r'] 

  * [kor] 이라 하면 k 또는 o 또는 r 에 맞는 모든 문자열을 매칭시킨다.

  

* 앞서 배운 \b를 이용하면 된다.

  * \b는 문자의 앞 뒤 공백을 의미하기에, 이를 패턴에 적용시키면 다음과 같은 결과를 얻을 수 있다.

    ```python
    text1 = 'Qeustion) kor에는 매칭이 되지만, korea, korean에는 매칭이 되지 않는 패턴'
    
    pattern8 = re.compile(r'\bkor\b') # ' kor '
    rst_matchList8 = re.findall(pattern8, text1)
    print(rst_matchList8)
    ```

    > [ 'kor' ]

    * 앞 뒤 공백이 포함되어있는 kor을 검색하는 것과 같기 때문에 단어 'kor'을 검색할 수 있다.

  * 만약 여기서 kor이 포함된 단어 전체를 검색하고자 한다면

    ```python
    text1 = 'Qeustion) kor에는 매칭이 되지만, korea, korean에는 매칭이 되지 않는 패턴'
    
    pattern9 = re.compile(r'kor\w*', re.I)
    # pattern9 = re.compile(r'\bkor\w*\b', re.I)
    rst_matchList9 = re.findall(pattern9, text1)
    print(rst_matchList9)
    ```

    > [ 'kor', 'korea', korean에는 ]

    * kor 이후 어떤 문자이든 0개 이상이 오면 매칭이 되는 패턴이다.

  

  #### 번외

  * 위 택스트에서 korea, korean만 매칭을 시키고 싶다면

    ```python
    text1 = 'Qeustion) kor에는 매칭이 되지만, korea, korean에는 매칭이 되지 않는 패턴'
    
    # pattern7 = re.compile(r'korea|korean')
    pattern7 = re.compile(r'korean|korea') # 긴 패턴을 먼저 써주어야 한다.
    
    # pattern7 = re.compile(r'korean|korea|kor', re.I)
    rst_matchList7 = re.findall(pattern7, text1)
    print(rst_matchList7)
    ```

    > [ 'korean', 'korea' ]

    * 여기서 주의할 점은 긴 패턴부터 써야 한다는 것이다(겹치는 것이 있을 때)
    * 그렇지 않으면 짧은 패턴으로만 매칭이되어버린다.



### 주어진 택스트에서 3개 또는 5개의 문자로 이루어지니 단어 찾기

* []와 {}, 그리고 - 메타문자를 사용하면 된다.

  ```python
  text1 = 'Qeustion) I have a feeling that house is not great for our family'
  
  pattern1 = re.compile(r'\b[a-zA-z]{3}\b|\b[a-zA-z]{5}\b')
  rst_matchList1 = re.findall(pattern1, text1)
  print(rst_matchList1)
  ```

  > ['house', 'not', 'great', 'for', 'our']

  * []안에 a~z, A~Z 범위의 문자 아무 문자나 3번 반복되면 그걸 찾는 패턴이다.

#### 번외

* 영어만 찾는다면?

  ```python
  text1 = 'NoSpacesInString'
  pattern2 = re.compile(r'^[a-z]+$', re.I) # 처음과 끝을 표시
  # pattern2 = re.compile(r'\b[a-zA-Z]+\b')
  # pattern2 = re.compile(r'\b[a-zA-Z0-9]+\b')
  
  rst_matchList2 = re.findall(pattern2, text1)
  print(rst_matchList2)
  ```

  > [ 'NoSpacesInString' ]

  * ^와 $는 처음과 끝을 표시한다.
    * 즉 공백이 없어야 한다.
  * 아래 패턴도 동일한, 혹은 숫자를 포함한 패턴이다.
    * 아이디나, 패스워드를 받을 때 쓰면 좋을듯..?

* 3글자 이상의 단어를 찾는다면?

  ```python
  text1 = 'Qeustion) kor 단어는 매칭이 되지만, Korea 또는 korean에는 매칭이 안되는 패턴은? a ab abc abcd abcde abcdef ab1'
  
  pattern3 = re.compile(r'\b[a-zA-z]{3,}', re.I)
  rst_matchList3 = re.findall(pattern3, text1)
  print(rst_matchList3)
  ```

  > ['Qeustion', 'kor', 'Korea', 'korean', 'abc', 'abcd', 'abcde', 'abcdef']

  * 파이썬 배열 문법과 비슷하게 콤마(,)를 이용해주면 된다.
    * 3개 이상이면 {3,}
    * 범위를 표현하고 싶으면 {3,5}
  * 주의할 점은 {} 안에 공백이 있으면 메타문자가 아닌 일반 문자열처럼 나타날 수 있다.



































