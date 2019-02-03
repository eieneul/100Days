"""
进程和线程

"""

# Python中的多进程：
from multiprocessing import Process
from os import getpid
from random import randint
from time import sleep, time


def download_task(filename):
    print('启动下载进程，进程号[%d]' % getpid())
    print('开始下载%s...' % filename)
    time_to_download = randint(2, 6)
    sleep(time_to_download)
    print('%s下载完成！耗时%d秒' % (filename, time_to_download))


def main_1():
    start = time()
    p1 = Process(target=download_task, args=('Python新手入门.pdf', ))
    p1.start()
    p2 = Process(target=download_task, args=('Happy New Year.mp4', ))
    p2.start()
    p1.join()
    p2.join()

    end = time()
    print('总共耗时%.2f秒。' % (start - end))


# 实现两个进程间的通信
from multiprocessing import Queue


def task_2(msg, q):
    counter = q.get()
    while counter < 10:
        print(msg, end='', flush=True)
        """
        这里的flush简单说就是将缓存里面的内容立即输出到标准输出流
        大多用于服务端，类似web的即时聊天，为了实时返回不能等请求之后再显示内容        
        
        """
        counter += 1
        q.put(counter)
        sleep(0.01)


def main_2():
    q = Queue()
    q.put(0)
    p1 = Process(target=task_2, args=('Ping', q, ))
    p2 = Process(target=task_2, args=('Pong', q, ))
    p1.start()
    p2.start()
    p1.join()
    p2.join()


# Python中的多线程
from random import randint
from threading import Thread
from time import time, sleep


def main_3():
    start = time()
    t1 = Thread(target=download_task, args=('xxx.pdf', ))
    t1.start()
    t2 = Thread(target=download_task, args=('123.avi', ))
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('Total time is: %.2f' % (end - start))

# 100人向同一个账户同时存1元钱, 由于多个线程同时使用同一个功能，初始balance都是0，
# 所以每个账户都会在此基础上+1，结果必然远小于100。此时需要用到“锁”来保证一个线程用完
# 之后才会释放该功能给其他线程使用。
from time import sleep
from threading import Thread, Lock


class Account(object):

    def __init__(self):
        self._balance = 0
        self._lock = Lock()

    def deposit(self, money):
        # 先获取锁才能执行后续的代码
        self._lock.acquire()
        try:
            new_balance = self._balance + money
            sleep(0.01)
            self._balance = new_balance
        finally:
            # 在finally中执行释放锁的操作保证正常异常锁都能释放
            self._lock.release()

    @property
    def balance(self):
        return self._balance


class AddMoneyThread(Thread):

    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        self._account.deposit(self._money)


def main_4():
    account = Account()
    threads = []
    for _ in range(100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print('账户余额为: ￥%d元' % account.balance)

# 练习
from multiprocessing import Process, Queue
from random import randint
from time import time


def task_handler(curr_list, result_queue):
    total = 0
    for number in curr_list:
        total += number
    result_queue.put(total)


def main():
    processes = []
    number_list = [x for x in range(1, 100000001)]
    result_queue = Queue()
    index = 0
    # 启动8个进程将数据切片后进行运算
    for _ in range(8):
        p = Process(target=task_handler,
                    args=(number_list[index:index + 12500000], result_queue))
        index += 12500000
        processes.append(p)
        p.start()
    # 开始记录所有进程执行完成花费的时间
    start = time()
    for p in processes:
        p.join()
    # 合并执行结果
    total = 0
    while not result_queue.empty():
        total += result_queue.get()
    print(total)
    end = time()
    print('Execution time: ', (end - start), 's', sep='')


if __name__ == '__main__':
    # main_1()
    # main_2()
    # main_3()
    # main_4()
    main()
