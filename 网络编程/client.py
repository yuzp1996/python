# -*- coding: cp936 -*-
import socket
"""
客户机代码
这是与本机的服务器进行交互
"""
s= socket.socket()

host = socket.gethostname()
port = 1024

s.connect((host,port))
print s.recv(1025)   #接受服务器端消息
