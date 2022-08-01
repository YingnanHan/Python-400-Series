# 创建方式1
a = {"name": "Mike", "age": 18, "job": "teacher"}

# 创建方式2
b = dict(name="Sarah", age=50, job="Musician")

# 创建方式3
c = dict([("name", "Johnson"), ("age", 20), ("job", "worker")])

# 创建方式4
d = {}

# 创建方式5
k = ["name", "age", "job"]
v = ["Scarlet", 36, "actor"]
e = dict(zip(k, v))  # 对应压缩构成键值对

# 创建方式6
f = dict.fromkeys("name", "age", "job")  # 创建一个值为空只有key的键值对
