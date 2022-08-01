# 程序开发中，有时候也需要自己定义异常类,自定义异常类一般都是运行时异常，
# 通常继承Exception或其子类即可。命名一般以Error,Exception为后缀。自
# 定义异常通常以raise子句来抛出

# coding = utf-8
# 测试自定义异常类

class AgeError(Exception):  # 继承Exception

    def __init__(self, errorInfo):
        Exception.__init__(self)
        self.errorInfo = errorInfo

    def __str__(self):
        return str(self.errorInfo) + "年龄错误,年龄应该在0-150之间！"


if __name__ == '__main__':  # 如果为True，则模块为独立运行文件，可以执行测试代码
    age = int(input("输入一个年龄:"))
    if age < 1 or age > 150:
        raise AgeError(age)  # 如果认为出了问题，就使用raise来抛出异常
    else:
        print("正常的年龄:", age)
