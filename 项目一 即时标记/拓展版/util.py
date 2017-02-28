# -*- coding: cp936 -*-
def lines(file):
    for line in file: yield line
    yield '\n'

def blocks(file):
    block = []
    for line in lines(file):
        if line.strip():    # 删除空白字符
            block.append(line)
        elif block:
            yield ''.join(block).strip()    # 指定字符连接序列种的元素生成新的字符串
            block = []
