#导入模块
import pymysql
#创建连接
con=pymysql.connect(host='localhost',password='root',user='root',port=3306,database='python_db')
#创建游标对象
cur=con.cursor()
#编写插入数据的sql
sql='insert into t_student(sname,age,score) values(%s,%s,%s)'
try:
    # 执行sql
    cur.executemany(sql,[('小明',19,99.8),('小红',18,99.9),('晓丽',18,99.8),('小花',19,99.6)])
    #提交事务
    con.commit()
    print('插入成功')
except Exception as e:
    print(e)
    con.rollback()
    print('插入失败')
finally:
    #关闭连接
    con.close()
