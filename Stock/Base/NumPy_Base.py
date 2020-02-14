import numpy as np
print(np.version.full_version)
'''
#生成一个自然数组
a = np.arange(21)
print(a)
print(type(a))

#重新构造一下这个数组
a = a.reshape(7,3)
#函数中reshape(a,b)，其中a*b 要等于arange(c)中的C，否则会报错
print(a)

a是array，我们还可以调用array的函数进一步查看a的相关属性："ndim"查看维度；"shape"查看各维度的大小；
"size"查看全部的元素个数，等于各维度大小的乘积；"dtype"可查看元素类型；"dsize"查看元素占位（bytes）大小。
print(a.ndim)
'''

#创建数组
raw = [0,1,2,3,4]
print(type(raw))
print(raw)
a = np.array(raw)
print(type(a))
print(a)