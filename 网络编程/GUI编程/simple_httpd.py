import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

# 构建web服务器，这五行代码缺一不可

# http服务，CGI服务的引入
from http.server import HTTPServer, CGIHTTPRequestHandler
# 端口号
port = 8080

# 创建一个服务器
# ''表示host默认本机
httpd = HTTPServer(('', port), CGIHTTPRequestHandler)
print("Starting simple_httpd on port: " + str(httpd.server_port))
# 启动服务
httpd.serve_forever()
