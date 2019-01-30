import getpass
import random
#
# username = input('请输入用户名：')
# # password = input('请输入口令: ')
# """
# 如果希望密码不被显示出来 可以使用getpass
# * 在pycharm中不能直接run getpass,用debug可以运行。
#
# """
# password = getpass.getpass('请输入密码：')
#
# real_password = 'wty0221'
#
# if username == 'admin' and password == real_password:
#     print('身份验证成功！')
# else:
#     print('身份验证失败！')


"""
三角形求面积（海伦公式） S = sqrt(p(p-a)(p-b)(p-c)), p = 1/2(a+b+c)

"""
import math

a = float(input('a:'))
b = float(input('b:'))
c = float(input('c:'))

if a+b>c or a+c>b or b+c>a:
    print('周长是%f' % (a+b+c))
    p = (a+b+c)/2
    area = math.sqrt(p*(p-a)*(p-b)*(p-c))
    print('面积%f' % area)
else:
    print("不能构成三角形")
