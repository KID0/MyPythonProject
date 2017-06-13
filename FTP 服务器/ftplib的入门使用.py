#!/usr/bin/python
#-*- coding:utf-8 -*- 

#加载ftp模块
from ftplib import FTP   

# 实例化一个客户端
ftp=FTP()
#打开调试级别2，显示详细信息
ftp.set_debuglevel(2)   
#连接的ftp sever和端口，这两个值都需要设置
ftp.connect("IP","port") 
#连接的用户名，密码
ftp.login("user","password")
#打印出欢迎信息
printftp.getwelcome()
# 命令CWD改变工作目录是改变当前所在位置
ftp.cwd("xxx/xxx")
#设置的缓冲区大小 
bufsize=1024       
#这是需要下载的文件
filename="filename.txt" 
#以写模式在本地打开文件
file_handle=open(filename,"wb").write
#接收服务器上文件并写入本地文件
ftp.retrbinaly("RETR filename.txt",file_handle,bufsize)
#关闭调试模式
ftp.set_debuglevel(0)   
#退出ftp
ftp.quit
#显示目录下文件信息         
ftp.dir()         
#新建远程目录
ftp.mkd(pathname)     
#显示整个路径名 Print Working Directory
ftp.pwd()
# 删除远程目录         
ftp.rmd(dirname)    
#删除远程文件
ftp.delete(filename)   
#将fromname修改名称为toname。
ftp.rename(fromname, toname)
#上传目标文件
ftp.storbinaly("STOR filename.txt",file_handel,bufsize)