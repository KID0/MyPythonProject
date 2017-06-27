#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 下载文件
# HTTP 头部

# 不知道为什么下载下来的文件内容为空

# attachment为以附件方式下载
# filename=\"down.txt\ 默认保存时的文件名" 
print ("Content-Disposition: attachment; filename=\"download.txt\"")
print()
# 打开文件
fo = open("download.txt", "rb")
str = fo.read();
print (str)
# 关闭文件
fo.close()