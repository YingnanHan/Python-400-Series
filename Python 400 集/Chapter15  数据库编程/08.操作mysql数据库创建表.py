#导入pymysql模块

import pymysql

#创建连接
conn = pymysql.connect(host="localhost",user="root",password="123456",database="python_db",port=3306)
print(conn)

#创建游标对象
cur = conn.cursor()

#编写创建表的sql语句
sql = """
    create table t_student(
        sno int primary key auto_increment,
        sname varchar(30) not null,
        age int(2),
        score float(3,1)
    )
"""

try:
    #执行创建表的sql
    cur.execute(sql)
    print("创建表成功")
except Exception as e:
    print(e)
    print("创建表失败")
finally:
    #关闭游标
    cur.close()
    #关闭连接
    conn.close()