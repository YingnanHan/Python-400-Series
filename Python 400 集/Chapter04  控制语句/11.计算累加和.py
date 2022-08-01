# 计算1-100之间的累加和，奇数累加和，偶数累加和
sum_all = 0
sum_even = 0
sum_odd = 0

for i in range(100):
    sum_all += i
    if i % 2 == 0:
        sum_even += i
    else:
        sum_odd += i

print("0-100以内的累加和：{0}，奇数和：{1}，偶数和：{2}".format(sum_all, sum_odd, sum_even))
