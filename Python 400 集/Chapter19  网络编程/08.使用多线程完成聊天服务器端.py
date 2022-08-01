from socket import  *
from threading import  Thread

#保存所有已连接客户端
sockets = []

def main():
    #创建TCP server_socket套接字对象
    server_socket = socket(AF_INET,SOCK_STREAM)
    #绑定本机端口
    server_socket.bind(('',8888))
    #监听
    server_socket.listen()
    #接收客户端的请求
    while True:
        client_socket,client_info = server_socket.accept()
        sockets.append(client_socket)
        #当某一个客户端发起连接的时候开启线程
        #由于线程需要了解当前是谁发来的消息所以需要额外传递参数
        t = Thread(target=readMsg,args=(client_socket,))
        t.start()

def readMsg(client_socket):
    #读取客户端发送来的消息
    while True:
        recv_data = client_socket.recv(1024)
        #如果接收到的消息中结尾是bye，则将该用户从客户端列表中移除
        if recv_data.decode('utf-8').endswith('bye'):
            sockets.remove(client_socket)
            client_socket.close()
            break
        #将消息发送给所有在线的客户端
        #遍历所有在线客户端列表
        if len(recv_data)>0:
            for socket in sockets:
                #给每一个客户发送相同的消息
                socket.send(recv_data)

if __name__ == '__main__':
    main()