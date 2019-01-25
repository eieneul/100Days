"""
<字符串和常用数据结构>

值得注意的tips: string.title()是把字符串中每一个单词的首字母大写，
而string.capitalize()则是只把字符串的第一个字母大写！

"""


def f1():
    str1 = 'hello world'
    # 获得字符串首字母大写
    print(str1.capitalize())
    # 字符串全部变大
    print(str1.upper())
    # 查找子串位置，不存在的内容为-1
    print(str1.find('or'))
    print(str1.find('shit'))
    # 与find类似的方法 找不到时会返回异常
    print(str1.index('or'))
    # print(str1.index('shit'))
    # 检查字符串是否以指定字符串为开头/结尾
    print(str1.startswith('hel'))
    print(str1.startswith('x'))
    print(str1.endswith('d'))

    # 将字符串以指定的宽度居中并在两侧填充指定的字符
    print(str1.center(30, '*'))
    # 将字符串以指定的宽度靠右放置左侧填充指定的字符
    print(str1.rjust(20, '-'))

    str2 = 'abc123456'
    # 取字符串中指定位置字符（用下标操作）
    print(str2[3])
    # 字符串切片
    print(str2[2:5])  # c12
    print(str2[2:])  # c123456
    print(str2[2::2])  # c246
    print(str2[::2])  # ac246
    print(str2[::-1])  # 654321cba
    print(str2[-3:-1])  # 45
    # 检查字符串是否由数字构成
    print(str2.isdigit())  # False
    # 检查字符串是否以字母构成
    print(str2.isalpha())  # False
    # 检查字符串是否以数字和字母构成
    print(str2.isalnum())
    str3 = '  eieneul@yahoo.com '
    print(str3)
    # 获得字符串修剪左右两侧空格的拷贝
    print(str3.strip())


def f1_2():
    # 列表的创建和下标
    l = [1,3,5,7,10]
    l1 = ['hello'] * 5
    print(l1)
    l[2] = 250
    print(l)
    # 添加元素
    l.append(73)
    l.insert(1, 100)
    l += ['a', 'b']
    print(l)
    # 删除元素
    l.remove('a')
    print(l)
    del l[-1]
    print(l)
    # 清空列表
    l1.clear()
    print(l1)


# 列表同样可以进行切片操作
def f2():
    fruits = ['grape', 'apple', 'strawberry', 'waxberry']
    fruits += ['pitaya', 'pear', 'mango']
    print(fruits)
    for fruit in fruits:
        print(fruit.title(), end=' ')
    print()
    print(fruits[::4])
    # copy list
    fruits2 = fruits[:]
    print(fruits2)
    # reversed list
    fruits3 = fruits[::-1]
    print(fruits3)


# 列表排序操作
def f3():
    l1 = ['C', 'A11111111111', 'B', 'Xba', 'Nacd']
    l2 = sorted(l1)
    print(l2)
    # 参数 reverse=True 将字母序的列表反转
    l3 = sorted(l1, reverse=True)
    print(l3)
    # 参数 key=len 根据字符串长度排序
    l4 = sorted(l1, key=len, reverse=False)
    print(l4)


def f4():


    return

if __name__ == '__main__':
    # f1()
    # f2()
    # f3()
    # f1_2()
    f4()
