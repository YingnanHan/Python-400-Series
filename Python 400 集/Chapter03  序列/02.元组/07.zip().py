# 将多个列表对象合并为一个列表对象 列表中每一个元素是之前的列表内元素各自重组成的元租对象
a = [1, 2, 3, 4]
b = [2, 3, 4, 5]
c = [6, 7, 8, 9]

print(list(zip(a, b, c)))
