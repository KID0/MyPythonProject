# coding=utf8

import zipfile
'''
zipfile模块是python中自带的模块，
提供了对zip文件的创建读、写、追加、解压以及列出zip文件列表的工具
'''
from threading import Thread
# 这是一个多线程控制模块




def extractFile(zFile, password):
    try:
        zFile.extractall(pwd=password)
        '''
        extractall(path=None, members=None, pwd=None)

        path指定解压后文件的存储位置
        members（可选）指定要Zip文件中要解压的文件
        pwd指定Zip文件的解压密码
        '''
    except Exception as e:
        pass


def main():
    zFile = zipfile.ZipFile('evil.zip')
    # 首先要有一个密码本！
    passFile = open('dictionary.txt')
    for line in passFile.readlines():
        password = line.strip('\n')
        t = Thread(target=execfile, args=(zFile, password))
        t.start()


if __name__ == '__main__':
    main()