# -*- coding: cp936 -*-
def lines(file):
    for line in file: yield line
    yield '\n'

def blocks(file):
    block = []
    for line in lines(file):
        if line.strip():    # ɾ���հ��ַ�
            block.append(line)
        elif block:
            yield ''.join(block).strip()    # ָ���ַ����������ֵ�Ԫ�������µ��ַ���
            block = []
