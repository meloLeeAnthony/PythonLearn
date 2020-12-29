# coding=utf-8
# 导入模块
import sqlite3

# SQL参数
params = []

# 创建连接
conn = sqlite3.connect('e:/sqlite3Demo/demo.db')
# 创建游标对象
cur = conn.cursor()
# 编写插入sql
sql = 'insert into t_person(pname,age) values(?,?)'

for i in range(1, 4):
    params.append(('melo{}'.format(i), i))

try:
    # 执行插入多条数据的sql
    cur.executemany(sql, params)
    # 提交事务
    conn.commit()
    print('插入多条数据成功')
except Exception as e:
    print('插入多条数据失败：', e)
    conn.rollback()
finally:
    # 关闭游标连接
    cur.close()
    # 关闭数据库连接
    conn.close()
