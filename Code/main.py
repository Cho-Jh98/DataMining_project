import html_tag, naver_crawl, get_info
import requests
from bs4 import *

print("검색할 키워드를 입력하세요 (',' 로 구분합니다)", end='\n')
key_words = []
key_words = input().split(', ') ### 이거 백퍼 잘못 입력한 경우 있으니까 제한조건 설정 하면 좋을듯?
key = " ".join(key_words)

print("검색할 페이지 수를 입력하세요(숫자로 입력)")
page_num = int(input())

url_list = []
url_list = naver_crawl.naver_crawling(key, page_num)

for url in url_list:
    info = get_info.by_press(url)
    if info is None:
        continue
    sentences = get_info.divide_sentence(info)
    keyword_sentences = get_info.get_keyword(sentences, key_words)

    print('언론사 :', info[0], end='\n')
    print('제목 :', info[1], end='\n')
    print('날짜 :', info[2], end='\n')
    print('작성자 :', info[3], end='\n')
    print('url :', url)
    for sentence in keyword_sentences:
        print(sentence.strip("\n"), end='\n')

    print('-'*80)
