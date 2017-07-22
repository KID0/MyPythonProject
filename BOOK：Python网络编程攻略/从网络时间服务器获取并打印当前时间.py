#!/usr/bin/env python
# Python Network Programming Cookbook -- Chapter - 1
# This program is optimized for Python 2.7. It may run on any
# other Python version with/without modifications.

# 通过“网络时间协议”（Network Time Protocol，简称NTP）处理客户端和服务器之间的通信
import ntplib
from time import ctime

def print_time():
	ntp_client = ntplib.NTPClient()
	# 向这个被墙的网站发出一个申请
	response = ntp_client.request('pool.ntp.org')
	# ctime()是一个将获取的时间转换为本地时间的函数
	print (ctime(response.tx_time))

if __name__ == '__main__':
	print_time()