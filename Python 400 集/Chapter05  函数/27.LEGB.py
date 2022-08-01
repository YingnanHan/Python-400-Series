"""
python在查找名称的时候，是按照LEGB规则进行查找的：
Local->Enclosed->Global->Built in
Local:指的就是函数或者类的方法内部
Enclosed:指的是嵌套函数(一个函数包裹另一个函数 闭包)
Global:指的是模块中的全局变量
如果某一个name映射在局部命名空间中没有找到，接下来就会在
闭包作用域进行搜索，如果闭包作用域也没有找到，python就回
到全局命名空间中进行查找，最后在内建built-in命名空间中进
行搜搜（如果在所有的命名空间中都没有找到，就会返回一个Nam
eError）
"""


# 测试LEGB

# str = "global str"
def outer():
    # str = "outer"
    def inner():
        # str  = "abcd"
        print(str)

    inner()


outer()
