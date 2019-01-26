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


# list & sort
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
    import sys
    f = [x for x in range(1, 10)]
    print(f)
    f = [x+y for x in 'ABCDE' for y in '1234567']
    print(f)
    # 用列表的生成表达式语法创建列表容器
    # 用这种语法创建列表之后元素已经准备就绪所以需要耗费较多的内存空间
    f = [x ** 2 for x in range(1, 1000)]
    print(sys.getsizeof(f))  # 查看对象占用内存的字节数
    print(f)
    # 请注意下面的代码创建的不是一个列表而是一个生成器对象
    # 通过生成器可以获取到数据但它不占用额外的空间存储数据
    # 每次需要数据的时候就通过内部的运算得到数据(需要花费额外的时间)
    f = (x ** 2 for x in range(1, 1000))
    print(sys.getsizeof(f))  # 相比生成式生成器不占用存储数据的空间
    print(f)
    for val in f:
        print(val)
    return


def fib1(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def fib2(n):
    # yield
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a

# tuple
"""
这里有一个非常值得探讨的问题，我们已经有了列表这种数据结构，为什么还需要元组这样的类型呢？

元组中的元素是无法修改的，事实上我们在项目中尤其是多线程环境（后面会讲到）中可能更喜欢使用的是那些不变对象
（一方面因为对象状态不能修改，所以可以避免由此引起的不必要的程序错误，简单的说就是一个不变的对象要比可变的
对象更加容易维护；另一方面因为没有任何一个线程能够修改不变对象的内部状态，一个不变对象自动就是线程安全的，
这样就可以省掉处理同步化的开销。一个不变对象可以方便的被共享访问）。所以结论就是：如果不需要对元素进行添加、
删除、修改的时候，可以考虑使用元组，当然如果一个方法要返回多个值，使用元组也是不错的选择。
元组在创建时间和占用的空间上面都优于列表。我们可以使用sys模块的getsizeof函数来检查存储同样的元素的元组和
列表各自占用了多少内存空间，这个很容易做到。

"""
def f5():
    import sys
    # tuple takes less space in memory than list
    l = [1,2,3,4,5]
    t = (1,2,3,4,5)
    print(sys.getsizeof(l))
    print((sys.getsizeof(t)))

# set
def f6():
    # 集合会删除重复元素
    set1 = {1, 2, 3, 3, 3, 2}
    print(set1)
    print('Length =', len(set1))
    set2 = set(range(1, 10))
    print(set2)
    set1.add(4)
    set1.add(5)
    set2.update([11, 12])
    print(set1)
    print(set2)
    # remove移除不存在元素时会报错，discard不报错
    set2.discard(5)
    print(set2)
    set2.pop()
    print(set2)
    # 集合的交集、并集、差集、对称差运算
    # 交
    print(set1 & set2)
    print(set1.intersection(set2))
    # 并
    print(set1 | set2)
    print(set1.union(set2))
    # 差
    print(set1 - set2)
    print(set1.difference(set2))
    # 对称差
    print(set1 ^ set2)
    print(set1.symmetric_difference(set2))
    # 判断子集和超集
    print(set1 <= set2)
    print(set1.issubset(set2))
    print(set1 >= set2)
    print(set1.issuperset(set2))


# dictionary: stored as {key: value}
def f7():
    scores = {'骆昊': 95, '白元芳': 78, '狄仁杰': 82}
    for elem in scores:
        print('%s\t--->\t%d' % (elem, scores[elem]))
    scores['白元芳'] = 65
    scores['诸葛王朗'] = 71
    scores.update(冷面=67, 方启鹤=85)
    print(scores)
    if '武则天' in scores:
        print(scores['武则天'])
    print(scores.get('武则天'))
    # get方法也是通过键获取对应的值但是可以设置默认值
    print(scores.get('武则天', 60)) # 但其实字典里并未添加 武则天：60
    print(scores)
    # 删除元素
    print(scores.popitem()) # 删除最后一组key:val 并返回
    print(scores.popitem())
    print(scores.pop('白元芳'))
    print(scores)
    # 清空
    scores.clear()
    print(scores)


if __name__ == '__main__':
    # f1()
    # f2()
    # f3()
    # f1_2()
    # f4()8
    # print(fib1(8))

    # for val in fib2(8):
    #     print(val)
    # f5()
    # f6()
    f7()
