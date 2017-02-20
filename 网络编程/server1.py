# -*- coding: cp936 -*-
import socket
"""
服务器端代码

"""

s = socket.socket()

host = socket.gethostname()# socket有这个方法
port = 1237  #端口只能被占用一次否则会提醒  ‘通常每个套接字端口（‘协议/网络地址/端口号’）’
s.bind((host, port)) #监听这个IP的这个端口

s.listen(5)
while True:
    c, addr = s.accept()    #接受客户端连接
    print 'Go connection from ', addr
    c.send('Thank you for connecting 服务器传过来的')
    c.close()
