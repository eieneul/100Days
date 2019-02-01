"""
字符串和正则表达式

很好的教程推荐：https://deerchao.net/tutorials/regex/regex.htm

"""
# 常用元字符：
# . 匹配除换行符以外任意字符
# .* 任意字符可以重复任意次（也可以是0次 ）
# \d 数字
# \d+ 与*不同的是+必须重复至少一次
# \w 字母数字下划线或汉子
# \s 空白符
# \b 匹配单词的开始或者结束
# ^ 匹配字符串的开始
# $ 匹配字符串的结束
# ---------------------------------------
# 常见限定符：
# *	重复零次或更多次
# +	重复一次或更多次
# ?	重复零次或一次
# {n}	重复n次
# {n,}	重复n次或更多次
# {n,m}	重复n到m次
# ----------------------------------------
# 字符类
# 例如想匹配a,e,i,o,u 只需要[aeiou]就可以
# [0-9] == \d
# [a-z0-9A-Z] == \w
# ----------------------------------------
# 分支条件： |
# 用分隔符来分开不同的规则，从而增加约束
# 分组：()
# 重复多个字符用括号即可，例如： (0\d{2}){3}
# ----------------------------------------
# 反义：
# \W	匹配任意不是字母，数字，下划线，汉字的字符
# \S	匹配任意不是空白符的字符
# \D	匹配任意非数字的字符
# \B	匹配不是单词开头或结束的位置
# [^x]	匹配除了x以外的任意字符
# [^aeiou]	匹配除了aeiou这几个字母以外的任意字符

# 捕获
# (exp)	匹配exp,并捕获文本到自动命名的组里
# (?<name>exp)	匹配exp,并捕获文本到名称为name的组里，也可以写成(?'name'exp)
# (?:exp)	匹配exp,不捕获匹配的文本，也不给此分组分配组号
# 零宽断言
# (?=exp)	匹配exp前面的位置
# (?<=exp)	匹配exp后面的位置
# (?!exp)	匹配后面跟的不是exp的位置
# (?<!exp)	匹配前面不是exp的位置
# 注释
# (?#comment) 这种类型的分组不对正则表达式的处理产生任何影响，用于提供注释让人阅读
# 例如： (?<=\s)\d+(?=\s)匹配以空白符间隔的数字(不包括这些空白符)

"""
Python re模块的核心函数：

compile(pattern, flags=0)	                    编译正则表达式返回正则表达式对象
match(pattern, string, flags=0)	                用正则表达式匹配字符串 成功返回匹配对象 否则返回None
search(pattern, string, flags=0)	            搜索字符串中第一次出现正则表达式的模式 成功返回匹配对象 否则返回None
split(pattern, string, maxsplit=0, flags=0)	    用正则表达式指定的模式分隔符拆分字符串 返回列表
sub(pattern, repl, string, count=0, flags=0)	用指定的字符串替换原字符串中与正则表达式匹配的模式 可以用count指定替换的次数
fullmatch(pattern, string, flags=0)	            match函数的完全匹配（从字符串开头到结尾）版本
findall(pattern, string, flags=0)	            查找字符串所有与正则表达式匹配的模式 返回字符串的列表
finditer(pattern, string, flags=0)	            查找字符串所有与正则表达式匹配的模式 返回一个迭代器
purge()                     	                清除隐式编译的正则表达式的缓存
re.I / re.IGNORECASE	                        忽略大小写匹配标记
re.M / re.MULTILINE	                            多行匹配标记

"""

import re


def main_1():
    """
    验证输入用户名和QQ号是否有效并给出对应的提示信息

    要求：
    用户名必须由字母、数字或下划线构成且长度在6~20个字符之间
    QQ号是5~12的数字且首位不能为0

    """
    username = input('请输入用户名: ')
    qq = input('请输入QQ号: ')
    # match函数的第一个参数是正则表达式字符串或正则表达式对象
    # 第二个参数是要跟正则表达式做匹配的字符串对象
    m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$', username)
    if not m1:
        print('请输入有效的用户名.')
    m2 = re.match(r'^[1-9]\d{4,11}$', qq)
    if not m2:
        print('请输入有效的QQ号.')
    if m1 and m2:
        print('你输入的信息是有效的!')


def main_2():
    # 创建正则表达式对象 使用了前瞻和回顾来保证手机号前后不应该出现数字
    pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
    sentence = '''
    重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
    不是15600998765，也是110或119，王大锤的手机号才是15600998765。
    '''
    # 查找所有匹配并保存到一个列表中
    mylist = re.findall(pattern, sentence)
    print(mylist)
    print('--------华丽的分隔线--------')
    # 通过迭代器取出匹配对象并获得匹配的内容
    for temp in pattern.finditer(sentence):
        print(temp.group())
    print('--------华丽的分隔线--------')
    # 通过search函数指定搜索位置找出所有匹配
    m = pattern.search(sentence)
    while m:
        print(m.group())
        m = pattern.search(sentence, m.end())


def main_3():
    """简单的替换字符串中的和谐词"""

    sentence = '艹你大爷的，你他妈是不是傻叉啊？'
    purified = re.sub('[操肏艹]|fuck|shit|傻[比屄逼叉缺吊屌]|煞笔', '*', sentence, flags=re.I)
    print(purified)


def main_4():
    """拆分长字符串"""

    poem = '窗前明月光，疑是地上霜。举头望明月，低头思故乡。'
    sentence_list = re.split(r'[，。, .]', poem)
    print(sentence_list)  # ['窗前明月光', '疑是地上霜', '举头望明月', '低头思故乡', '']
    # split后list中会存在''，通过下面代码删除它
    while '' in sentence_list:
        sentence_list.remove('')
    print(sentence_list)  # ['窗前明月光', '疑是地上霜', '举头望明月', '低头思故乡']


if __name__ == '__main__':
    # main_1()
    # main_2()
    # main_3()
    main_4()
