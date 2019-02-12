"""
函数的使用方法


"""
from functools import wraps
from time import time


def record_time(func):
    """自定义装饰函数的装饰器"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        print(f'{func.__name__}: {time() - start}秒')
        return result

    return wrapper


def record(output):
    """自定义带参数的装饰器"""

    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time()
            result = func(*args, **kwargs)
            output(func.__name__, time() - start)
            return result

        return wrapper

    return decorate


def hello():
    for i in range(10):
        print('hello')


record(hello)


def singleton(cls):
    """线程安全的单例装饰器"""
    instances = {}
    locker = Lock()

    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instances:
            with locker:
                if cls not in instances:
                    instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper
