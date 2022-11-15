# -*- coding: utf-8 -*-
#!/usr/bin/env python
import argparse
import random
import datetime
import sys
import pymysql
 
db_host='localhost'
db_port=3306
db_user = 'root'
db_password = 'goback@2022'
db_dbname = 'aibouc'

# MySQL Connection 연결
conn = pymysql.connect(host=db_host, user=db_user, password=db_password,
                       db=db_dbname, charset='utf8')
 
# Connection 으로부터 Dictoionary Cursor 생성
#curs = conn.cursor(pymysql.cursors.DictCursor)
curs = conn.cursor()

id_list = [1,2,3,4]
    
id = 998000
camera_id= 2



# SQL문 실행
for i in range(1 , 300):
    id = id + i
    date_time= datetime.datetime.now()
    equipment_id= random.randrange(1,10)
    min_temp= random.uniform(50,80)
    max_temp=random.uniform(80,90) 
    min_temp_x= random.randrange(100,400)
    min_temp_y = random.randrange(500,800)
    max_temp_x= random.randrange(100,400)
    max_temp_y= random.randrange(500,800)
    raw_img_path= "C:/Users/Goback/Desktop/asd/2022-08-05 181516.png"
    processed_img_path = "C:/Users/Goback/Desktop/asd/2022-08-05 181516.png"
    try:
        sql = "INSERT INTO equipment_temperatures (id, date_time, camera_id, equipment_id, min_temp, max_temp, min_temp_x,min_temp_y,max_temp_x,max_temp_y,raw_img_path,processed_img_path) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        print(sql)
        
        curs.execute(sql,(id, date_time, camera_id, equipment_id, min_temp, max_temp, min_temp_x,min_temp_y,max_temp_x,max_temp_y,raw_img_path,processed_img_path))
        
        conn.commit()
        
    except pymysql.MySQLError as error:
        print('got error {!r}, errno is {}'. format(error,error.args[0]))

