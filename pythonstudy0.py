# people = {
# 'yu':{
# 'phone' : '123',
# 'addr' :'anbei'

# },
# 'wang':{
# 'phone' : '321',
# 'addr' :'an1bei'

# },
# 'xu': {
# 'phone' : '456',
# 'addr' :'an2bei'

# }
# }

# name = raw_input('Name: ');
# reasher = raw_input(" p or a :");
# if name in people:
#     if reasher == 'p':
#         print r"%s 'phone is %s" %(name,people[name]['phone'])

# raw_input("Press Enter");

# print "enne  leuo"


#
# dir = {"yu" : 1 ,"zhi" : 2};
# print dir
#
# dir1=dir.copy()
# dir1["yu"] = 3
# print dir1
# print dir
# print dir.get("yuss")
# raw_input("Press Enter")


# print 123,431,43
# raw_input("press enter")

# x,y,rest = [1,2,3 ]
# for num in range(0,101):
#     print num,'you should live hard'

# fibs = [0,1]
# for obj in range(8):
#     fibs.append(fibs[-2]+fibs[-1])
# print(fibs[-1])
# print(fibs)

# def fibs(num):
#     result = [0,1]
#     num = input("please input your num: ")
#     for i in range(num):
#         result.append(result[-1]+result[-2])
#     print(result)
#     return result
#
# fibs(1)
#
# raw_input("press enter")

# _metaclass_=type
# class Bird:
#     def  __init__(self):
#         self.hunger = True
#     def eat(self):
#         if self.hunger:
#             print "Aaaah..."
#             self.hunger =False
#         else:
#             print"NO Thank you"
#
# class SongBird(Bird):
#     def __init__(self):
#         super(SongBird,self).__init__()
#         self.sound = "Squawk!"
#     def sing(self):
#         print self.sound
# sb = SongBird()
# sb.sing()
#
# sb.eat();
# sb.eat();

# raw_input("please enter ")




# def checkIndex(key):
#     if not isinstance(int,long):raise TypeError
#     if key<0:raise IndexError
# class ArithmeticSequence:
#     def __init__(self,start = 0,step = 1):
#         self.start = start
#         self.step = step
#         self.changed = {}
# def __getitem__(self,key):
#     checkIndex(key)
#     try: return self.changed[key]
#     except KeyError:
#         return self.start+key*self.step
# def __setitem__(self,key,value):
#     checkIndex(key)
#     self.changed[key] = value
# raw_input("试试咯")

# __metaclass__=type
# class Rectangle:
    # def __init__(self):
        # self.width=0
        # self.height=0
    # def setSize(self,size):
        # self.width,self.height = size
    # def getSize(self):
        # return self.width,self.height
    # size = property(getSize,setSize)


# class Fibs:
    # def __init__(self):
        # self.a = 0
        # self.b = 1
    # def next(self):
        # self.b,self.a = self.a+self.b,self.b
        # return self.a
    # def __iter__(self)
        # # return self

# def flatten(nested):
    # for sublist in nested:
	    # for element in sublist:
		    # yield element

def flatten(nested)
    try：
	    for sublist in nested:
		    for element in flatten(sublist):
			    yield element
	except TypeError:
	    yield nested

#八皇后
# -*- coding: cp936 -*-
def conflict(state,nextX):# 中心函数 定义冲突
    nextY = len(state)
    for i in range(nextY):
        if abs(state[i]-nextX) in (0,nextY-i):
            return True
    return False


def queens(num,state=()):#state=()是初始化
    for pos in range(num):
        if not conflict(state,pos):
            if len(state) == num-1:
                yield(pos,)
            else:
                for result in queens(num,state+(pos,)):
                    yield (pos,)+result

def prettyprint(solution):
    def line(pos, length = len(solution)):
        return '. '*(pos)+'X'+'. '*(length-pos-1)
    for pos in solution:
        print line(pos)			
		
		
		
		
		
from random import randrange
num = input("how many dice?")
side = input("how many side per dir")
sum =0
for i in range(num): sum+=randrange(side)
print "the result is ",sum




values = range(1,11)+'Jack Queen King'.split()
suits = 'diamonds clubs hearts spades'.split()
print values
print suits
deck=['%s of %s '%(v,s) for v in values for s in suits ]
from pprint import pprint
from random import shuffle
shuffle(deck)
pprint(deck[:12])
