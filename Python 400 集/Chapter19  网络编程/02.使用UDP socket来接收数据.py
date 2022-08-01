#导入模块
from socket import socket,AF_INET,SOCK_DGRAM
#创建UDP套接字
udp_socket = socket(AF_INET,SOCK_DGRAM)
#绑定一个接受消息用的端口
udp_socket.bind(('',8989))#''表示绑定的是本机 端口号是8989
#开始接受消息
recv = udp_socket.recvfrom(1024)#设置可接受的字节数最大为1024个字节
#输出接收到的消息
print("接收到来自{0}的消息{1}:".format(recv[1],recv[0].decode("gb2312")))
#关闭套接字
udp_socket.close()