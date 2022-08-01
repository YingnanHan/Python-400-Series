#导入模块
from socket import socket,AF_INET,SOCK_DGRAM

#创建一个套接字对象
#AF_INET指定套接字是面向网络的
#SOCK_DGRAM指定无连接套接字 也就是UDP链接
udp_socket = socket(AF_INET,SOCK_DGRAM)

#创建信息接收的socket
addr = ("192.168.56.1",8081)#端口号可以根据实际情况设置 网络助手端口

#调用senfto方法发送信息
#键盘接收需要发送的消息
data = input("请输入您所需要发送的消息")
udp_socket.sendto(data.encode('gb2312'),addr)

#关闭套接字
udp_socket.close()