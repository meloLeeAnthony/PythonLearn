# coding=utf-8
# 导入模块
import sqlite3

# 创建连接
con = sqlite3.connect('e:/sqlite3Demo/demo.db')
# 创建游标对象
cur = con.cursor()
# 编写修改的SQL语句
sql = 'update t_person set pname=? where pno=?'
# 执行sql
try:
    cur.execute(sql, ('小a', 1))
    # 提交事务
    con.commit()
    print('修改成功')
except Exception as e:
    print(e)
    print('修改失败')
    con.rollback()
finally:
    # 关闭游标连接
    cur.close()
    # 关闭连接
    con.close()
