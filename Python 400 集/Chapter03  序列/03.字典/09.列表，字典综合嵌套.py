r1 = {"name": "Mike", "age": 18, "salary": 30000, "city": "Peking"}
r2 = {"name": "John", "age": 18, "salary": 30000, "city": "Peking"}
r3 = {"name": "Mickey", "age": 18, "salary": 30000, "city": "Peking"}
r4 = {"name": "Mark", "age": 18, "salary": 30000, "city": "Peking"}
# 构建键值对列表，凑成表格
tb = [r1, r2, r3, r4]
print(tb)

# 获取第二行员工的薪资
print(tb[1].get("salary"))

# 获取所有员工的名字
for i in range(len(tb)):
    print(tb[i].get("name"))

# 打印表的所有数据
for i in range(tb.__len__()):
    print(tb[i].get("name"), tb[i].get("age"), tb[i].get("salary"), tb[i].get("city"))
