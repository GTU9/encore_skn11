import urllib.parse
import urllib.request

client_id='' #naver api - Client ID
client_secret=''       #naver api - Client Secret

encText=urllib.parse.quote('돈까스')

# 요청 URL
# url='https://openapi.naver.com/v1/search/news.json?query='+encText # naver json 요청 api 주소
url='https://openapi.naver.com/v1/search/news.xml?query='+encText # naver xml 요청 api 주소

# Request 객체 생성 -> 헤더 설정
request=urllib.request.Request(url)
request.add_header('X-Naver-Client-Id',client_id) # {애플리케이션 등록 시 발급받은 클라이언트 아이디 값}
request.add_header('X-Naver-Client-Secret',client_secret) # {애플리케이션 등록 시 발급받은 클라이언트 시크릿 값}
 
response=urllib.request.urlopen(request)

print(response.getcode()) # getcode() : 응답 코드 반환, 요청 성공시 200 출력

response_body=response.read() #read() : 응답 내용 반환
print(response_body.decode('utf-8'))