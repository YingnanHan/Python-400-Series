#导入模块
import pymysql
#创建连接
con=pymysql.connect(host='127.0.0.1',database='python_db',user='root',password='root',port=3306)
#创建游标对象
cur=con.cursor()
#编写删除的sql
sql='delete from t_student where sname=%s'
#执行sql语句
try:
    cur.execute(sql,('张三丰'))
    con.commit()
    print('删除成功')
except Exception as e:
    print(e)
    con.rollback()
    print('删除失败')
finally:
    #关闭连接
    con.close()