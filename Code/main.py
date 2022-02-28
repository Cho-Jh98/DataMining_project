import html_tag, naver_crawl, get_info
import requests
from bs4 import *

print("검색할 키워드를 입력하세요 (스페이스 로 구분합니다)", end='\n')
key = input() ### 이거 백퍼 잘못 입력한 경우 있으니까 제한조건 설정 하면 좋을듯?

print("기사 안에서 찾고싶은 단어를 입력하세요 (,로 구문합니다)")
key_words = input().split(', ')

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
    
    if( len(keyword_sentences) == 0 ): # 매칭된 키워드가 없을경우 다음 기사로
        continue
    print('-' * 80)
    print('언론사 :', info[0], end='\n')
    print('제목 :', info[1], end='\n')
    print('날짜 :', end=' ')
    if len(info[2]) == 1:
        print(info[2][0])
    else:
        for i in range(len(info[2])):
            print(info[2][i])
    print('작성자 :', info[3], end='\n')
    print('url :', url)

    for sentence in keyword_sentences:
        print(sentence.strip("\n"), end='\n')
