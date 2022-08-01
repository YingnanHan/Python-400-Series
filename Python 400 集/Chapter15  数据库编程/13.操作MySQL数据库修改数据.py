#导入模块
import pymysql
#创建连接
con=pymysql.connect(host='127.0.0.1',database='python_db',user='root',password='root',port=3306)
#创建游标对象
cur=con.cursor()
#编写修改的sql
sql='update t_student set sname=%s where sno=%s'
#执行sql语句
try:
    cur.execute(sql,('张三丰',1))
    con.commit()
    print('修改成功')
except Exception as e:
    print(e)
    con.rollback()
    print('修改失败')
finally:
    #关闭连接
    con.close()