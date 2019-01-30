"""
文件和异常

"""


def main_1():
    f = None
    try:
        f = open('xxx.txt', 'r', encoding='utf-8')
        print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件!')
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')
    finally:
        if f:
            f.close()

"""
我们通常把finally块称为“总是执行代码块”，它最适合用来做释放外部资源的操作。
如果不愿意在finally代码块中关闭文件对象释放资源，也可以使用上下文语法，
通过with关键字指定文件对象的上下文环境并在离开上下文环境时自动释放文件资源

"""

# 3种读文件方法
def read():
    # 一次性读取整个文件内容
    with open('xxx.txt', 'r', encoding='utf-8') as f:
        print(f.read())

    # 通过for-in循环逐行读取
    with open('xxx.txt', mode='r') as f:
        for line in f:
            print(line, end='')
    print()

    # 读取文件按行读取到列表中
    with open('xxx.txt') as f:
        lines = f.readlines()
    print(lines)


# 执行复制一张图片 (二进制编码'b'读取)
def main_copy():
    try:
        with open('sample.jpg', 'rb') as fs1:
            data = fs1.read()
            print(type(data))  # <class 'bytes'>
        with open('copy.jpg', 'wb') as fs2:
            fs2.write(data)
    except FileNotFoundError:
        print('指定的文件无法打开')
    except IOError:
        print('读写文件时出现错误')
    print('搞定！')


# 分别写入不同的文件
def main_2():
    filenames = ('a.txt', 'b.txt', 'c.txt')
    fs_list = []
    try:
        for filename in filenames:
            fs_list.append(open(filename, 'w', encoding='utf-8'))
        for number in range(1, 10000):
            if number < 100:
                fs_list[0].write(str(number) + '\n')
            elif number < 1000:
                fs_list[1].write(str(number) + '\n')
            else:
                fs_list[2].write(str(number) + '\n')
    except IOError as ex:
        print(ex)
        print('写文件时发生错误!')
    finally:
        for fs in fs_list:
            fs.close()
    print('操作完成!')


# JSON文件读写
import json


def main_json():
    my_data = {
        'name': 'James',
        'age': 18,
        'email': '123@qq.com',
        'friends': ['Tim', 'Alice'],
        'cars': [
            {'brand': 'Ford', 'max_speed': 220},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }
    try:
        with open('car_data.json', 'w', encoding='utf-8') as f:
            json.dump(my_data, f)
    except IOError as e:
        print(e)
    print('Data has been collected!')


"""
json模块主要有四个比较重要的函数，分别是：

dump - 将Python对象按照JSON格式序列化到文件中
dumps - 将Python对象处理成JSON格式的字符串
load - 将文件中的JSON数据反序列化成对象
loads - 将字符串的内容反序列化成Python对象

"""


if __name__ == '__main__':
    # main_copy()
    main_json()
