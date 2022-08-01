# lambda arg1,arg2,arg3...:表达式
#定义一个匿名函数求解三个数字之和
f = lambda a,b,c:a+b+c
print("调用:",f(1,2,3))


#匿名函数作为高阶函数的参数
#计算一个数组每一个元素的平方，以列表形式输出
L = list(map(lambda x:x*x ,[1,2,3,4,5,6,7,8,9]))
print(L)


#sorted中使用匿名函数
class Student:

    def __init__(self,name,age):
        self.name = name
        self.age = age

stu1 = Student("zhangsan",18)
stu2 = Student("lisi",19)
stu3 = Student("wangwu",20)

stu_list = [stu1,stu2,stu3]
res_list = sorted(stu_list,key= lambda x:x.age)#按照年龄升序排序
res_list = sorted(stu_list,key= lambda x:x.name)#按照姓名升序排序
res_list = sorted(stu_list,key= lambda x:x.name,reverse=True)#按照姓名降序排序
print(res_list)
#打印排序后的结果
for i in res_list:
    print("name:",i.name," age:",i.age)
