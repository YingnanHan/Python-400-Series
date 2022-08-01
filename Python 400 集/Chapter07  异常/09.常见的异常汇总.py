"""
1.SyntaxError:语法错误
    int a = 3
         ^
    SyntaxError:Invalid Syntax

2.NameError:尝试访问一个没有声明的变量
    print(a)
    NameError:name 'a' is not defined

3.ZeroDivisionError:除数为0错误(零除错误)
    a = 3/0
    ZeroDivisionError:division by error

4.ValueError:数值错误
    float("abc")
    ValueError:could not convert string to float :'abc'

5.TypeError:类型错误
    123+"abc"
    123+"abc"
    TypeError:unsupportted operand type(s) for+:'int' and 'str'

6.ArttributeError:访问对象的不存在的属性
    a = 100
    a.say()
    ArrtributeError：“int” object has no arttribute say()

7.IndexError:索引越界异常
    a = [4,5,6]
    a[10]
        a[10]
    IndexError:list index out of range

8.KeyError:字典的关键字不存在
    a = {"name":"Joe"}
    a["salary"]
        a["salary"]
    KeyError:'salary'
"""
