# -*- coding: cp936 -*-
import socket

s = socket.socket()

host = socket.gethostname()
port = 1234
s.bind((host, port))    #��������˿�

s.listen(5)    #����������
while True:
    c, addr = s.accept()    #���ܿͻ������� accpet����һֱ�ȴ�ֱ���ͻ��˵�����  ���أ�client,address��Ԫ��
    print 'Go connection from ', addr
    c.send('Thank you for connecting')
    c.close()
