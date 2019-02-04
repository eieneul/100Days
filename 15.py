"""
根据需求提取除了excel中需要的数据并存入新的excel中

"""


# -*- coding: utf-8 -*-
import xlrd
import xlwt

file = 'shoes.xlsx'

wb = xlrd.open_workbook(filename=file)
sheet1 = wb.sheet_by_index(0)
title = sheet1.row_values(0)
cols = sheet1.col_values(0)
print(title)
nrows = sheet1.nrows
# price
price_dic = {}
# size
size_dic = {}
# compute the sum of n_size for each
sum_size = {}
# type
type_dic = {}
for i in range(1, nrows):
    price_dic[sheet1.row_values(i)[0]] = sheet1.row_values(i)[3]
    name = sheet1.row_values(i)[0]
    size = sheet1.row_values(i)[1]
    n_size = sheet1.row_values(i)[2]
    type = sheet1.row_values(i)[5]
    if name not in size_dic:
        lst = []
        s = 0
        lst.append([size, n_size])
        size_dic[name] = lst
        if n_size:
            s = n_size
        sum_size[name] = s
        type_dic[name] = type
    else:
        lst.append([size, n_size])
        size_dic[name] = lst
        if n_size:
            s += n_size
            sum_size[name] = s
    print(sheet1.row_values(i))
print(size_dic)
print(sum_size)
print(type_dic)

f = xlwt.Workbook()
s1 = f.add_sheet(u'sheet1',cell_overwrite_ok=True)
row0 = [u'产品款号', u'小类', u'零售价', u'5', u'6', u'6.5', u'7', u'7.5', u'8', u'8.5', u'9', u'9.5', u'10', u'10.5', u'11', u'35', u'36',\
        u'37', u'38', u'39', u'40', u'41', u'42', u'43', u'44', u'45', u'46', u'47', u'48', u'总数量']
row0_index = {}

row0_index['产品编号'] = 0
row0_index['小类'] = 1
row0_index['零售价'] = 2
row0_index['总数量'] = 29
for i in range(3, len(row0)-1):
    row0_index[float(row0[i])] = i


print(row0_index)
# 生成第一行
for i in range(0, len(row0)):
    s1.write(0, i, row0[i])
row = 1
for key in size_dic:
    # write name
    s1.write(row, 0, key)
    # write price
    s1.write(row, 2, price_dic[key])
    # write size
    for i in size_dic[key]:
        if i[1]:
            if i[1] > 0:
                s1.write(row, row0_index[i[0]], i[1])
    # write sum
    s1.write(row, 29, sum_size[key])
    # write type
    s1.write(row, 1, type_dic[key])

    row += 1
f.save(u'鞋.xls')
