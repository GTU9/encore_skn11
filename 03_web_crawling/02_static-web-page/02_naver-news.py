import requests
from bs4 import BeautifulSoup
from datetime import datetime
from urllib.request import urlretrieve
import os

# 스크랩한 뉴스 정보를 담은 NewsEntry Class
class NewsEntry():
    def __init__(self,title,href,img_path):
        self.title=title
        self.href=href
        self.img_path=img_path

    def __repr__(self):
        return f'NewsEntry\ntitle= {self.title}\nhref= {self.href}\nimg_path= {self.img_path}\n'

# 1. requet -> url 요청
keyword=input('뉴스검색 키워드 : ')
url=f'https://search.naver.com/search.naver?where=news&query={keyword}&sm=tab_tmr&nso=so:r,p:all,a:all&sort=0'

response=requests.get(url)

# 2. html 응답
html=response.text

# 3. BeautifulSoup 객체 생성
bs=BeautifulSoup(html,'html.parser')

# 4. li.bx 반복순회 > .news_content > 두번째 a 태그
news_contents=bs.select('div.news_contents')
# print(len(news_contents))

# 5. href속성 : 링크, text: 뉴스제목
news_list=[]
for i,news_content in  enumerate(news_contents):
    a_tag=news_content.select_one('a.news_tit')
    title=a_tag.text
    href=a_tag['href']

    img_tag=news_content.select_one('img.thumb')
    img_lazysrc=img_tag['data-lazysrc']
    if img_lazysrc.startswith('http'):
        if(not os.path.exists(f'images/{keyword}')): # 경로에 폴더 유무 판단
            os.mkdir(f'images/{keyword}')            # 없을시 폴더 생성
        img_dir=f'images/{keyword}'
        today=datetime.now().strftime('%y%m%d')      # 파일명 생성을 위한 오늘 날짜
        filename=f'{img_dir}/{today}_{i}.jpg'        #파일명 (저장할 파일 확장자까지)
        urlretrieve(img_lazysrc,filename)            # 파일 저장

    news_entry=NewsEntry(title,href,filename)
    news_list.append(news_entry)

# 결과 값 확인
for news_entry in news_list:
    print(news_entry)