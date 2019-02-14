"""
并发编程：多线程，多进程，异步I/O

并发编程的好处在于可以提升程序的执行效率以及改善用户体验；
坏处在于并发的程序不容易开发和调试，同时对其他程序来说它并不友好。

"""
# 进程和线程的区别和联系？
# 进程 - 操作系统分配内存的基本单位 - 一个进程可以包含一个或多个线程
# 线程 - 操作系统分配CPU的基本单位


# ----多线程----
"""
启动5个线程向账户中存钱，5个线程从账户中取钱，取钱时如果余额不足就暂停线程进行等待。
为了达到上述目标，需要对存钱和取钱的线程进行调度，在余额不足时取钱的线程暂停并释放锁，
而存钱的线程将钱存入后要通知取钱的线程，使其从暂停状态被唤醒。可以使用threading模块的
Condition来实现线程调度，该对象也是基于锁来创建的。

多个线程竞争一个资源 - 保护临界资源 - 锁（Lock/RLock）
多个线程竞争多个资源（线程数>资源数） - 信号量（Semaphore）
多个线程的调度 - 暂停线程执行/唤醒等待中的线程 - Condition
"""
from concurrent.futures import ThreadPoolExecutor
from random import randint
from time import sleep

import threading


class Account():
    """银行账户"""

    def __init__(self, balance=0):
        self.balance = balance
        lock = threading.Lock()
        self.condition = threading.Condition(lock)

    def withdraw(self, money):
        """取钱"""
        with self.condition:
            while money > self.balance:
                self.condition.wait()
            new_balance = self.balance - money
            sleep(0.001)
            self.balance = new_balance

    def deposit(self, money):
        """存钱"""
        with self.condition:
            new_balance = self.balance + money
            sleep(0.001)
            self.balance = new_balance
            self.condition.notify_all()


def add_money(account):
    while True:
        money = randint(5, 10)
        account.deposit(money)
        print(threading.current_thread().name,
              ':', money, '====>', account.balance)
        sleep(0.5)


def sub_money(account):
    while True:
        money = randint(10, 30)
        account.withdraw(money)
        print(threading.current_thread().name,
              ':', money, '<====', account.balance)
        sleep(1)


def main_1():
    account = Account()
    with ThreadPoolExecutor(max_workers=10) as pool:
        for _ in range(5):
            pool.submit(add_money, account)
            pool.submit(sub_money, account)


# ----多进程----
"""
多进程可以有效的解决GIL的问题，实现多进程主要的类是Process，其他辅助的类跟threading模块中的类似，
进程间共享数据可以使用管道、套接字等，在multiprocessing模块中有一个Queue类，它基于管道和锁机制提供了多个进程共享的队列。
"""
import concurrent.futures
import math

PRIMES = [
    1116281,
    1297337,
    104395303,
    472882027,
    533000389,
    817504243,
    982451653,
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419
] * 5


def is_prime(n):
    """判断素数"""
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


def main_2():
    """主函数"""
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print('%d is prime: %s' % (number, prime))


# 以下情况需要使用多线程：
#
# 1.程序需要维护许多共享的状态（尤其是可变状态），Python中的列表、字典、集合都是线程安全的，所以使用线程而不是进程维护共享状态的代价相对较小。
# 2.程序会花费大量时间在I / O操作上，没有太多并行计算的需求且不需占用太多的内存。

# 以下情况需要使用多进程：
#
# 1.程序执行计算密集型任务（如：字节码操作、数据处理、科学计算）。
# 2.程序的输入可以并行的分成块，并且可以将运算结果合并。
# 3.程序在内存使用方面没有任何限制且不强依赖于I / O操作（如：读写文件、套接字等）。


# ----异步处理----
"""
异步处理：从调度程序的任务队列中挑选任务，该调度程序以交叉的形式执行这些任务，
我们并不能保证任务将以某种顺序去执行，因为执行顺序取决于队列中的一项任务是否愿
意将CPU处理时间让位给另一项任务。异步任务通常通过多任务协作处理的方式来实现，
由于执行时间和顺序的不确定，因此需要通过回调式编程或者future对象来获取任务执行的结果。
Python3通过asyncio模块和await和async关键字（在Python 3.7中正式被列为关键字）来支持异步处理。

"""
# https://github.com/jackfrued/Python-100-Days/blob/master/Day16-20/Python%E8%AF%AD%E8%A8%80%E8%BF%9B%E9%98%B6.md
import asyncio


def num_generator(m, n):
    """指定范围的数字生成器"""
    yield from range(m, n + 1)


async def prime_filter(m, n):
    """素数过滤器"""
    primes = []
    for i in num_generator(m, n):
        flag = True
        for j in range(2, int(i ** 0.5 + 1)):
            if i % j == 0:
                flag = False
                break
        if flag:
            print('Prime =>', i)
            primes.append(i)

        await asyncio.sleep(0.001)
    return tuple(primes)


async def square_mapper(m, n):
    """平方映射器"""
    squares = []
    for i in num_generator(m, n):
        print('Square =>', i * i)
        squares.append(i * i)

        await asyncio.sleep(0.001)
    return squares


def main_3():
    """主函数"""
    loop = asyncio.get_event_loop()
    future = asyncio.gather(prime_filter(2, 100), square_mapper(1, 100))
    future.add_done_callback(lambda x: print(x.result()))
    loop.run_until_complete(future)
    loop.close()



if __name__ == '__main__':
    # main_1()
    # main_2()
    main_3()
