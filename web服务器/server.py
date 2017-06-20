# 参考来源：http://python.jobbole.com/81524/

# 网络编程应该使用这个模块
import socket
 
HOST, PORT = '', 8888

# 创建一个socket
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
# 最多可以同时接受一个客户端的连接申请
listen_socket.listen(1)
print('Serving HTTP on port %s ...' % PORT)

while True:
    # 在浏览器输入网址就是发送客户端请求
    client_connection, client_address = listen_socket.accept()
    # 1024指缓冲区的大小
    request = client_connection.recv(1024)
    print(request)
    
    # 不知道为什么server发送的信息浏览器没有收到
    http_response = """
HTTP/1.1 200 OK
 
Hello, World!
"""
    http_response_1 = http_response.encode(encoding='utf-8')

    client_connection.sendall(http_response_1)
    client_connection.close()