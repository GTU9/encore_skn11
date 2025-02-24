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


# BeautifulSoup = html, xml을 parsing(쪼개서 분석)해서 데이터 추출
bs=BeautifulSoup(html,'html.parser')
# print(bs)
# print('=======================')
# print(type(bs))

def test_find():
    # find : html 태그 및 속성을 dictionary로 조회 (1개만 조회)
    tag=bs.find('li') # 맨 처음에 나오는 조건을 만족하는 한가지를 가져옴
    # print(tag)
    # print(type(tag))
        
    # find_all : html 태그 및 속성을 dictionary로 조회 (전부 조회)
    tags=bs.find_all('section', {'id' : 'section1'}) # 파일 내 조건에 해당하는 모든 것을 가져옴
    print(tags)
    print(type(tags))
    
# test_find()

def test_selector():
    # CSS 선택자로 특정 태그 찾기
    tag=bs.select_one('section#section2')
    # print(tag)
    # print(type(tag))

    tags=bs.select('.section-content')
    print(tags)
    print(type(tags))

# test_selector()

def get_content():
    # id가 section2인 section 태그의 자손  li 태그들을 추출
    # 자식 요소 : section#section2 > h2
    # 후손 요소 : section#section2 li
    tags=bs.select('section#section2 li')
    # for tag in tags:
    #     print(tag)

    for tag in tags:
        print(tag.text)

# get_content()

def get_content2():
    # id가 section1인 section 태그의 자손 h2태그의 '내용', p태그의 '내용' 출력
    h2_tag=bs.select_one('section#section1 > h2')
    print('h2_tag : ',h2_tag)

    p_tags=bs.select('section#section1 > p')
    for p_tag in p_tags:
        print('p_text : ', p_tag)

# get_content2()

def get_content3():
    #자식 태그 조회
    section1_tag=bs.select_one('section#section1')
    h2_tag=section1_tag.select_one('h2')
    # print('h2_tag : ',h2_tag.text)

    p_tags=section1_tag.select('p')
    # print([p_tag.text for p_tag in p_tags])

    children= section1_tag.findChildren()
    print(children)

get_content3()