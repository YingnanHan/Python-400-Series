'''
try...except...else结构增加了else块，如果try块中没有抛出异常，执行else块。如果
try块中抛出异常，则执行except块，不执行else块
'''

# 测试
try:
    a = input("请输入一个被除数：")
    b = input("请输入一个除数：")
    c = float(a) / float(b)
except BaseException as e:
    print(e)
else:
    print(c)

print("程序结束！！！")
