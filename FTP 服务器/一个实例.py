#coding:utf-8

'''
ctypes是Python的外部函数库。
它提供了C兼容的数据类型，并且允许调用动态链接库/共享库中的函数。
它可以将这些库包装起来给python使用。
'''
from ctypes import *
import os 
import sys 
import ftplib 

class myFtp:
  # 实例化一个客户端
  ftp=ftplib.FTP() 
  # 这是什么变量？
  bIsDir=False
  path="" 
  
  '''
  21端口用于连接，20端口用于传输数据,都是FTP服务的默认端口
　进行FTP文件传输中，客户端首先连接到FTP服务器的21端口，进行用户的认证，
  认证成功后，要传输文件时，服务器会开一个端口为20来进行传输数据文件。
  '''
  # 用来初始化的方法
  def __init__(self, host, port='21'):
    # 打开调试级别2，显示详细信息 
    self.ftp.set_debuglevel(2)
    # 0主动模式 1被动模式 
    self.ftp.set_pasv(0)  
    # 连接到某一个主机的某一端口
    self.ftp.connect(host, port)

  def Login(self, user, passwd ): 
    self.ftp.login( user, passwd ) 
    print(self.ftp.welcome)

  def DownLoadFile(self, LocalFile, RemoteFile ): 
    # wb:只写打开或新建一个二进制文件；只允许写数据。
    file_handler=open( LocalFile, 'wb') 
    # retrbinary() 创建一个新端口，用二进制取得数据
    # 应该是将RemoteFile文件的内容写入到LocalFile中
    self.ftp.retrbinary("RETR %s" %( RemoteFile ), file_handler.write )  
    file_handler.close()
    return True

  def UpLoadFile( self, LocalFile, RemoteFile ): 
    # 如果本地没有发现要上传的文件
    if os.path.isfile( LocalFile ) ==False:
      return False
    file_handler=open( LocalFile, "rb") 
    # 4096指一次性上传文件的最大容量限制
    self.ftp.storbinary('STOR %s'%RemoteFile, file_handler, 4096)
    file_handler.close()
    return True

  # 更新文件目录
  def UpLoadFileTree( self, LocalDir, RemoteDir ): 
    if os.path.isdir( LocalDir ) ==False:
      return False
    LocalNames=os.listdir( LocalDir ) 
    print(RemoteDir)
    # cwd:跳转目录
    self.ftp.cwd( RemoteDir ) 
    for Local in LocalNames: 
      src=os.path.join( LocalDir, Local) 
      if os.path.isdir( src ): 
        self.UpLoadFileTree( src, Local ) 
      else:
        self.UpLoadFile( src, Local ) 
    self.ftp.cwd("..") 
    return

  def DownLoadFileTree( self, LocalDir, RemoteDir ): 
    if os.path.isdir( LocalDir ) ==False:
      os.makedirs( LocalDir ) 
    self.ftp.cwd( RemoteDir ) 
    # nlst():列出给定目录的文件列表
    RemoteNames=self.ftp.nlst() 
    for file in RemoteNames: 
      Local=os.path.join( LocalDir, file) 
      if self.isDir(file): 
        self.DownLoadFileTree( Local, file)         
      else:
        self.DownLoadFile( Local, file) 
    self.ftp.cwd("..") 
    return

  def show( self,list): 
    result=list.lower().split(" " ) 
    if self.pathinresult and"<dir>" in result: 
      self.bIsDir=True

  def isDir( self, path ): 
    self.bIsDir=False
    self.path=path 
    #this ues callback function ,that will change bIsDir value 
    # retrlines() 按行取数据
    self.ftp.retrlines('LIST',self.show ) 
    return self.bIsDir

  def close( self): 
    self.ftp.quit()

ftp=myFtp('********')
ftp.Login('*****','*****')
#ftp.DownLoadFile('TEST.TXT', 'others\\runtime.log')#ok 
#ftp.UpLoadFile('runtime.log', 'others\\runtime.log')#ok 
#ftp.DownLoadFileTree('bcd', 'others\\abc')#ok 
#ftp.UpLoadFileTree('aaa',"others\\" ) 
ftp.close()
print("ok!")