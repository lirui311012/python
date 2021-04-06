import  socket

#tcp客户端开发
if __name__ == '__main__':
    
    tcp_client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcp_client_socket.connect(("127.0.0.1",9090))
    data = "你好，我是客户端！"
    tcp_client_socket.send(data.encode("utf-8"))
    res = tcp_client_socket.recv(1024)
    print(res)
    print("收到服务端的数据: %s" % res.decode("utf-8"))

    tcp_client_socket.close()