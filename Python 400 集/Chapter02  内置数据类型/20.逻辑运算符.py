# and or not被称为逻辑运算符 分别为 逻辑与 逻辑或 逻辑非

print(True or False)
print(True and False)
print(False and True)  # 这里存在短路求值的情况，对于and运算如果左侧的值为false那么就不会计算右侧的值并且直接返回false
print(not False)
