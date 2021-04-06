import  socket

#tcp服务端开发

if __name__ == '__main__':

    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #print(type(tcp_server_socket))
    #print(tcp_server_socket)

    tcp_server_socket.bind(("",9090))
    tcp_server_socket.listen(128)

    client_socket, client_addr = tcp_server_socket.accept()

    print("客户端连接成功，ip:%s  port:%d" % (client_addr[0],client_addr[1]))

    recv_data = client_socket.recv(1024)
    print(recv_data)
    print("客户端说: %s" % recv_data.decode("utf-8"))
    send_data = "服务端已经收到你的数据"
    client_socket.send(send_data.encode("utf-8"))


    client_socket.close()
    tcp_server_socket.close()