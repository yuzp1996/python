# -*- coding: cp936 -*-
import socket
"""
�ͻ�������
�����뱾���ķ��������н���
"""
s= socket.socket()

host = socket.gethostname()
port = 1024

s.connect((host,port))
print s.recv(1025)   #���ܷ���������Ϣ
