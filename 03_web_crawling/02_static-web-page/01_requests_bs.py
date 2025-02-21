# pip install requests beautifulsoup4 selenium 터미널 requests beautifulsoup4 selenium 패키지 pip 설치 명령어

# 정적 페이지 웹 스크래핑
# 정적 페이지 : 요청한 url에서 응답받은 html을 그대로 사용한 경우 SSR(Server Side Rendering)

import requests
from bs4 import BeautifulSoup

def web_request(url):
    response=requests.get(url)
    print(response) # <Response [200]>
    print('===========1============')
    print(response.status_code) # 200
    print('===========2============')
    print(response.text)
    return response

# url= 'http://www.naver.com'
# web_request(url)

with open('../html_sample.html','r',encoding='utf-8') as f:
    html = f.read()

bs=BeautifulSoup(html,'html.parser')
# print(bs)
# print('=======================')
# print(type(bs))

def test_find():
    # find 
    tag=bs.find('li') # 맨 처음에 나오는 조건을 만족하는 한가지를 가져옴
    # print(tag)
    # print(type(tag))
        
    # find_all
    tags=bs.find_all('section', {'id' : 'section1'}) # 파일 내 조건에 해당하는 모든 것을 가져옴
    print(tags)
    print(type(tags))
    
test_find()