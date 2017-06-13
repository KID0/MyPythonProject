# 参考来源：https://www.shiyanlou.com/courses/725/labs/2383/document

#编辑base_ftp_server.py文件

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

# 实例化虚拟用户 这是ftp验证首要条件
# "Authorizer"用于验证用户信息，处理客户端请求之类
authorizer = DummyAuthorizer()

# 为了方便起见 这里文件目录改成了home目录
# 添加用户权限和路径 参数分别是 用户名 密码 用户目录 权限

# 这里的路径都需要已经存在的文件夹
authorizer.add_user("user", "12345", "C:/Users/zxc78/Desktop/new/", perm="elradfmw")

#添加匿名用户 这个只需要路径就行
authorizer.add_anonymous("C:/Users/zxc78/Desktop/new/")
#初始化ftp句柄
handler = FTPHandler
handler.authorizer = authorizer


# 添加动态端口:在2000到2333的打开被动端口 用于连接
handler.passive_ports = range(2000,2333)

# 监听ip和端口 这是本地一个服务器
# 127.0.0.1是回送地址，指本地机，一般用来测试使用
# 做过端口映射的同学肯定知道把127.0.0.1的ip改成0.0.0.0 监听所有的ip就可以进行访问了
server = FTPServer(("127.0.0.1", 21), handler)
# 开始服务
server.serve_forever()