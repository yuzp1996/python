# -*- coding: cp936 -*-
import socket

s = socket.socket()

host = socket.gethostname()
port = 1234
s.bind((host, port))

s.listen(5)
while True:
    c.addr = s.accept()    #接受客户端连接
    print 'Go connection from ', addr
    c.send('Thank you for connecting')
    c.close()
