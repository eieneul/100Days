"""
面向对象相关知识

"""

# 三大支柱：封装，继承，多态

"""
月薪结算系统 - 部门经理每月15000 程序员每小时200 销售员3800底薪加销售额5%提成
"""
from abc import ABCMeta, abstractmethod


class Employee(metaclass=ABCMeta):
    """员工：抽象类"""
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @abstractmethod
    def get_salary(self):
        """结算月薪（抽象类）"""
        pass


class Manager(Employee):
    """部门经理"""
    def get_salary(self):
        return 15000.0


class Programmer(Employee):
    """程序员"""
    def __init__(self, name):
        self._working_hour = 0
        super().__init__(name)

    @property
    def working_hour(self):
        """工作时间"""
        return self._working_hour

    @working_hour.setter
    def working_hour(self, hour):
        self._working_hour = hour if hour > 0 else 0

    def get_salary(self):
        return 200.0 * self._working_hour


class Salesman(Employee):
    """销售员"""
    def __init__(self, name):
        self._sales = 0.0
        super().__init__(name)

    @property
    def sales(self):
        return self._sales

    @sales.setter
    def sales(self, sales):
        self._sales = sales if sales > 0 else 0

    def get_salary(self):
        return 3800.0 + self._sales * 0.05


class EmployeeFactory():
    """创建员工的工厂（工厂模式-通过工厂实现对象使用者和对象之间的解耦合）"""
    @staticmethod
    def create(emp_type, *args):
        """创建员工"""
        emp_type = emp_type.upper()
        emp = None
        if emp_type == 'M':
            emp = Manager(*args)
        elif emp_type == 'P':
            emp = Programmer(*args)
        elif emp_type == 'S':
            emp = Salesman(*args)
        return emp


def main():
    emps = [
        EmployeeFactory.create('M', 'Tim'), EmployeeFactory.create('P', 'Bob'),
        EmployeeFactory.create('P', 'Jack'), EmployeeFactory.create('S', 'Todd')
    ]
    for emp in emps:
        # 用isinstance函数识别对象引用所引用对象的类型
        if isinstance(emp, Programmer):
            emp.working_hour = int(input('本月工作时间： '))
        elif isinstance(emp, Salesman):
            emp.sales = float(input('本月销售额： '))
        print('%s: %.2f元' % (emp.name, emp.get_salary()))


if __name__ == '__main__':
    main()
