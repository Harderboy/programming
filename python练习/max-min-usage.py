"""
max() 方法返回给定参数的最大值，参数可以为序列

max(x, y[, z...]):Number|Sequence 入参类型不能混入（要么全Number(int|float|complex|bool），要么全序列）。

入参是序列的话： 单序列入参，返回序列中最大的一个数值多序列入参, 按索引顺序，逐一对比各序列的当前索引位的 “值”，
直到遇见最大值立即停止对比，并返回最大值所在的序列（也就是说，多序列入参，返回值依旧是一个序列，而不是数值）

>>> max(0, True) #布尔喔
True
>>> max([1,2,3])
3
>>> max(1,2,4)
4
>>> max(-1, -0.5, 0)
0
>>> max((1,2,3))
3
>>> max([2,4], [3,6])
[3, 6]
>>> max([2,4], [1,5])
[2, 4]
>>> max([2,4], [1,5], [3,1], [2,5],[0,7])
[3, 1]
>>> max((1,2,3), (3,3,0))
(3, 3, 0)
>>> max((1,-1,0), (True,False,0)) #布尔喔
(True, False, 0)
>>> max((1,-1,0), (True,False,2,0),(1, 0, 0, 2))
(True, False, 2, 0)
>>> max((1,-1,0), (True,),(1,))
(1, -1, 0)
>>> max((-1,-1,0), (True,),(1,))
(True,)
>>> max([1,3,2],3,4) #非法入参
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '>' not supported between instances of 'int' and 'list'
>>> max((1,2,3), [2,4,1]) #非法入参
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '>' not supported between instances of 'list' and 'tuple'
"""

# 列表序列
list_seq=["flower", "flow", "flight",'']
list_max=max(list_seq)
list_min=min(list_seq)  # 空字符串最小 空字符ascii为0
print("max:",list_max,"min:",list_min)

# 字符串序列
str_seq="flower"
str_max=max(str_seq)
str_min=min(str_seq)
print(str_max,str_min)


# min用法类似

# 以min()函数为例进行说明，max()同理。
# 高阶函数 可以指定key（函数）

# 先来看看源码
'''
def min(*args, key=None): # known special case of min
    """
    min(iterable, *[, default=obj, key=func]) -> value
    min(arg1, arg2, *args, *[, key=func]) -> value
    
    With a single iterable argument, return its smallest item. The
    default keyword-only argument specifies an object to return if
    the provided iterable is empty.
    With two or more arguments, return the smallest argument.
    """
    pass
'''

# 用法一：
# 常规用法,对可迭代对象求最小值

a = min(1, 2, 3)
print(a) 

b = [1, 2, 3]
res = min(b)
print(res)

# 用法二:
# 当第二参数key不为空时,以key的函数对象为依据进行判断
print("-"*22)
a = [1, 2, 3, -4]
res1 = min(a)
res2 = min(a, key=lambda x: abs(x))
print(res1) # -4
print(res2) # 1


# 用法三:

# 对字典进行数据操作时,默认只会对key,而不是value
# 若是想求得字典中值最大的那组数据需要先用zip函数进行翻转
dict = {1: 'c', 2: 'b', 3: 'a'}
min_dict1 = min(dict) # 字典对象，对key进行排序
min_dict = min(zip(dict.values(), dict.keys()))
print(min_dict1) # 1
print(min_dict) # ('a', 3)

#对于翻转后的字典键值对,当键(原来的值)相等时才会对比值(原来的键)
