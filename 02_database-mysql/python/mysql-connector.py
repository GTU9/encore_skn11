# pip install mysql-connector-python # python과 mysql을 연결해주는 패키지 설치

import mysql.connector

connection= mysql.connector.connect(
    host='localhost',
    user='ohgiraffers',
    password='ohgiraffers',
    database='menudb'
)

if connection.is_connected():
    print('MySQL에 성공적으로 연결되었습니다.')

connection.close()