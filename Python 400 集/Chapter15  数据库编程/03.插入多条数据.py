#01.导入模块
import sqlite3
#02.创建连接
conn = sqlite3.connect("demo.db")
#03.创建游标对象
cursor = conn.cursor()
#04.编写SQL语句
sql = "insert into t_person(pname,age) values(?,?) "
#执行SQL
try:
    #执行同样的语句，但是数据不同的时候采用以下函数来执行
    cursor.executemany(sql,[('Sarah',12),('Jack',18),('Sue',12)])
    conn.commit()#提交事务
    print("插入多条数据成功")
except Exception as e:
    print(e)
    conn.rollback()#失败回滚
    print("插入数据失误")
finally:
    #关闭游标连接
    cursor.close()
    #关闭数据库连接
    conn.close()