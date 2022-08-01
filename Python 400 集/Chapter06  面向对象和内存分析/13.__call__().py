# 定义了__call__()方法的对象成为可调用对象，就是这个对象可以像函数一样被调用


# 测试可调用方法 __call__()

class SalaryAccount:
    """
    工资计算类
    """

    def __call__(self, salary):
        print("正在计算工资...")
        yearSalary = salary * 12

        daySalary = salary // 22.5  # 国家规定的每月平均工作天数22.5天
        hourSalary = daySalary // 8
        return dict(yearSalary=yearSalary, monthSalary=salary, daySalary=daySalary, hourSalary=hourSalary)


s = SalaryAccount()
print(s(3000))
# 当直接义函数的方式时用类对象的时候间接调用的就是__call__()函数
# 可以通过修改__call__()来设定调用类对象时的行为
