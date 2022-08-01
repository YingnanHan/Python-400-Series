# 进行如下操作
# 输入一个学生的成绩，将其转化为以下简单描述
# 不及格(<60)  及格(60-79)  良好(80-89)  优秀(90-100)

# 方案一
# score = int(input("请输入成绩:"))
# grade = ""
#
# if score < 60:
#     grade = "不及格"
# elif score < 80:
#     grade = "及格"
# elif score < 90:
#     grade = "良好"
# else:
#     print("优秀")
#
# print("分数是{0},等级是{1}".format(score,grade))

# 方案二


score = int(input("请输入成绩:"))
grade = ""

print("分数是{0}".format(score))
print("等级是")

if (60 <= score <= 80):
    print("及格")
if score <= 60:
    print("不及格")
if (80 <= score <= 90):
    print("良好")
if (90 <= score <= 100):
    print("优秀")
