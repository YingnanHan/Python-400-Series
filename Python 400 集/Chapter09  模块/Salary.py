# coding:utf-8
"""
02
用于计算公司员工的工资

"""

company = "Baidu"


def yearSalary(monthSalary):
    """根据传入的月薪的值，计算出年薪,monthSalary*12"""
    return monthSalary * 12


def daySalary(monthSalary):
    """根据传入的月薪值，计算出一天的薪资。一个月按照22.5天计算(国家规定的工作日)"""
    return monthSalary / 22.5


if __name__ == '__main__':
    print(daySalary(100))
