# 정규식으로 문장별로 짜르고 그 안에서 키워드 찾기



## 초기 상황

```python
import requests, re
from bs4 import *
from urllib.request import *
import pandas as pd

test_exl = pd.read_excel('/content/test.xlsx', header = 1, index_col = 0)

print((test_exl.iloc[0][0].split(', ')[0])) # 첫번째 키워드 출력
```

* text_exl 에는 검색시 사용한 키워드와 원하는 문장(target), 그리고 target이 포함된 기사의 url이 저장 되어있다.



## 엑셀 파일에서 URL 가져오기

```python
pattern = re.compile(r'http[s]*://[\w]{1,3}.([\w]+).')

def crawling(matched_pattern, url):
  news_dict = {'ktv' : 0, 'hani' : 1, 'hankyung' : 2, 'bbc' : 3, 'khan' : 4, 'chosun' :5, 'munhwa' : 6, 'sedaily' : 7, 'ajunews' : 8, 'mk' : 9}
  print(news_dict[matched_pattern])

  res = requests.get(url)
  
  soup = BeautifulSoup(res.text, 'html.parser')

  

for i in test_exl.itertuples():
  url = i.url
  
  matchedObj = re.findall(pattern, url)[0]
  crawling(matchedObj, url)
```

* URL을 가져올 함수 crawling을 만들고 url 별 언론사를 딕셔너리로 정리하였다
  * 하지만 뒤에 나올 이유로 이 함수를 사용할 일은 없었다..
* BeautifulSoup을 사용해보았지만 모종의 이유로 404 에러가 떳고, 결국 본문 내용을 txt로 긁어와야 했다..





## 문장 찾기

* 12개의 기사의 본문을 txt파일로 긁었고, 문장별로 매칭시켜줄 정규식을 찾았다.

  ```python
  pattern = re.compile(r'\s*(.+?\D[\.\n]+)\s*')
  ```

  * .+?는 non greedy한 방법으로 모든 문자를 매칭시킨다
  * \D[\\.\\n+] 는 마지막에 올 문자인 . 혹은 개행문자를 매칭한다
  * 앞 뒤로 공백문자를 찾는다

  > 매칭시키게 되는 예시는 다음과 같다.
  >
  > 위 문장을 매칭시킨다고 할 때
  >
  > 매칭시키게 ~ 같 을 .+? 로 매칭시키고
  >
  > 다. 를 \D[\\.\\n]+로 매칭시킨다

  * \\D\\. 을 하는 이유는 기사에 있을 소숫점 표현 때문이다. 해서 마지막에 숫자가 아닌 문자 + . 이 와야 문장의 끝으로 인식시키게 했다.

* 그럼 전체 문장에서 키워드만 뽑아내는 코드를 보자

  ```python
  count = 1 # 기사 개수 세줄 카운트 변수
  res = []
  
  pattern = re.compile(r'\s*(.+?\D[\.\n]+)\s*')
  for i in range(12):
    print(test_exl.iloc[i][0].split(', ')) # 키워드 출력(비교용)
    
    with open("/content/test/test" + str(i+1) + ".txt", encoding = "UTF-8") as infile:
      content = infile.read()
  
    res = re.findall(pattern, content)
    for sentence in res:
      key_list = test_exl.iloc[i][0].split(', ')
  
      for key_word in key_list:
        if key_word in str(sentence.strip()):
          print(sentence.strip('\n'))
          break
    print(count, "-" * 80)
    count += 1
  ```

  * test1~12.txt파일로 되어져 있는 본문 글을 가져와서
  * 먼저 문장별로 분리하기 위해 정규식을 돌린다
    * 이 때 문장별로 list에 들어간다 (findall() 함수의 반환형이 list)
  * 이후 키워드를 하나씩 사용해 if A in B 문을 통해 존재하면 프린트를 해주는 방식으로 진행했다.
    * strip() 함수를 사용해 혹시 있을 공백, 개행문자를 제거해준다.
    * 2개의 키워드가 한 문장에 있을 경우 2번 출력되기 때문에 break함수를 이용해 빠져나온다.
  * 끝



## 앞으로 추가할 점

* 형태소 분석을 통해 키워드를 포함한 다양한 단어도 서칭에 추가
* 별로 의미없는 문장의 경우 제거
  * 이건 좀... 공부가 많이 필요해 보일 듯 하다.
