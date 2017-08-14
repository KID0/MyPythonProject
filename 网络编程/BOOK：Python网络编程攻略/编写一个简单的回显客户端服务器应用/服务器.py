#!/usr/bin/env python
# Python Network Programming Cookbook -- Chapter – 1
# This program is optimized for Python 2.7. It may run on any
# other Python version with/without modifications.

import socket
import sys
import argparse

host = 'localhost'
data_payload = 2048
backlog = 5

def echo_server(port):
	""" A simple echo server """
	# Create a TCP socket
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# Enable reuse address/port
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

	# Bind the socket to the port
	server_address = (host, port)
	print ("Starting up echo server on %s port %s" % server_address)
	sock.bind(server_address)

	# Listen to clients, backlog argument specifies the max no. of queued connections
	sock.listen(backlog)
	while True:
		print ("Waiting to receive message from client")
		# 对客户端进行处理
		client, address = sock.accept()
		data = client.recv(data_payload)
		if data:
			print ("Data: %s" %str(data,encoding="utf-8"))
			client.send(data)
			print ("sent %s bytes back to %s" % (str(data,encoding="utf-8"), address))
		# end connection
		client.close()

# 下面这段666
if __name__ == '__main__':
	# 语法分析器？
	parser = argparse.ArgumentParser(description='Socket Server Example')
	parser.add_argument('--port', action="store", dest="port", type=int,required=True)
	given_args = parser.parse_args()
	port = given_args.port
	echo_server(port)