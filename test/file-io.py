import sys
import os
import os.path
import shutil
rootdir = "D:/Python/filetext"
# -*- coding: utf-8 -*- 

#文件打开
#file object = open(file_name [, access_mode][, buffering])
#file_name变量是一个包含了你要访问的文件名称的字符串值。
#access_mode：access_mode决定了打开文件的模式：只读，写入，追加等。所有可取值见如下的完全列表。这个参数是非强制的，默认文件访问模式为只读(r)。
#buffering：如果buffering的值被设为0，就不会有寄存。如果buffering的值取1，访问文件时会寄存行。如果将buffering的值设为大于1的整数，表明了这就是的寄存区的缓冲大小。如果取负值，寄存区的缓冲大小则为系统默认。


#查找问题后 发现是由于python中的 ‘\’ 是转义符号，要想输出\ 的办法有两种
#1 、在\后再加\  就是\\ 的形式
#把第二行改为infile =open("C:\\Users\\Spirit\\Desktop\\bc.txt",'r') 即可
#2、在路径前加个 r ，意思是按原始字符处理 。
# eg：  infile =open(r"C:\Users\Spirit\Desktop\bc.txt",'r')
# 
# ##文件在UE中打开，编码另存为ANSI/ASCII，对应encoding 为 GBK
# ##文件在UE中打开，编码另存为UTF-8无BOM，对应encoding 为 UTF-8
'''
#读模式 r 以只读方式打开文件。文件的指针将会放在文件的开头
def main():
    #file = open("D:\\Python\\filetext\\Efile\\pyhtonfile-1.txt","r",encoding = "GBK")
    file = open("D:\\Python\\filetext\\Efile\\zhinengcunk.csv","r",encoding = "UTF-8")
    data = file.read()
    print(data)
    file.close()
main()
'''
'''
#读写模式 r+ 打开一个文件用于读写。文件指针将会放在文件的开头
def main():
    #file = open("D:\\Python\\filetext\\Efile\\pyhtonfile-1.txt","r",encoding = "GBK")
    file = open("D:\\Python\\filetext\\Efile\\pyhtonfile-2.txt","r+",encoding = "UTF-8")
    data = file.read()
    print(data)
    print("--------------------------------------------------------------")
    #无论write写在哪里都是在文件后追加
    file.write("我在测试pyhton文件处理\n")
    #data = file.read()
    file.close()
main()
'''

#写模式 w 打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件
'''
def main():
    file = open("D:\\Python\\filetext\\Efile\\file-W.txt","w",encoding = "UTF-8")
    print("--------------------------------------------------------------")
    file.write("我在测试pyhton文件处理,测试WWWWW\n")
    file.close()
main()
'''

#读写模式 w+ 打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件
'''    
seek():移动文件读取指针到指定位置
tell():返回文件读取指针的位置
seek()的三种模式：
    （1）f.seek(p,0)  移动当文件第p个字节处，绝对位置
    （2）f.seek(p,1)  移动到相对于当前位置之后的p个字节
    （3）f.seek(p,2)  移动到相对文章尾之后的p个字节   

def main():
    file = open("D:\\Python\\filetext\\Efile\\file-W1.txt","w",encoding = "UTF-8")
    print("--------------------------------------------------------------")
    file.write("我在测试pyhton文件处理,测试WWWWW\n")
    print("定位之前的光标位置:%s" % (file.tell())) #tell():返回文件读取指针的位置,也就是光标停留位置
    file.flush() #刷新文件使内存的内容刷新至文件夹

 #因为W+读取文件之后会定位在文件尾部，所以需要重新定位一下光标位置，要不无法读取
    file.seek(0)  
    print("定位之前的光标位置:%s" % (file.tell()))
    file.close()
#使用W模式写后是没有权限read的，要重新进行读取，才能读到文件中的内容
    file = open("D:\\Python\\filetext\\Efile\\file-W1.txt","r",encoding = "UTF-8")
    data = file.read()
    print(data)
    file.close()
main()
'''
'''
#追加读 a+打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。
#文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
def main():
    file = open("D:\\Python\\filetext\\Efile\\file-W1.txt","a+",encoding = "UTF-8")
    print("--------------------------------------------------------------")
    file.write("我在测试pyhton文件处理,测试A+++++\n")
    print("定位之前的光标位置:%s" % (file.tell())) #tell():返回文件读取指针的位置,也就是光标停留位置
    file.flush() #刷新文件使内存的内容刷新至文件夹
 #因为W+读取文件之后会定位在文件尾部，所以需要重新定位一下光标位置，要不无法读取
    file.seek(0)  
    print("定位之前的光标位置:%s" % (file.tell()))
    #file.close()
#使用W模式写后是没有权限read的，要重新进行读取，才能读到文件中的内容
    #file = open("D:\\Python\\filetext\\Efile\\file-W1.txt","r",encoding = "UTF-8")
    data = file.read()
    print(data)
    file.close()
main()
'''
#------------------------------------------------#
'''
#文件的其他处理方法#
#fileno() 方法返回一个整型的文件描述符(file descriptor FD 整型)，可用于底层操作系统的 I/O 操作
def main():
    file = open("D:\\Python\\filetext\\Efile\\file-W1.txt","r",encoding = "UTF-8")
    print("--------------------------------------------------------------")
    fileid = file.fileno()
    print("文件的描述符为:",fileid)#fileno() 方法返回一个整型的文件描述符(file descriptor FD 整型)，可用于底层操作系统的 I/O 操作
    print("文件名为：",file.name)
    for index in range(5):
        line = next(file)
        print("第 %d 行 - %s" % (index, line))
    file.close() 
main()
'''
'''
#read方法：用于从文件读取指定的字节数，如果为给定或为负则读取所有
def main():
    file = open("D:\\Python\\filetext\\Efile\\file-W1.txt","r",encoding = "UTF-8")
    print("--------------------------------------------------------------")
    print("文件名为：",file.name)
    data = file.read()
    print("data:",data)
    print("--------------------------------------------------------------")    
    data1 = file.readline(5)
    print("data1:",data1)
    print("光标位置",file.tell())
    print("--------------------------------------------------------------")  
   
    data2 = file.readlines(10)
    for data2 in file.readlines():
        data2 = data2.strip("\n") #使用strip去掉换行符/n
        print("读取所有行:%s" % (data2))
    file.close() 
main()
'''
'''
#readlines() 方法用于读取所有行(直到结束符 EOF)并返回列表
file = open("D:\\Python\\filetext\\Efile\\file-W1.txt","r",encoding = "UTF-8")
#data2 = file.readlines(10)
for data2 in file.readlines():
    data2 = data2.strip("\n") #使用strip去掉换行符/n
    print("读取所有行:%s" % (data2))
file.close() 

'''
'''
file = open("D:\\Python\\filetext\\Efile\\file-W1.txt","r",encoding = "UTF-8")
data = file.readline(12)
print("读取所有行:%s" % (data))
file.close() 
'''

#writelines() 方法用于向文件中写入一序列的字符串
#这一序列字符串可以是由迭代对象产生的，如一个字符串列表，
#换行需要制定换行符 \n
def main():
    file = open("D:\\Python\\filetext\\Efile\\file-W1.txt","a+",encoding = "UTF-8")
    data = ["我在测试writelines 1\n","我在测试writelines 2\n",]
    file.writelines(data)
    file.flush()
    file.seek(0,0) #跳到首行
    line = file.readlines() #读取所有行
    print ("读取的数据: %s" % (line))
    file.close() 
main()