from socket import *

#创建服务器TCP端套接字对象
server_socket = socket(AF_INET,SOCK_STREAM)
#绑定端口
server_socket.bind(('',8888))#绑定本机8888号端口
#对8888号端口进行监听
server_socket.listen()
#等待客户端的链接
client_socket,client_info = server_socket.accept()
while True:
    #服务器端接受客户端消息
    recv_data = client_socket.recv(1024)
    print("client:",recv_data.decode("utf-8"))
    if recv_data.decode("utf-8") == "bye":
        #遇到特定字符断开连接
        break
    #服务器端发送给客户端消息
    msg = input(">>>")
    client_socket.send(msg.encode("utf-8"))
client_socket.close()
server_socket.close()