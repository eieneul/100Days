"""
猜数字游戏
计算机出一个1~100之间的随机数由人来猜
计算机根据人猜的数字分别给出提示大一点/小一点/猜对了

"""

# import random
#
# answer = random.randint(1, 100)
# counter = 0
# while True:
#     counter += 1
#     number = int(input('Input an integer: '))
#     if number < answer:
#         print('Please input a larger number.')
#     elif number > answer:
#         print('Please input a smaller number.')
#     else:
#         print('Awesome!')
#         break
# print('You have tried %d times.' % counter)

"""
九九乘法表

"""
for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d*%d=%d' % (i, j, i * j), end='\t')
    print()
