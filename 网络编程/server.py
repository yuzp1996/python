# -*- coding: cp936 -*-
import socket

s = socket.socket()

host = socket.gethostname()
port = 1234
s.bind((host, port))    #监听这个端口

s.listen(5)    #允许监听五个
while True:
    c, addr = s.accept()    #接受客户端连接 accpet函数一直等待直到客户端的连入  返回（client,address）元祖
    print 'Go connection from ', addr
    c.send('Thank you for connecting')
    c.close()
