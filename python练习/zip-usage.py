"""
zip在python3中，处于优化内存的考虑，只能访问一次！！！(python2中可以访问多次)
在python 3.0中有个大坑，zip中的数据只能操作一次，内存就会释放，当下次访问时就会有问题。

zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的对象，这样做的好处是节约了不少的内存。

我们可以使用 list() 转换来输出列表。

如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将对象中的元组元素解压为列表元素。

zip(*)解压函数，将对象中的每一个元素(元祖/字符串)的相同位置的子元素组合成一个新的元祖，并使用list()将所有组成的元祖以列表的形式进行展示。

zip 方法在 Python 2 和 Python 3 中的不同：在 Python 2.x zip() 返回的是一个列表。

zip 语法：
    zip([iterable, ...])
参数说明：
    iterable -- 一个或多个迭代器;
返回值
    返回一个zip对象。

实例:
>>> a = [1,2,3]
>>> b = [4,5,6]
>>> c = [4,5,6,7,8]
>>> zipped = zip(a,b)     # 返回一个对象
>>> zipped
<zip object at 0x103abc288>
>>> list(zipped)  # list() 转换为列表
[(1, 4), (2, 5), (3, 6)]
>>> list(zip(a,c))              # 元素个数与最短的列表一致
[(1, 4), (2, 5), (3, 6)]
 
 
>>> a1, a2 = zip(*zip(a,b))          # 与 zip 相反，zip(*) 可理解为解压，返回二维矩阵式
>>> list(a1)
[1, 2, 3]
>>> list(a2)
[4, 5, 6]
>>>
"""


a = [1, 2, 3]
print(zip(a))
print(list(zip(a)))  # [(1,), (2,), (3,)]


l = ['flower', 'flow', 'flight']
print(zip(l))
print(zip(*l))
print(list(zip(l)))  # 转换为list显示
print(list(zip(*l)))
print(tuple(zip(l)))
print(tuple(zip(*l)))

# <zip object at 0x0000018B0BBD4F08>
# <zip object at 0x0000018B0BBD4F08>
# [('flower',), ('flow',), ('flight',)]
# [('f', 'f', 'f'), ('l', 'l', 'l'), ('o', 'o', 'i'), ('w', 'w', 'g')]
# (('flower',), ('flow',), ('flight',))
# (('f', 'f', 'f'), ('l', 'l', 'l'), ('o', 'o', 'i'), ('w', 'w', 'g'))

print("\r")

l = ['flower', 'flow', 'flight']
m = ['a', 'b', 'c']

# 问题代码，如下

# k = zip(l, m)
# print(zip(l, m))
# print(list(k))
# d=list(k)
# print(list(k))
# print(d)  # 输出为空
# print(zip(*d))  # 输出为空
# print(list(zip(*d)))  # 输出为空
"""
>>> l = ['flower', 'flow', 'flight']
>>> m = ['a', 'b', 'c']
>>> k = zip(l, m)
>>> k
<zip object at 0x7fb3b3c12200>
>>> list(k)
[('flower', 'a'), ('flow', 'b'), ('flight', 'c')]
>>> list(k)
[]
>>> 
"""

# 正确代码，如下
print(zip(l, m))
print(list(zip(l, m)))
print(zip(*zip(l, m)))
print(list(zip(*zip(l, m))))

# [('flower', 'a'), ('flow', 'b'), ('flight', 'c')]
# [('flower', 'flow', 'flight'), ('a', 'b', 'c')]


"""
参考链接
    https://www.jb51.net/article/189995.htm

python3中zip()函数使用详解

zip函数接受任意多个可迭代对象作为参数,将对象中对应的元素打包成一个tuple,然后返回一个可迭代的zip对象.
这个可迭代对象可以使用循环的方式列出其元素,若多个可迭代对象的长度不一致,则所返回的列表与长度最短的可迭代对象相同.

zip在python3中，处于优化内存的考虑，只能访问一次！！！(python2中可以访问多次)，童鞋们一定要注意，

zip()函数的定义：从参数中的多个迭代器取元素组合成一个新的迭代器；
返回： 返回一个zip对象，其内部元素为元组；可以转化为列表或元组；
传入参数： 元组、列表、字典等迭代器。
当zip()函数中只有一个参数时，zip(iterable)从iterable中依次取一个元组，组成一个元组。
在python 3.0中有个大坑，zip中的数据只能操作一次，内存就会释放，当下次
访问时就会报错，例如例子1中的输出操作

1、zip()函数单个参数

print(‘=‘*10 + “zip()函数单个参数” + ‘=‘*10) 
list1 = [1, 2, 3, 4] 
tuple1 = zip(list1)
 
list2=list(tuple1)

打印zip函数的返回类型

print(“zip()函数的返回类型：\n”, type(tuple1))#类型为

将zip对象转化为列表

print(“zip对象转化为列表：\n”, list(tuple1))#值为[(1,), (2,), (3,), (4,)] 
print(“zip对象转化为列表：\n”, list(tuple1))#值为[]
 
print(“list2输出的列表1为:\n”,list2) 
print(“list2输出的列表2为:\n”,list2) 

当zip()函数有两个参数时:zip(a,b)zip()函数分别从a和b依次各取出一个元素组成
元组，再将依次组成的元组组合成一个新的迭代器–新的zip类型数据。
注意：要求a与b的维数相同，当两者具有相同的行数与列数时，正常组合对应位置元素即可；
当a与b的行数或列数不同时，取两者结构中最小的行数和列数，依照最小的行数和列数将
对应位置的元素进行组合；这时相当于调用itertools.zip_longest(*iterables)函数。

2、zip()函数有2个参数

print(‘=‘*10 + “zip()函数有2个参数” + ‘=‘*10) 
m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] 
n = [[2, 2, 2], [3, 3, 3], [4, 4, 4]] 
p = [[2, 2, 2], [3, 3, 3]]

行与列相同

print(“行与列相同:\n”, list(zip(m, n)))

值为[([1, 2, 3], [2, 2, 2]), ([4, 5, 6], [3, 3, 3]), ([7, 8, 9], [4, 4, 4])]

行与列不同

print(“行与列不同:\n”, list(zip(m, p)))

值为[([1, 2, 3], [2, 2, 2]), ([4, 5, 6], [3, 3, 3])]

3、zip()应用，也可以使用for循环+列表推导式实现

矩阵相加减、点乘

m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
n = [[2, 2, 2], [3, 3, 3], [4, 4, 4]]

矩阵点乘

print(‘=‘*10 + “矩阵点乘” + ‘='10)#左右两端各有10个 
print([x*y for a, b in zip(m, n) for x, y in zip(a, b)])
 
[2, 4, 6, 12, 15, 18, 28, 32, 36]

矩阵相加,相减雷同

print(‘=‘*10 + “矩阵相加,相减” + ‘=‘*10) 
print([x+y for a, b in zip(m, n) for x, y in zip(a, b)])
 
[3, 4, 5, 7, 8, 9, 11, 12, 13]

4、*zip的操作

m5=[1,2,3] 
n5=[4,5,6] 
k5=[7,8,9] 
zip5=zip(m5,n5,k5)
 
print(“list(zip5):”,list(zip5))不能输出，否则zip(*zip5)
就无法执行

m6,n6,k6=zip(*zip5) 
print(“m6:”,m6)#m6: (1, 2, 3) 
print(“n6:”,n6)#n6: (4, 5, 6) 
print(“k6:”,k6)#k6: (7, 8, 9)

5、*zip()函数

*zip()函数是zip()函数的逆过程，将zip对象变成原先组合前的数据。

print(‘=‘*10 + “*zip()函数” + ‘=‘*10) 
m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] 
n = [[2, 2, 2], [3, 3, 3], [4, 4, 4]]
 
print(“zip(m, n)返回:\n”, zip(m, n)) # 
print(“*zip(m, n)返回:\n”, *zip(m, n))
 
*zip(m, n)返回:([1, 2, 3], [2, 2, 2]) ([4, 5, 6],[3, 3, 3]) ([7, 8, 9], [4, 4, 4])
 
print(“list(zip(m, n))返回:\n”, list(zip(m, n)))
 
list(zip(m, n))返回: [([1, 2, 3], [2, 2, 2]), ([4, 5, 6], [3, 3, 3]), ([7, 8, 9], [4, 4, 4])]
 
m2, n2 = zip(*zip(m, n))#先合到一块 
print(“m2:”,m2)#([1, 2, 3], [4, 5, 6], [7, 8, 9]) 
print(“n2:”,n2)#([2, 2, 2], [3, 3, 3], [4, 4, 4]) 
print(m == list(m2) and n == list(n2))#true

"""