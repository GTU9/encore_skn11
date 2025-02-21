import urllib.request
import json
import mysql.connector


client_id='' #naver api - Client ID
client_secret=''       #naver api - Client Secret

# 검색어
searchText=urllib.parse.quote('소나기')  

# url 및 헤더 설정
url='https://openapi.naver.com/v1/search/book.json?query=' + searchText + '&display=100' # naver json 요청 api 주소, 최대 100개의 데이터를 가져옴
request=urllib.request.Request(url)
request.add_header('X-Naver-Client-Id',client_id) # {애플리케이션 등록 시 발급받은 클라이언트 아이디 값}
request.add_header('X-Naver-Client-Secret',client_secret) # {애플리케이션 등록 시 발급받은 클라이언트 시크릿 값}

# API 요청 및 결과값 json 변환 (dictionary)
response=urllib.request.urlopen(request)
response_body=response.read()
response_body=json.loads(response_body)
# print(response_body)

book_list = response_body['items']

# DB 연결 객체 생성
connection=mysql.connector.connect(
    host='localhost',
    user='ohgiraffers',
    password='ohgiraffers',
    database='bookdb',
)

# sql 수행을 위한 cursor
cursor=connection.cursor()
sql='INSERT INTO naver_book(book_title, book_image, author, publisher, isbn, book_description, pub_date) VALUES(%s, %s, %s, %s, %s, %s, %s)'

# 받아온 정보만큼 sql 수행
for book_Info in book_list:
    values=(book_Info['title'], book_Info['image'], 
            book_Info['author'], book_Info['publisher'], 
            book_Info['isbn'], book_Info['description'], 
            book_Info['pubdate'])
    cursor.execute(sql, values)

# 데이터베이스 커밋 (반영)
connection.commit()

# cursor 및 연결 객체 종료 (반납)
cursor.close()
connection.close()