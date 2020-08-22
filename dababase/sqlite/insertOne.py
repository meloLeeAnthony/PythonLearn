# coding=utf-8
# 导入模块
import sqlite3

conn = None

# 创建连接
try:
    conn = sqlite3.connect('e:/sqlite3Demo/demo.db')
    print('连接sqlite库成功')
except Exception as e:
    print('连接sqlite库失败：', e)

if conn is not None:
    # 创建游标对象
    cur = conn.cursor()
    # 编写插入sql
    sql = 'insert into t_person(pname,age) values(?,?)'
    try:
        # 执行sql
        cur.execute(sql, ('张三', 24))
        # 提交事务
        conn.commit()
        print('插入数据成功')
    except Exception as e:
        print('插入数据失败：', e)
        conn.rollback()
    finally:
        # 关闭游标连接
        cur.close()
        # 关闭数据库连接
        conn.close()
