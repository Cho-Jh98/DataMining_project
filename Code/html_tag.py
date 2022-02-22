import requests, re, pandas
from bs4 import *
from urllib.request import Request, urlopen

"""
    function : get_(PRESS)
    Parameter : URL (string) 
    Return form : (
                    title (string), 
                    date (list -> 입력, 수정 날짜 고려),
                    writer (string),
                    text (list)
                   )

    주어진 기사 URL에서 기사 제목, 입력 및 수정 날짜, 기자, 본문 텍스트를 크롤링하는 함수입니다.
"""


### 동아일보 ###
def get_DONGA(URL):
    donga_html = requests.get(URL)
    soup = BeautifulSoup(donga_html.text, 'html.parser')

    # 제목
    headline = soup.find_all('h1', {'class': 'title'})
    title = headline[0].text  # str, 제목

    # 날짜
    date = soup.find_all('span', {'class': 'date01'})
    date_list = []  # 입력, 수정 날짜
    for day in date:
        date_list.append(day.text)

    # 본문
    body_text = []

    body = soup.find_all('div', {'class': 'article_txt'})
    for sentences in body:
        body_text.append(sentences.text)

    return title, date_list, None, body_text  ## 기자는 없읍니다


### JTBC ###
def get_JTBC(URL):
    jtbc_html = requests.get(URL)

    soup = BeautifulSoup(jtbc_html.text, 'html.parser')

    # 제목
    headline = soup.find_all('h3', {'id': 'jtbcBody'})
    title = headline[0].text

    # 날짜
    published_date = soup.find_all('span', {'class': 'i_date'})[0].text
    modified_date = soup.find_all('span', {'class': 'm_date'})
    if len(modified_date) == 0:
        modified_date = None
    else:
        modified_date = modified_date[0].text
    date_list = [published_date, modified_date]

    # 기자
    writer = soup.find_all('dd', {'class': 'name'})[0].text

    # 본문
    body_text = []

    body = soup.find_all('div', {'id': 'article'})
    for sentences in body:
        body_text.append(str(sentences.text))

    return title, date_list, writer, body_text


### 한겨레 ###
def get_HANI(URL):
    hani_html = requests.get(URL)
    soup = BeautifulSoup(hani_html.text, 'html.parser')
    print(URL)
    # 제목
    title = soup.find_all('span', {'class': 'title'})[0].text

    # 날짜
    date_list = []
    date_time = soup.find_all('p', {'class': 'date-time'})[0].get_text(' ', strip=True)
    date_list.append(date_time)

    # 기자
    name = soup.find_all('div', {'class': 'name'})
    if len(name) == 0:
        text = soup.find_all('div', {'class': 'text'})[0]
        name = text.find_all('strong')
    else:
        name = name[0].find_all('strong')

    if len(name) == 0:
        name = None

    if name is not None:
        name = name[0].text

    # 본문
    body_text = []
    body = soup.find_all('div', {'class': 'text'})

    for sentences in body:
        body_text.append(str(sentences.text))

    return title, date_time, name, body_text


### SBS ###
def get_SBS(URL):
    print(URL)
    sbs_html = requests.get(URL)
    soup = BeautifulSoup(sbs_html.text, 'html.parser')

    # 제목
    headline = soup.find_all('h3', {'id': 'vmNewsTitle'})[0].text

    # 날짜
    date_list = []
    date_time = soup.find_all('span', {'class': 'date'})
    date = date_time[0].find_all('span')[0].text
    date_list.append(date)

    # 기자
    writer = soup.find_all('a', {'class': 'name'})
    if len(writer) == 0:
        writer = '뉴스딱!'
    else:
        writer = writer[0].text

    # 본문
    body = soup.find_all('div', {'class': 'text_area'})

    body_text = []
    for sentences in body:
        body_text.append(sentences.text)

    return headline, date_list, writer, body_text


### KBS ###
def get_KBS(URL):
    kbs_html = requests.get(URL)
    soup = BeautifulSoup(kbs_html.text, 'html.parser')

    # 제목
    headline = soup.find_all('h5', {'class': 'tit-s'})[0].text

    # 날짜
    date_time = soup.find_all('em', {'class': 'date'})
    date = []
    for day in date_time:
        date.append(day.text)

    # 기자
    writer = soup.find_all('p', {'class': 'name'})[0].get_text(' ', strip=True)

    # 본문
    body = soup.find_all('div', {'class': 'detail-body font-size'})
    body_text = []
    for sentences in body:
        body_text.append(str(sentences.text))

    return headline, date, writer, body_text


### MBC ###
def get_MBC(URL):
    mbc_html = requests.get(URL)
    soup = BeautifulSoup(mbc_html.text, 'html.parser')

    # 제목
    headline = soup.find_all('h2', {'class': 'art_title'})[0].text

    # 날짜
    date_time = soup.find_all('span', {'class': 'input'})
    date = [re.sub(r'[\t\r\n]', '', date_time[0].text), date_time[1].text.strip()]  # 작성 날짜, 수정 날짜

    # 기자
    writer = soup.find_all('span', {'class': 'writer'})
    if len(writer) == 0:
        writer = None
    else:
        writer = writer[0].text
    # 본문
    body = soup.find_all('div', {'class': 'news_txt'})
    body_text = []
    for sentences in body:
        body_text.append(str(sentences.text))

    return headline, date, writer, body_text


### 중앙일보 ###
def get_JOONGANG(URL):
    res = urlopen(URL)
    soup = BeautifulSoup(res, 'html.parser')

    head = soup.find_all('header', {'class': 'article_header'})
    body = soup.find_all('article', {'class':'article'})

    # 제목
    headline = head[0].find_all('h1', {'class': 'headline'})[0].get_text().strip()

    # 0: 입력 날짜 / 1: 업데이트 날짜
    date = []
    date_time = head[0].find_all('div', {'class': 'datetime'})[0].find_all('p', {'class': 'date'})
    for p in date_time:
        date.append(p.get_text())

    # 기자
    writer = body[0].find_all('div', {'class': 'byline'})
    if len(writer) == 0:
        writer = body[0].find_all('span', {'class': 'profile_name'})

        if len(writer) == 0:
            writer = None
        else:
            writer = writer[0].text
    else:
        writer = writer[0].text


    # 본문
    article = body[0].find_all('p')
    body_text = []
    for p in article:
        body_text.append(p.text)

    return headline, date, writer, body_text
