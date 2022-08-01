# coding=utf-8
'''
with 关键字（上下文管理器）可以自动管理上下文资源，不论什么原因跳出 with 块，都能
确保文件正确的关闭，并且可以在代码块执行完毕后自动还原进入该代码块时的现场。
'''

s = ["Mike\n", "John\n", "Sarah"]
with open(r"file/e.txt", "a", encoding="utf-8") as f:
    f.writelines(s)  # 这里不需要在调用f.close()了，with管理器已经帮助用户执行完这一步操作了
