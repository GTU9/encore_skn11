# pip install mysql-connector-python # python과 mysql을 연결해주는 패키지 설치

import mysql.connector

connection= mysql.connector.connect(
    host='localhost',
    user='ohgiraffers',
    password='ohgiraffers',
    database='menudb'
)

cursor=connection.cursor()

sql='INSERT INTO tbl_menu(menu_name,menu_price, category_code, orderable_status) VALUES (%s,%s,%s,%s)'
values=('에스프레소쌀국수',12000,4,'Y')

cursor.execute(sql,values)

print(f'{cursor.rowcount}개의 행을 삽입하였습니다.')
connection.commit()

cursor.close()

# if connection.is_connected():
#     print('MySQL에 성공적으로 연결되었습니다.')

connection.close()