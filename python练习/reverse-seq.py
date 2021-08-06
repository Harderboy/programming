# coding=utf-8

"""
reversed 函数返回一个反转的迭代器。
以下是 reversed 函数的语法:
    reversed(seq)

参数
    seq -- 要转换的序列，可以是 tuple, string, list 或 range。也可以为迭代器，像range等
返回值
    返回一个反转的迭代器。


str() 函数将对象转化为适于人阅读的形式。

语法
    class str(object='')
参数
    object -- 对象。
返回值
    返回一个对象的string格式。

实例

>>>s = 'RUNOOB'
>>> str(s)
'RUNOOB'
>>> dict = {'runoob': 'runoob.com', 'google': 'google.com'};
>>> str(dict)
"{'google': 'google.com', 'runoob': 'runoob.com'}"
>>>

Python join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。

语法
    str.join(sequence)
参数
    sequence -- 要连接的元素序列（/迭代器/生成器），且序列中元素须为**字符串**类型
返回值
    返回通过指定字符连接序列中元素后生成的新字符串。


实例
#!/usr/bin/python3

s1 = "-"
s2 = ""
seq = ("r", "u", "n", "o", "o", "b") # 字符串序列
print (s1.join( seq ))
print (s2.join( seq ))
"""

# 字符串
print("----------字符串----------")
string = "reverse string"
# 字符串逆序 string[::-1]、string[-1::-1]、"".join(reversed(string))
print(string[::-1])
print(string[-1::-1])
print(reversed(string))
print(type(reversed(string)))
print(list(reversed(string)))
print("".join(reversed(string)))


# 列表
print("----------列表----------")
seqList = [1, 2, 4, 3, 5]
print(reversed(seqList))
print(list(reversed(seqList)))

# 元组
print("----------元组----------")
seqTuple = ('R', 'u', 'n', 'o', 'o', 'b')
print(reversed(seqTuple))
print(tuple(reversed(seqTuple)))

# 集合无序，集合（set）是一个无序的不重复元素序列。

# 字典，字典是另一种可变容器模型，且可存储任意类型对象。
# dict2 = { 'abc': 123, 98.6: 37 }
# print(reversed(dict2))

# range 
# Python3 range() 返回的是一个可迭代对象（类型是对象）
print("----------range----------")
seqRange = range(5, 9)
print(reversed(seqRange)) # <range_iterator object at 0x7fb6ef5ca150>
print(type(reversed(seqRange))) # <class 'range_iterator'>
print(list(reversed(seqRange)))
print(str(reversed(seqRange)))  # 体会str的作用
# str.join(sequence) 函数中的 sequence 中的元素必须的字符串，否则会报错
# print("".join(reversed(seqRange)))  报错：TypeError: sequence item 0: expected str instance, int found  序列中含有数字（int类型）
print(tuple(reversed(seqRange)))
