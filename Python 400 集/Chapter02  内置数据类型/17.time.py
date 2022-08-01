import time

# 返回1970年1月1号开始到现在经过的时间
print(time.time())

# other operations  求解1970年到今天为止经过的 秒数 分钟数 小时数 天数 年数
totalMinutes = int(time.time() // 60)
print(totalMinutes)
print(totalMinutes / 60)
print(totalMinutes / 60 / 24)
print(totalMinutes / 60 / 24 / 365)
