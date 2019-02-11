"""
数据结构与算法

排序算法：冒泡排序，归并排序
查找算法：顺序查找，折半查找

"""


# 冒泡排序
def bubble_sort(original_list):
    temp_list = original_list[:]
    for i in range(len(temp_list) - 1):
        for j in range(len(temp_list) - i - 1):
            if temp_list[j] > temp_list[j + 1]:
                temp_list[j], temp_list[j + 1] = temp_list[j + 1], temp_list[j]
    return temp_list


# 归并排序（先拆分让子序列有序，后合并）
def merge_sort(items, comp=lambda x, y: x <= y):
    if len(items) < 2:
        return items[:]
    mid = len(items) // 2
    left = merge_sort(items[:mid], comp)
    right = merge_sort(items[mid:], comp)
    return merge(left, right, comp)


def merge(item1, item2, comp=lambda x, y: x <= y):
    result = []
    idx1, idx2 = 0, 0
    while idx1 < len(item1) and idx2 < len(item2):
        if comp(item1[idx1], item2[idx2]):
            result.append(item1[idx1])
            idx1 += 1
        else:
            result.append(item2[idx2])
            idx2 += 1
    result += item1[idx1:]
    result += item2[idx2:]
    return result


# 顺序查找
def seq_search(items, key):
    for index, item in enumerate(items):
        if item == key:
            return index
    return -1


# 折半查找
def bin_search(items, key):
    start, end = 0, len(items) - 1
    while start <= end:
        mid = (start + end) // 2
        if key > items[mid]:
            start = mid + 1
        elif key < items[mid]:
            end = mid - 1
        else:
            return mid
    return -1


if __name__ == '__main__':
    print(bubble_sort([5, 3, 7, 2, 11]))
    print(merge_sort([5, 3, 7, 2, 11]))
    print(seq_search([5, 3, 7, 2, 11], 7))
    print(bin_search([5, 3, 7, 2, 11], 7))


# 生成式（推导式）语法：
prices = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
}
# 用股票价格大于100元的股票构造一个新的字典
prices2 = {key: value for key, value in prices.items() if value > 100}
print(prices2)


# 嵌套列表
def qian_tao_list():
    names = ['关羽', '张飞', '赵云', '马超', '黄忠']
    courses = ['语文', '数学', '英语']
    # 错误 - 参考http://pythontutor.com/visualize.html#mode=edit
    # scores = [[None] * len(courses)] * len(names)
    scores = [[None] * len(courses) for _ in range(len(names))]
    for row, name in enumerate(names):
        for col, course in enumerate(courses):
            scores[row][col] = float(input(f'请输入{name}的{course}成绩： '))
            print(scores)


# heapq, itertools等的用法：
import heapq
"""
从列表中找出最大的或最小的N个元素
"""
import heapq

list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
list2 = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
print(heapq.nlargest(3, list1))
print(heapq.nsmallest(3, list1))
print(heapq.nlargest(2, list2, key=lambda x: x['price']))
print(heapq.nlargest(2, list2, key=lambda x: x['shares']))

"""
排列 / 组合 / 笛卡尔积
"""
import itertools

for val in itertools.permutations('ABCD'):
    print(val)

for val in itertools.combinations('ABCDE', 3):
    print(val)

for val in itertools.product('ABCD', '123'):
    print(val)
