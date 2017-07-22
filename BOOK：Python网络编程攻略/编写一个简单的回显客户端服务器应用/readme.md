为了查看客户端和服务器之间的交互，要在一个终端（cmd.exe）里启动如下服务器脚本：

$ python 1_13a_echo_server.py --port=9900
Starting up echo server on localhost port 9900
Waiting to receive message from client

然后，在另一个终端（cmd.exe）里运行客户端，如下所示：

$ python 1_13b_echo_client.py --port=9900
Connecting to localhost port 9900
Sending Test message. This will be echoed
Received: Test message. Th
Received: is will be echoe
Received: d
Closing connection to the server

连接到本地主机后，服务器还会输出以下消息：

Data: Test message. This will be echoed
sent Test message. This will be echoed bytes back to ('127.0.0.1', 42961)
Waiting to receive message from client


<!-- 
网络数据交换太容易发生编码错误了，注意去解决
发送的时候转换成二进制，接受打印数据的时候变成字符串
-->