"""
面向对象编程基础
<类>

"""


# 首先定义一个类
class Student:
    def __init__(self, name, age):
        self.__name = name
        self.age = age

    def study(self, course_name):
        print('%s正在学习%s.' % (self.__name, course_name))

    def watch_av(self):
        if self.age < 18:
            print('%s只能观看《熊出没》.' % self.__name)
        else:
            print('%s正在观看岛国爱情动作片.' % self.__name)


# 当类定义完成后，我们可以创建对象并给对象发消息
def main1():
    # 创建学生对象并指定姓名和年龄
    stu1 = Student('Tom', 15)
    stu2 = Student('Caspar', 19)
    # 给对象发消息
    stu1.study('Python Algorithm')
    stu2.study('Art Design')
    # 给对象发watch_av消息
    stu1.watch_av()
    stu2.watch_av()


# 属性名以单下划线开头，用来表示属性是受保护的
# 练习 1： 定义一个类 描述数字时钟
class Clock:

    """数字时钟"""
    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second

    def run(self):
        """走字"""
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def __str__(self):
        """显示"""
        return '%02d:%02d:%02d' % \
               (self._hour, self._minute, self._second)


def main_clock():
    from time import sleep

    clock = Clock(23, 59, 58)
    while True:
        print(clock)
        sleep(1)
        clock.run()


# 练习 2： 定义一个类描述平面上的点并提供移动点和计算到另一个点距离的方法。
from math import sqrt

class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move_to(self, x, y):
        self.x = x
        self.y = y

    def move_by(self, dx, dy):
        """
        移动指定的增量

        :param dx: 横坐标的增量
        "param dy: 纵坐标的增量
        """
        self.x += dx
        self.y += dy

    def distance_to(self, other):
        dx = other.x - self.x
        dy = other.y - self.y
        return sqrt(dx**2 + dy**2)

    def __str__(self):
        return '(%s, %s)' % (str(self.x), str(self.y))


def main_p():
    p1 = Point(3, 5)
    p2 = Point()
    print(p1)
    print(p2)
    p2.move_by(-1, 2)
    print(p2)
    print(p1.distance_to(p2))

if __name__ == '__main__':
    # main1()
    # main_clock()
    main_p()
