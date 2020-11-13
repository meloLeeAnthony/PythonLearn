# coding=utf-8
# 导入模块
import sqlite3

# 创建连接
conn = sqlite3.connect('e:/sqlite3Demo/demo.db')
# 创建游标对象
cur = conn.cursor()
# 创建查询sql
sql = 'select * from t_person'
try:
    cur.execute(sql)
    # 获取结果集
    person_all = cur.fetchall()
    print(person_all)
    for person in person_all:
        print(person)
except Exception as e:
    print('查询所有数据失败：', e)
finally:
    # 关闭游标
    cur.close()
    # 关闭连接
    conn.close()
