"""
函数和模块的使用

"""


def combination():
    """
    根据input: M, N
    求组合C(M,N)的值

    """
    def factorial(num):
        """
        写出阶乘函数供循环使用
        :param num: 非负整数
        :return: num的阶乘
        """
        result = 1
        for i in range(1, num + 1):
            result *= i
        return result

    m = int(input('m: '))
    n = int(input('n: '))
    print('C(M,N)=', factorial(m) // factorial(n) // factorial(m-n))


"""
在Python中，函数的参数可以有默认值，也支持使用可变参数，
所以Python并不需要像其他语言一样支持函数的重载，
因此我们在定义一个函数的时候可以让它有多种不同的使用方式。

"""
from random import randint


def roll_dice(n=2):
    """
    摇色子

    :param n: 色子的个数
    :return: n颗色子点数之和
    """
    total = 0
    for _ in range(n):
        total += randint(1, 6)
    return total


def add(a=0, b=0, c=0):
    return a*2 + b + c


# 如果没有指定参数那么使用默认值摇两颗色子
print(roll_dice())
# 摇三颗色子
print(roll_dice(3))
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
# 传递参数时可以不按照设定的顺序进行传递
print(add(c=50, a=100, b=200))


"""
上述中的add函数，有一种更方便的写法可以允许我们随意指定参数的数量

"""
# 在参数名前面的*表示args是一个可变参数
# 即在调用add函数时可以传入0个或多个参数
def add_2(*args):
    total = 0
    for val in args:
        total += val
    return total


print(add_2())
print(add_2(1))
print(add_2(1, 2))
print(add_2(1, 2, 3))
print(add_2(1, 3, 5, 7, 9))
