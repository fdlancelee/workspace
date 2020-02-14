#os模块主要用于与操作系统交互
#shutil模块则包含一些针对文件的操作
import os
import os.path
import shutil
rootdir = "D:/Python/filetext"

#os.listdir() 返回工作目录--ls
os.listdir(rootdir);
#print (os.listdir(rootdir))

##os.getcwd()：以字符串形式获取当前工作目录路径 → pwd
##获取工作空间目录
Wordspacedir = os.getcwd();
print ("Wordspacedir is :",Wordspacedir)

#os.chdir（"/absolute/or/relative/path"）：更改当前的工作路径→ cd
#os.path.join()：创建路径供后续使用→ 没有等效的命令
#shutil.copy2（"source_file_path","
#
#
#
#
#
#stination_directory_path"）：复制文件或目录→ cp
#shutil.move（"source_file_path","destination_directory_path"）：移动文件或目录→ mv
#os.remove（“my_file_path”）：删除文件→ rm
#shutil.rmtree（“my_directory_path”）：删除路径及其包含的所有文件和目录→ rm –rf

#os.walk（"starting_directory_path"）：返回一个生成器（generator），该生成器包含当前目录和所有子目录中的文件名称及路径信息；
#→没有完全等价的shell命令，
#不过 ls -R 命令提供了子目录名称和子目录中的文件名称
#创建一个生成器，用于返回关于当前目录和子目录的信息。在起始指定的目录中有效。 
#os.walk() 遍历包含的每个目录后，都会返回下列项：
#（1）当前目录路径（字符串类型）
#（2）当前目录下的子目录名称（字符串列表类型）
#（3）当前目录中的文件名称（字符串列表类型的）

for dir_path,dir_names,file_names in os.walk(rootdir):
    #输出文件路径
    #print ("dir_path is :",dir_path)
    for dir_name in dir_names:
            print ("dir_names is :",dir_names)
            for file_names in file_names:
                print ("file_names is :",file_names)

#获取信息
 #   * 
#os.getcwd() ——以字符串形式获取当前工作目录路径—— pwd
#    * 
#os.listdir() ——以字符串列表的形式获取当前工作目录的内容——ls
#    * 
#os.walk("starting_directory_path")——返回函数，其中包含当前目录和所有子目录中的目录和文件的名称和路径信息——没有完全等价的shell命令，不过ls -R提供了子目录名称和子目录中的文件名称
#
#改动信息
#    * 
#os.chdir("/absolute/or/relative/path") ——改变当前的工作路径——cd
#    * 
#os.path.join()——创建路径供后续使用——没有等效CLI
#    * 
#os.makedirs (“dir1 / dir2”)——创建目录——mkdir - p
#    * 
#shutil.copy2("source_file_path","destination_directory_path")——复制文件或目录——cp
#    * 
#shutil.move("source_file_path","destination_directory_path")——移动文件或目录——mv
#    * 
#os.remove (“my_file_path”)——删除文件——rm
#    * 
#shutil.rmtree (“my_directory_path”)——删除路径及其包含的所有文件和目录——rm –rf