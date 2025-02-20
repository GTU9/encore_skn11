# pip install mysql-connector-python # python과 mysql을 연결해주는 패키지 설치

import mysql.connector

connection= mysql.connector.connect(
    host='localhost',
    user='ohgiraffers',
    password='ohgiraffers',
    database='menudb'
)

sql='UPDATE tbl_menu SET menu_name=%s ,menu_price=%s  WHERE menu_code=1'
values=('에스프레소칼국수',15000)
# 1번 메뉴의 이름과 가격을 수정

cursor=connection.cursor()
cursor.execute(sql,values)

print(f'{cursor.rowcount}개의 행을 수정하였습니다.')
connection.commit()

cursor.close()

# if connection.is_connected():
#     print('MySQL에 성공적으로 연결되었습니다.')

connection.close()