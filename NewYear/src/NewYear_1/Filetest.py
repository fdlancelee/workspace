'''
Created on 2016年1月5日

@author: FUDIAN
'''
# f = open('D:\Python\test\test.txt','r')
from asyncore import write
fn = 'D:/Python/test/test.txt'
# f = open(fn,'r')
# print(f.read())

with open(fn,'w') as s:
#     print(s.read())
    s.write('我是成功了吗？')
#     print(s.read())

    
