创建的A与C文件夹中要放置clinet.py与server.py文件，要在文件夹中启动服务才可以。

    python client.py urlsA.txt A http://localhost:4242 


可以参考的网站  http://www.code123.cc/1335.html


其实这个的原理比较简单，书上的说明也是很简洁明了的，自己做了后就回去有点迷糊  其实是这样子的

## 这时服务端 
from SimpleXMLRPCServer import SimpleXMLRPCServer
s = SimpleXMLRPCServer("",4242)

def twice()
   ...

s.server_forever() 启动服务器

## 这里是请求端

from xmlrpclib import ServerProxy
s = ServerProxy("http://localhost:4242")
s.twice(2)




请求端来调用服务器端的程序 来实现远程节点的读写