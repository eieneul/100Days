"""
input， int， 占位符的使用

"""

# a = int(input('a = '))
# b = int(input('b = '))
#
# print("%d + %d = %d" % (a, b, a+b))
# # %f is float: 103/10 = 10.3, %d is integer: 103/10=10
# print("%d / %d = %f" % (a, b, a/b))
# print("%d // %d = %d" % (a, b, a//b))
#
#
# # a = '4.3'
# # if '.' in a:
# #     print(float(a))

#
# a = 1 + 5j
# print(type(a))

"""
exercise
"""
f = float(input("华氏度： "))
c = (f - 32) / 1.8
print('%.1f 华氏度 = %.1f 摄氏度' % (f, c))
