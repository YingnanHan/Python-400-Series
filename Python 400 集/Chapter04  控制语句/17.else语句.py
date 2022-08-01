# while for循环可以附带一个else子句，如果for while语句没有被break中断并且
# 自身条件并不满足，则执行else子句
#   while  条件表达式:
#       循环体
#   else:
#       语句块

# or

#   for 变量 in 可迭代对象:
#       循环体
#   else:
#       语句块

# 内容同上例 求解录入的四名员工的平均工资
salarySum = 0
salarys = []
for i in range(4):
    s = input("请输入4位员工的薪资  按Q | q 结束。")

    if s.upper() == 'Q':
        print("录入完成，退出")
        break
    if float(s) < 0:
        continue

    salarys.append(float(s))
    salarySum += float(s)
else:
    print("您已经对4名员工的薪资录入完毕")

print("录入薪资:{0}".format(salarySum))
print("平均薪资:{0}".format(salarySum / 4))
