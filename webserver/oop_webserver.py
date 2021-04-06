import socket
import os
import threading
import sys



class HttpWebServer(object):
    def __init__(self,port = 8000):
        tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        tcp_server_socket.bind(("", port))
        tcp_server_socket.listen(128)
        self.tcp_server_socket = tcp_server_socket

    @staticmethod
    def handle_client_request(new_socket):
        recv_data = new_socket.recv(4096)
        if len(recv_data) == 0:
            new_socket.close()
            return
        print("============未解码的http请求============")
        print(recv_data)
        print("============未解码的http请求============")
        recv_data_decode = recv_data.decode("utf-8")
        print("============解码后的http请求============")
        print(recv_data_decode)
        print("============解码后的http请求============")
        lst = recv_data_decode.split(" ", 2)
        request_path = lst[1]
        if request_path == "/":
            request_path = "/index.html"

        # with open 关闭文件这步操作不用程序员来完成，系统帮助我们来完成
        try:
            with open("static" + request_path, "rb") as file:  # file就是文件对象
                file_data = file.read()
        except Exception as e:
            response_line = "HTTP/1.1 404 Not Found\r\n"
            response_header = "Server: PWD/1.0\r\n"
            with open("static/error.html", "rb") as file:
                file_data = file.read()
            response_body = file_data
            response = (response_line + response_header + "\r\n").encode("utf-8") + file_data
            new_socket.send(response)
        else:
            # 把数据封装成http响应报文格式的数据
            response_line = "HTTP/1.1 200 OK\r\n"
            response_header = "Server: PWS/1.0\r\n"
            response_body = file_data
            response = (response_line + response_header + "\r\n").encode("utf-8") + response_body
            new_socket.send(response)
        finally:
            new_socket.close()

    def start(self):
        while True:
            new_socket, ip_port = self.tcp_server_socket.accept()
            sub_thread = threading.Thread(target=self.handle_client_request, args=(new_socket,))
            sub_thread.setDaemon(True)
            sub_thread.start()

def main():
    argv_lst = sys.argv
    if (len(argv_lst) != 2):
        print("error! format: python3 text.py port")
        return
    webserver = HttpWebServer(int(argv_lst[1]))
    webserver.start()
if __name__ == '__main__':
    main()


