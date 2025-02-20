# pip install mysql-connector-python # python과 mysql을 연결해주는 패키지 설치

import mysql.connector

connection= mysql.connector.connect(
    host='localhost',
    user='ohgiraffers',
    password='ohgiraffers',
    database='menudb'
)

cursor=connection.cursor()

sql='DELETE FROM tbl_menu WHERE menu_code>= %s'
values=(100,) # ','가 없으면 기본 자료형으로 인식하기 때문에 ','를 추가하여 튜플로 인식하게 만들어줘야함
#menu_code가 100번 이상인 메뉴 삭제

cursor.execute(sql,values)

print(f'{cursor.rowcount}개의 행을 삭제하였습니다.')
connection.commit()

cursor.close()


# if connection.is_connected():
#     print('MySQL에 성공적으로 연결되었습니다.')

connection.close()