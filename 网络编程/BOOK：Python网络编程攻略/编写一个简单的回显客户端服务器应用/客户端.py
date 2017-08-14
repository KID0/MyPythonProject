#!/usr/bin/env python
# Python Network Programming Cookbook -- Chapter – 1
# This program is optimized for Python 2.7. It may run on any
# other Python version with/without modifications.

import socket
import sys
import argparse

host = 'localhost'

def echo_client(port):
	""" A simple echo client """
	# Create a TCP/IP socket
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# Connect the socket to the server
	server_address = (host, port)
	print ("Connecting to %s port %s" % server_address)
	sock.connect(server_address)
	# Send data
	try:
		# Send data
		message = "Test message. This will be echoed"
		print ("Sending %s" % message)
		# 原本这里直接发送了message字符串，然而报错，我们对其进行了二进制编码予以搞定~
		sock.sendall(bytes(message,encoding='utf-8'))
		# Look for the response
		amount_received = 0
		amount_expected = len(message)
		while amount_received < amount_expected:
			# 一次只打印16 bytes
			data = sock.recv(16)
			amount_received += len(data)
			# 这里也出现了编码错误，我们予以修正即可
			print ("Received: %s" %str(data,encoding="utf-8"))
	except socket.error as e:
		print ("Socket error: %s" %str(e))
	except Exception as e:
		print ("Other exception: %s" %str(e))
	finally:
		print ("Closing connection to the server")
		sock.close()

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Socket Server Example')
	parser.add_argument('--port', action="store", dest="port", type=int,required=True)
	given_args = parser.parse_args()
	port = given_args.port
	echo_client(port)