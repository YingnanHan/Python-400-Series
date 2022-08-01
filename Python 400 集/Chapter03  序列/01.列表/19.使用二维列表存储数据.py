l = [["Mike", 18, 30000, "北京"], ["John", 20, 40000, "上海"], ["Jack", 35, 6000, "长春"]]

print(l)
print(l[0])
print(l[0][2])

# 使用嵌套循环打印二维列表
for i in range(len(l)):
    for j in range(len(l[i])):
        print(l[i][j], end="\t")
    print()
