#!/usr/bin/env python
# Python Network Programming Cookbook -- Chapter - 2
# This program is optimized for Python 2.7.
# It may run on any other version with/without modifications.

# 参考教程：http://www.cnblogs.com/hazir/p/python_socket_programming.html
# 本程序无法正常运行，原因不知啊

import select
import socket
import sys
import signal
import pickle
import struct
import argparse

SERVER_HOST = 'localhost'
CHAT_SERVER_NAME = 'server'

# Some utilities
def send(channel, *args):
    buffer = cPickle.dumps(args)
    value = socket.htonl(len(buffer))
    size = struct.pack("L",value)
    channel.send(size)
    channel.send(buffer)

def receive(channel):
    size = struct.calcsize("L")
    size = channel.recv(size)
    try:
        size = socket.ntohl(struct.unpack("L", size)[0])
    except struct.error as e:
        return ''
    buf = ""
    while len(buf) < size:
        buf = channel.recv(size - len(buf))
    return cPickle.loads(buf)[0]


class ChatServer(object):
    """ An example chat server using select """
    # backlog=5  最多同时连接五台客户端
    def __init__(self, port, backlog=5):
        self.clients = 0
        self.clientmap = {}
        self.outputs = [] # list output sockets

        '''
        函数 socket.socket 创建一个 socket，返回该 socket 的描述符，将在后面相关函数中使用。
        该函数带有两个参数：
            1.Address Family：可以选择 AF_INET（用于 Internet 进程间通信） 
            或者 AF_UNIX（用于同一台机器进程间通信）
            2.Type：套接字类型，可以是 SOCKET_STREAM（流式套接字，主要用于 TCP 协议）
            或者SOCKET_DGRAM（数据报套接字，主要用于 UDP 协议）
        '''
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        '''
        默认的socket选项不够用的时候，就必须要使用setsockopt来调整。
        就是使用socket.setsockopt(level,optname, value)
        有三个参数：
            level：选项定义的层次。支持SOL_SOCKET、IPPROTO_TCP、IPPROTO_IP和IPPROTO_IPV6。
            optname：需设置的选项。
            value：设置选项的值。
        '''
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # 将server绑定在这个adress
        self.server.bind((SERVER_HOST, port))
        print ('Server listening to port: %s ...' %port)
        # 开始监听啦
        self.server.listen(backlog)

        # 以使用signal模块捕获用户的中断操作
        # 信号处理方法捕获从键盘输入的中断信号后，关闭所有输出套接字
        signal.signal(signal.SIGINT, self.sighandler)
        
    def sighandler(self, signum, frame):
        """ Clean up client outputs"""
        # Close the server
        print ('Shutting down server...')
        # Close existing client sockets
        for output in self.outputs:
            output.close()            
        self.server.close()

    def get_client_name(self, client):
        """ Return the name of the client """
        # clientmap是一个字典
        info = self.clientmap[client]
        host, name = info[0][0], info[1]
        # 用@将name，host连接起来
        return '@'.join((name, host))
         
    def run(self):
        # stdin：标准输入
        # 输入参数是聊天室服务器套接字stdin
        inputs = [self.server, sys.stdin]
        self.outputs = []
        running = True
        while running:
            try:
                # 调用select.select()方法后得到三个列表：可读套接字、可写套接字和异常套接字
                readable, writeable, exceptional = select.select(inputs, self.outputs, [])
            except select.error as e:
                break
            
            # 聊天室服务器只关心可读套接字，其中保存了准备被读取的数据
            for sock in readable:
                '''
                如果可读套接字是服务器本身，表示有一个新客户端连到服务器上了，
                服务器会读取客户端的名字，将其广播给其他客户端
                '''
                if sock == self.server:
                    # handle the server socket
                    client, address = self.server.accept()
                    print ("Chat server: got connection %d from %s" % (client.fileno(), address))
                    # Read the login name
                    cname = receive(client).split('NAME: ')[1]
                    
                    # Compute client namber and send back
                    self.clients += 1
                    send(client, 'CLIENT: ' + str(address[0]))
                    inputs.append(client)
                    self.clientmap[client] = (address, cname)
                    # Send joining information to other clients
                    msg = "\n(Connected: New client (%d) from %s)" % (self.clients, self.get_client_name(client))
                    for output in self.outputs:
                        send(output, msg)
                    self.outputs.append(client)

                elif sock == sys.stdin:
                    # handle standard input
                    junk = sys.stdin.readline()
                    running = False
                else:
                    # handle all other sockets
                    '''
                    这个聊天室服务器也能处理其他客户端套接字的输入，
                    转播客户端直接传送的数据，还能共享客户端进入和离开聊天室的信息。
                    '''
                    try:
                        data = receive(sock)
                        if data:
                            # Send as new client's message...
                            msg = '\n#[' + self.get_client_name(sock) + ']>>' + data
                            # Send data to all except ourself
                            for output in self.outputs:
                                if output != sock:
                                    send(output, msg)
                        else:
                            print ("Chat server: %d hung up" % sock.fileno())
                            self.clients -= 1
                            sock.close()
                            inputs.remove(sock)
                            self.outputs.remove(sock)

                            # Sending client leaving information to others
                            msg = "\n(Now hung up: Client from %s)" % self.get_client_name(sock)
                            for output in self.outputs:                                
                                send(output, msg)                                
                    except socket.error as e:
                        # Remove
                        inputs.remove(sock)
                        self.outputs.remove(sock)
        self.server.close()


class ChatClient(object):
    """ A command line chat client using select """

    def __init__(self, name, port, host=SERVER_HOST):
        self.name = name
        self.connected = False
        self.host = host
        self.port = port
        # Initial prompt
        self.prompt='[' + '@'.join((name, socket.gethostname().split('.')[0])) + ']> '
        # Connect to server at port
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((host, self.port))
            print ("Now connected to chat server@ port %d" % self.port)
            self.connected = True
            # Send my name...
            send(self.sock,'NAME: ' + self.name) 
            data = receive(self.sock)
            # Contains client address, set it
            addr = data.split('CLIENT: ')[1]
            self.prompt = '[' + '@'.join((self.name, addr)) + ']> '
        except socket.error as e:
            print ("Failed to connect to chat server @ port %d" % self.port)
            sys.exit(1)

    def run(self):
        """ Chat client main loop """
        while self.connected:
            try:
                sys.stdout.write(self.prompt)
                sys.stdout.flush()
                # Wait for input from stdin and socket
                readable, writeable,exceptional = select.select([0, self.sock], [],[])
                for sock in readable:
                    if sock == 0:
                        data = sys.stdin.readline().strip()
                        if data: send(self.sock, data)
                    elif sock == self.sock:
                        data = receive(self.sock)
                        if not data:
                            print ('Client shutting down.')
                            self.connected = False 
                            break
                        else:
                            sys.stdout.write(data + '\n')
                            sys.stdout.flush()
                            
            except KeyboardInterrupt:
                print (" Client interrupted. """)
                self.sock.close()
                break


if __name__ == "__main__":
    # 启动服务需要额外的参数
    parser = argparse.ArgumentParser(description='Socket Server Example with Select')
    parser.add_argument('--name', action="store", dest="name", required=True)
    parser.add_argument('--port', action="store", dest="port", type=int, required=True)

    given_args = parser.parse_args() 
    port = given_args.port
    name = given_args.name
    if name == CHAT_SERVER_NAME:
        server = ChatServer(port)
        server.run()
    else:
        client = ChatClient(name=name, port=port)
        client.run()
    
