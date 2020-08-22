'''
Created on 2018年10月10日

@author: Administrator
'''
import pymysql as pm

conn = pm.connect("localhost", "root", "meloLee", "python_db")
cursor = conn.cursor()
cursor.execute("select * from t_student")
emp = cursor.fetchone()
print(emp)
print(type(emp))
all = cursor.fetchall()
print(all)
conn.close()
