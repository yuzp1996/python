# -*- coding: cp936 -*-
import socket
"""
�������˴���

"""

s = socket.socket()

host = socket.gethostname()# socket���������
port = 1237  #�˿�ֻ�ܱ�ռ��һ�η��������  ��ͨ��ÿ���׽��ֶ˿ڣ���Э��/�����ַ/�˿ںš�����
s.bind((host, port)) #�������IP������˿�

s.listen(5)
while True:
    c, addr = s.accept()    #���ܿͻ�������
    print 'Go connection from ', addr
    c.send('Thank you for connecting ��������������')
    c.close()
