"""
eval() 函数用来执行一个字符串表达式，并返回表达式的值。

eval(expression[, globals[, locals]])
参数
    expression -- 表达式。
    globals -- 变量作用域，全局命名空间，如果被提供，则必须是一个字典对象。
    locals -- 变量作用域，局部命名空间，如果被提供，可以是任何映射对象。
返回值
    返回表达式计算结果。


>>>x = 7
>>> eval( '3 * x' )
21
>>> eval('pow(2,2)')
4


eval 方法能使字符串本身的引号去掉，保留字符的原本属性。

>>> a = "123"
>>> type(a)
<class 'str'>
>>> b = eval(a)
>>> ba
123
>>> type(b)
<class 'int'>

eval() 函数也可以直接用来提取用户输入的多个值。（将字符串转换为元组）

例如：
a,b=eval(input())
输入：10,5，得到 a=10，b=5。
"""

# eval()函数常见作用有：
# 1、计算字符串中有效的表达式，并返回结果

"""
>>> eval('pow(2,2)')
4
>>> eval('2 + 2')
4
>>> eval("n + 4")
85

"""

# 2、将字符串转成相应的对象（如list、tuple、dict和string之间的转换）

"""
>>> a = "[[1,2], [3,4], [5,6], [7,8], [9,0]]"
>>> b = eval(a)
>>> b
[[1, 2], [3, 4], [5, 6], [7, 8], [9, 0]]
>>> a = "{1:'xx',2:'yy'}"
>>> c = eval(a)
>>> c
{1: 'xx', 2: 'yy'}
>>> a = "(1,2,3,4)"
>>> d = eval(a)
>>> d
(1, 2, 3, 4)

"""

# str->list
str1_info = "[1,2,3,4,5]"
list_info = eval(str1_info)
print("string info type is -->: %s" % (type(str1_info)))
print("list info type is -->: %s" % (type(list_info)))


# str->tuple
str2_info = "(1,2,3,4,5)"
tuple_info=eval(str2_info)
print("string info type is -->: %s" % (type(str2_info)))
print("tuple info type is -->: %s" % (type(tuple_info)))


# 这种情况相当于将类似“20,5”类型的字符串，转换为元组，“20,5”去掉字符串本身引号，就是元组的形式了
# a, b = eval(input("请输入两个值，用逗号隔开，如10，5，输入的值为："))
# print("a: ", a)
# print("b: ", b)

str3_info = "{'name': 'nock', 'age': 14}"
dict_info = eval(str3_info)
print("string info type is -->: %s" % (type(str3_info)))
print("dict info type is -->: %s" % (type(dict_info)))

# 3、将利用反引号转换的字符串再反转回对象

"""
不支持使用反引号将list、tuple、dict转换为string
>>> `list1`
  File "<stdin>", line 1
    `list1`
    ^
SyntaxError: invalid syntax

"""

"""
>>> list1 = [1,2,3,4,5]
>>> `list1`
'[1, 2, 3, 4, 5]'
>>> type(`list1`)
<type 'str'>
>>> type(eval(`list1`))
<type 'list'>
>>> a = eval(`list1`)
>>> a
[1, 2, 3, 4, 5]
"""

# list1 = [1,2,3,4,5]
# print(type(`list1`))
