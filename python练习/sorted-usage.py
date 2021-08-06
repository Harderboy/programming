"""
sorted() 函数对所有可迭代的对象进行排序操作。

「sorted()函数增加了key参数来指定一个函数，此函数将在可迭代对象的每个元素比较前被调用,它接受一个参数并返回一个用于排序的键。」

语法
    sorted(iterable, key=None, reverse=False)
参数说明:
    iterable -- 可迭代对象。
    key -- 主要是用来接收函数来实现自定义排序规则，具体的函数的参数就是取自于可迭代对象中的元素
    reverse -- 排序规则，reverse = True 降序 ， reverse = False 升序（默认）按照ASCII码表的顺序排列的
返回值:
    返回重新排序的列表。

参考链接
    https://www.runoob.com/python3/python-sort-dictionaries-by-key-or-value.html
    https://blog.csdn.net/qq_22022063/article/details/79019294
    https://www.cnblogs.com/ajianbeyourself/p/5395653.html
"""
# 元组列表排序
from operator import itemgetter
student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]

# sort by age
# func=lambda student:student[2]
# def func(student):
#     return student[2]

student_sorted = sorted(student_tuples, key=lambda student: student[2])
# [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
print(student_sorted)


# python3中sorted没有cmp这个参数
# L = [('a', 3), ('d', 2), ('c', 1), ('b', 4)]
# a = sorted(L, cmp=lambda x, y : cmp(x[0], y[0]))
# b = sorted(L, cmp=lambda x, y : cmp(x[1], y[1]))
# print(a)
# print(b)

# 字典排序
# 字典，字典是一个无序的数据结构
sys = {'name': '张三',
       'age': '十八',
       'gender': 'man'}
# 1.根据字典的key排序
# 单独打印出排序后的key值
new_sys = sorted(sys)
print(new_sys)  # [1, 2, 3, 4, 5]

# sorted() 函数可以接收任何的 iterable。对字典的key进行排序，因为key值是唯一的，返回值为重新排序的列表
list13 = sorted({1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'})
print(list13)  # [1, 2, 3, 4, 5]

# 根据key的升序排列，把key value都打印出来
new_sys1 = sorted(sys.items(), key=lambda d: d[0], reverse=False)
print(new_sys1)  # [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

# 2.根据字典的value值进行排序
# 单独打印出排序后的value值
new_sys1 = sorted(sys.values())
print(new_sys1)

# 打印出根据value排序后的键值对的具体值
new_sys2 = sorted(sys.items(), key=lambda d: d[1], reverse=False)
print(new_sys2)


# 字典列表排序
lis = [{"name": "Taobao", "age": 100},
       {"name": "Runoob", "age": 7},
       {"name": "Google", "age": 100},
       {"name": "Wiki", "age": 200}]

# 通过 age 升序排序
print("列表通过 age 升序排序: ")
print(sorted(lis, key=lambda i: i['age']))

print("\r")


# 多列排序
# 先按 age 排序，age相同的再按 name 排序
print("列表通过 age 和 name 排序: ")
# [{'name': 'Runoob', 'age': 7}, {'name': 'Google', 'age': 100}, {'name': 'Taobao', 'age': 100}, {'name': 'Wiki', 'age': 200}]
print(sorted(lis, key=lambda i: (i['age'], i['name'])))

# 先按照成绩降序排序，相同成绩的按照名字升序排序：
d1 = [{'name': 'alice', 'score': 38}, {'name': 'bob', 'score': 18},
      {'name': 'darl', 'score': 28}, {'name': 'christ', 'score': 28}]
l = sorted(d1, key=lambda x: (-x['score'], x['name']))
print(l)  # [{'name': 'alice', 'score': 38}, {'name': 'christ', 'score': 28}, {'name': 'darl', 'score': 28}, {'name': 'bob', 'score': 18}]

print("\r")

# 按 age 降序排序
print("列表通过 age 降序排序: ")
print(sorted(lis, key=lambda i: i['age'], reverse=True))


# 使用operator.itemgetter

"""
a = [1,2,3]
b = [[1,2,3],[4,5,6],[7,8,9]]

get_1 = itemgetter(1)
get_1(a)  >>> 2
get_1(b)  >>> [4,5,6]
"""

students = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

print(sorted(students, key=itemgetter(0)))
print(sorted(students, key=lambda t: t[1]))
print(sorted(students, key=itemgetter(1), reverse=True))
