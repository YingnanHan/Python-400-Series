#查询一条数据

#导入模块
import sqlite3

#创建连接
conn = sqlite3.connect("demo.db")

#创建游标对象
cur = conn.cursor()

#编写sql
sql = "select * from t_person"

try:
    cur.execute(sql)
    #获取结果集
    person_all = cur.fetchone()
    #输出结果集对象
    print(person_all)
    #遍历结果集
    for p in person_all:
        print(p)
except Exception as e:
    print(e)
    print("查询所有数据失败")
finally:
    #关闭连接
    cur.close()