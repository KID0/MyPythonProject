#!/usr/bin/env python
# Python Network Programming Cookbook -- Chapter - 2
# This program is optimized for Python 2.7.
# It may run on any other version with/without modifications.
# See more: http://docs.python.org/2/library/socketserver.html

'''
1.本教程用到了一个仅在Linux中存在的内置函数，没办法继续了
2.字符串的发送接受编码问题依旧困扰
'''

import os
import socket
import threading
# 在py 3.x 中，SocketServer更名为socketserver
# SocketServer模块提供了可以直接使用的TCP、UDP及其他协议服务器
import socketserver

SERVER_HOST = 'localhost'
SERVER_PORT = 0 # tells the kernel to pick up a port dynamically
BUF_SIZE = 1024
ECHO_MSG = 'Hello echo server!'


class ForkingClient():
	""" A client to test forking server（分支服务器）"""
	# __init__：初始化已实例化后的对象
	def __init__(self, ip, port):
		# Create a socket
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		# Connect to the server
		self.sock.connect((ip, port))
	def run(self):
		""" Client playing with the server"""
		# Send the data to server
		# pid === process id
		current_process_id = os.getpid()
		print ('PID %s Sending echo message to the server : "%s"' % (current_process_id,ECHO_MSG))
		sent_data_length = self.sock.send(bytes(ECHO_MSG,encoding='utf-8'))
		print ("Sent: %d characters, so far..." %sent_data_length)
		# Display server response
		response = self.sock.recv(BUF_SIZE)
		print ("PID %s received: %s" % (current_process_id, response[5:]))
	def shutdown(self):
		""" Cleanup the client socket """
		self.sock.close()

class ForkingServerRequestHandler(socketserver.BaseRequestHandler):
	def handle(self):
		# Send the echo back to the client
		data = self.request.recv(BUF_SIZE)
		current_process_id = os.getpid()
		response = '%s: %s' % (current_process_id, data)
		print ("Server sending response [current_process_id: data] = [%s]" %response)
		self.request.send(response)
		return

# ForkingServer类继承TCPServer和ForkingMixIn类
	# TCPServer实现服务器操作，例如创建套接字、绑定地址和监听进入的连接
	# ForkingMixIn会为每个客户端请求派生一个新进程，异步处理客户端
class ForkingServer(socketserver.ForkingMixIn,socketserver.TCPServer,):
	"""Nothing to add here, inherited everything necessary from parents"""
	pass

def main():
	# Launch the server
	# 实例化一个class，创建一个Server
	server = ForkingServer((SERVER_HOST, SERVER_PORT), ForkingServerRequestHandler)
	# address自动分配好了
	ip, port = server.server_address # Retrieve the port number
	# 线程控制器
	server_thread = threading.Thread(target=server.serve_forever)
	# 设置线程控制器为后台程序
	server_thread.setDaemon(True) # don't hang on exit
	# 开始运行线程控制器
	server_thread.start()

	print ('Server loop running PID: %s' %os.getpid())

	# Launch the client(s)
	client1 = ForkingClient(ip, port)
	client1.run()
	client2 = ForkingClient(ip, port)
	client2.run()
	# Clean them up
	server.shutdown()
	client1.shutdown()
	client2.shutdown()
	server.socket.close()
if __name__ == '__main__':
	main()