# getter&setter方法用来设置获取类内部的私有方法

# class Employee:
#
#     def __init__(self,name,salary):
#         self.__name = name
#         self.__salary = salary
#
#     def get_salary(self):
#         return self.__salary
#
#     def set_salary(self,salary):
#         if 1000<salary<500000:
#             self.__salary = salary
#         else:
#             print("录入错误，请将录入的金额限定在1000-500000范围内！")
#
# emp1 = Employee("Mike",3000)
# print(emp1.get_salary())
# emp1.set_salary(2000)
# print(emp1.get_salary())

# 使用@property来实现同样的功能


class Employee:

    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    # 经过如下的操作之后，在以获取salary属性的时就可以将其直接作为一个属性来使用
    @property
    def salary(self):
        return self.__salary

    # 表示针对salary属性的设置,这样一来salary就可以真正类似属性的被使用
    @salary.setter
    def salary(self, salary):
        if 1000 < salary < 500000:
            self.__salary = salary
        else:
            print("录入错误，请将录入的金额限定在1000-500000范围内！")


print(Employee.salary)
emp1 = Employee("Mike", 3000)
print(emp1.salary)
emp1.salary = 5000
print(emp1.salary)
