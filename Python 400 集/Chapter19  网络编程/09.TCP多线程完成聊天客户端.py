from socket import *
from threading import Thread

flag = True

def readMsg(client_socket):
    while flag:
        recv_data = client_socket.recv(1024)
        print("receive:",recv_data.decode('utf-8'))

def writeMsg(client_socket):
    global flag
    while flag:
        msg = input(">>>")
        msg = user_name+" said that "+msg
        client_socket.send(msg.encode('utf-8'))
        #设置输入内容以bye结尾的时候下线
        if msg.endswith('bye'):
            flag = False
            break

#创建客户端套接字对象
client_socket = socket(AF_INET,SOCK_STREAM)
#调用connect连接服务器
client_socket.connect(('192.168.56.1',8888))
user_name = input(">>>请输入用户名:")
#开启一个线程处理客户端的读取消息
t1 = Thread(target=readMsg,args=(client_socket,))
t1.start()
#开启一个线程处理客户端发送消息
t2 = Thread(target=writeMsg,args=(client_socket,))
t2.start()

t1.join()
t2.join()

client_socket.close()