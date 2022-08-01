#导入模块
from socket import *
#创建TCP服务器端套接字对象
server_socket = socket(AF_INET,SOCK_STREAM)
#绑定端口
server_socket.bind(('',8989))#绑定当前主机下的8989端口
#监听
server_socket.listen()
#接收客户端的链接
client_socket,client_info = server_socket.accept()
#接收客户端发送的消息
recv_data = client_socket.recv(1024)
#输出消息的流程一般采取这种方式
print("接收到%s的消息%s"%(client_info,recv_data.decode("gb2312")))
#关闭连接
client_socket.close()
server_socket.close()