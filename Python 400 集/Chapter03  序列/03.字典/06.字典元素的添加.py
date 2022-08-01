a = {"name": "Mike", "age": 18, "job": "teacher"}
# 方式一
a["name"] = "Joe"  # 如果键重复直接覆盖
a["hobby"] = "music"
print(a)


# 方式二
b = {"sex": "male", "name": "Bidden"}
a.update(b)
print(a)
