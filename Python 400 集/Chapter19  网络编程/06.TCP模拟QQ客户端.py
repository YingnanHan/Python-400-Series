from socket import *
#创建客户端套接字对象
client_socket = socket(AF_INET,SOCK_STREAM)
#调用connect方法与服务器建立链接
client_socket.connect(("192.168.56.1",8888))
while True:
    #客户端发送消息
    msg = input(">>>")
    client_socket.send(msg.encode("utf-8"))
    if recv_data.decode("utf-8") == "bye":
        #遇到特定字符断开连接
        break
    #客户端接收消息
    recv_data = client_socket.recv(1024)
    print("server:",recv_data.decode('utf-8'))