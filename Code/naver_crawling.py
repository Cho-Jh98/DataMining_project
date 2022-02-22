from bs4 import *
from urllib.request import Request, urlopen
import requests, re, pandas, random

def naver_crawling(key, page_num):
    url = 'https://search.naver.com/search.naver'
    url_list = []
    
    for page in range(page_num) :
        payload = {'where' : 'news', 'sm' : 'tab_pge', 'query' : key, 'start' : str(page) + '1'}
        
        res = requests.get(url, params=payload)
        soup = BeautifulSoup(res.text, 'html.parser')
        
        news_list = soup.find_all('ul', {'class' : 'list_news'})[0].find_all('a', {'class' : 'news_tit'})
        sub_list = soup.find_all('ul', {'class' : 'list_cluster'})
        
        for news in news_list:
            url_list.append(news['href'])
        for cluster in sub_list:
            news = cluster.find_all('a', {'class' : 'elss sub_tit'})
            for i in news:
                url_list.append(i['href'])
        
    return url_list

if __name__ == '__main__':
    
    print(naver_crawling('세금', 10))