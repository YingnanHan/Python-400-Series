# coding:utf-8

'''
当我们导入某个模块文件时， Python 解释器去哪里找这个文件呢？只有找到这个文
件才能读取、装载运行该模块文件。它一般按照如下路径寻找模块文件（按照顺序寻找，找
到即停不继续往下寻找）：
1. 内置模块
2. 当前目录
3. 程序的主目录
4. pythonpath 目录（如果已经设置了 pythonpath 环境变量）
5. 标准链接库目录
6. 第三方库目录（site-packages 目录）
7. .pth 文件的内容（如果存在的话）
8. sys.path.append()临时添加的目录
当任何一个 python 程序启动时，就将上面这些搜索路径(除内置模块以外的路径)进行收集，
放到 sys 模块的 path 属性中（sys.path）。
'''

#测试systemppath，打印模块搜索路径
import  sys

print(sys.path)
