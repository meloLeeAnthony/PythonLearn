# coding=utf-8
# 导入模块
import sqlite3

# 创建连接
con = sqlite3.connect('e:/sqlite3Demo/demo.db')
# 创建游标对象
cur = con.cursor()
# 编写删除数据的SQL语句
sql = 'delete from t_person where pno=?'
# 执行sql
try:
    # parameters are of unsupported type： 参数必须是元组类型，所以必须要加逗号
    cur.execute(sql, (3,))
    # 提交事务
    con.commit()
    print('删除成功')
except Exception as e:
    print(e)
    print('删除失败')
    con.rollback()
finally:
    # 关闭连接
    con.close()
