# pip install mysql-connector-python # python과 mysql을 연결해주는 패키지 설치

import mysql.connector

connection= mysql.connector.connect(
    host='localhost',
    user='ohgiraffers',
    password='ohgiraffers',
    database='menudb'
)

cursor=connection.cursor()

cursor.execute('SELECT menu_code, menu_name, menu_price FROM tbl_menu')
result=cursor.fetchall()

# print(result)
for row in result: # row = 한 행의 결과
    print('menuCode:',row[0],'/','menuName:',row[1],'/','menuPrice: ',row[2])

cursor.close()

# if connection.is_connected():
#     print('MySQL에 성공적으로 연결되었습니다.')

connection.close()