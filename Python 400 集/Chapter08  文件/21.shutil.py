# coding=utf-8

# shutil模块用于文件的拷贝 压缩

import shutil
import zipfile

# 拷贝指定文件
# shutil.copyfile("./file/a.txt","./file/aCopy.txt")#第一个参数是 src 第二个参数是dest

# 拷贝指定文件夹及其下属所有文件
# shutil.copytree("./file","./fileCopy")

# 手动设置不拷贝哪些文件
# shutil.copytree("./电影","./fileCopy2",ignore=shutil.ignore_patterns("*.mp4","*.html"))

# 压缩，解压缩
# shutil.make_archive("映画","zip","file")#将file文件/文件夹压缩成 映画.zip文件

# 压缩操作
# z1 = zipfile.ZipFile("target.zip","w")#生成一个target.zip目标压缩文件对象，可以将不同的文件压缩至里面
# z1.write("./file")#使用该对象的write方法来进行写操作
# z1.write("./fileCopy")
# z1.write("./fileCopy2")
# z1.close()#压缩文件添加结束之后关闭

# 解压缩操作
z2 = zipfile.ZipFile("target.zip", "r")
z2.extractall("extractedFile")  # 讲一个压缩文件解压缩
z2.close()
