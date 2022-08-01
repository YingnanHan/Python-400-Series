# 使用列表和字典来保存数据
tb = []
r1 = {"name": "Mike", "age": 18, "salary": 7000, "city": "北京"}
r2 = dict(name="John", age=19, salary=8000, city="上海")
r3 = dict(name="Sarah", age=15, salary=0, city="长春")

tb = [r1, r2, r3]
# 遍历去除tb中的内容
for x in tb:
    print(x)

# 按照需求打印工资高于6000的数据
for x in tb:
    if x["salary"] > 6000:
        print(x["name"], end=" ")
