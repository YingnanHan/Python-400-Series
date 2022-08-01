#1.对数组进行排序
sortedList = sorted([454,6,465,56,64,64,8548,4555])
print("升序排列:",sortedList)

#2.对数组进行排序
sortedList = sorted([454,6,465,56,64,64,8548,4555],reverse=True)
print("降序排列:",sortedList)

#3.对字符串列表进行排序  按字典序升序排
sortedList = sorted(["sadfas","asgadrt","asfhby","casdtcfrt"])
print("升序排列:",sortedList)

#4.sorted接收KEY来实现自定义排序
def func1(a):
    return abs(a)

def func2(a):
     return len(str(a))
sortedList = sorted([454,-6,-465,-56,64,-64,8548,4555],reverse=True,key=func2)
print("自定义排列:",sortedList)