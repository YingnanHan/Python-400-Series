# coding=utf-8
# 测试os模块中关于文件和目录的操作
import os

# 1.获取文件和文件夹的相关信息
print(os.name)  # 判断当前的操作系统，Linux,Unix->posix  Windows->nt
print(os.sep)  # 输出当前系统的文件路径分隔符
print(repr(os.linesep))  # 输出当前系统的默认换行符,repr函数将对象转化为供解释器读取的形式
print(os.stat("17.os.py"))  # 输出指定文件所有的指定信息

# 2.关于工作目录的操作
print(os.getcwd())  # 获取当前项目的工作目录
# os.chdir(r"C:\Users\20613\Desktop")#切换工作目录录
# os.mkdir("books")#在当前的工作空间创建一个目录

# 3.创建目录，创建多级目录，删除
# os.rmdir("books")#删除指定目录,注意这个函数只删除空文件夹
# os.makedirs("电影/港台/周星驰")#生成多级目录
# os.removedirs("电影/港台/周星驰")#注意这个函数只删除空文件夹
# os.makedirs("../music/hongkong/刘德华")#使用相对路径
# os.rename("../music","../movie")#文件重命名
dirs = os.listdir("../movie")  # 列出某一目录下的子目录
print(dirs)
