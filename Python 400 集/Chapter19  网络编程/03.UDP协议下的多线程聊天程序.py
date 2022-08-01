#导入模块
from socket import *
from threading import *

#创建UDP套接字对象
udp_socket = socket(AF_INET,SOCK_DGRAM)
#绑定本机和端口
udp_socket.bind(('',8989))
#定义接收任务
def recv_func():
    while True:
        # 使用udp接收数据的时候要使用recvfrom函数否则会出现意料之外的错误
        recv_data = udp_socket.recvfrom(1024)
        print(">>%s:%s"%(recv_data[1],recv_data[0].decode("gb2312")))

#定义发送任务
def send_func():
    while True:
        addr = ("192.168.56.1",8080)#发送到网络助手的8080端口上·
        data = input("<<:")
        udp_socket.sendto(data.encode("gb2312"),addr)

if __name__ == '__main__':
    #创建两个线程
    t1 = Thread(target=send_func)
    t2 = Thread(target=recv_func)
    t1.start()
    t2.start()
    t1.join()
    t2.join()