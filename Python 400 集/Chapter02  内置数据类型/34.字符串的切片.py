a = "abcdefghijklmnopqrstuvwxyz"
# 按照下标取得某一个字符
print(a[2])
# 包头不包尾 对字符串进行切片 默认步长为1
print(a[1:5])
# 手动设置步长
print(a[1:5:2])
# 如果不提供偏移量以及步长默认取得整个字符串
print(a[:])
# 没有起始偏移量的情况
print(a[:5])  # 输出 0 1 2 3 4号元素


# 操作数为负数的情况
print("abcdefghijklmnopqrstuvwxyz"[-3])
print("abcdefghijklmnopqrstuvwxyz"[-8:-3])  # 注意所有含有两个数字的切片操作包含的范围
print("abcdefghijklmnopqrstuvwxyz"[::-1])  # 实现字符串的逆序


# 如果切片的偏移量超过了实际上的范围那么自动取到合理范围的极限
print("abcdefghijklmnopqrstuvwxyz"[-88:55])
