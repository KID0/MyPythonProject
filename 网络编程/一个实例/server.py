# -*- coding: UTF-8 -*-
# 文件名：server.py

import socket               # 导入 socket 模块

s = socket.socket()         # 创建 socket 对象
host = socket.gethostname() # 获取本地主机名
port = 12344                # 设置端口
s.bind((host, port))        # 绑定端口
'''
s.listen()
开始TCP监听。
backlog指定在拒绝连接之前，操作系统可以挂起的最大连接数量。
该值至少为1，大部分应用程序设为5就可以了。
'''
s.listen(5)                 # 等待客户端连接
while True:
	# accept() -> (socket object, address info)
    c, addr = s.accept()     # 建立客户端连接。
    print ('连接地址：', addr)
    '''
	encode():str-->bytes
    decode():bytes-->str
    '''
    # 这里将字符串转化为byte码发送出去
    c.send('欢迎访问菜鸟教程！'.encode())
    c.close()                # 关闭连接