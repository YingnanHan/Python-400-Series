#在一个列表中的偶数删除并返回剩下的元素
l = list(filter(lambda x: x%2!=0,[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))#将所有的满足条件的元素过滤出来
print(l)

#将一个序列中的空字符串都删除
l = list(filter(lambda s:len(s)!=0,["123","","asa","AAA"]))
print(l)