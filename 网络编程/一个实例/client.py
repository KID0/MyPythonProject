#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：client.py

import socket               # 导入 socket 模块

s = socket.socket()         # 创建 socket 对象
host = socket.gethostname() # 获取本地主机名
port = 12344                # 设置端口

# 连接到这个地址
s.connect((host, port))
# s.recv(1024) 接收TCP数据，数据以字符串形式返回，1024为指定要接收的最大数据量
# 这里将接受到的byte码转化为字符串打印出来
print (s.recv(1024).decode())
s.close()  