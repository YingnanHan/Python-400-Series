a = {"name": "Mike", "age": 18, "job": "teacher"}

# 通过[]来访问字典
print(a["name"])  # 如果没有这个键就会报告KeyError错误

# 使用get方法访问字典
print(a.get("age"))  # 如果没有这个对象就会返回None
print(a.get("hobby"))
print(a.get("hobby", "not exist"))  # 如果不存在对应的值，就会返回第二个参数
