#这里不是很懂  待研究
import threading
# 创建全局ThreadLocal对象:
local = threading.local()
def process_student():
    # 获取当前线程关联的name:
    student_name = local.name
    print('线程名：%s 学生姓名:%s' % (threading.current_thread().name,student_name))
def process_thread(name):
    # 绑定ThreadLocal的name:
    local.name = name
    process_student()
t1 = threading.Thread(target=process_thread, args=('张三',), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('李四',), name='Thread-B')
t1.start()
t2.start()
