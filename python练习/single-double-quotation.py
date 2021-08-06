'''
简单来说，在Python中使用单引号或双引号是没有区别的，都可以用来表示一个字符串。但是这两种通用的表达方式，
除了可以简化程序员的开发，避免出错之外，还有一种好处，就是可以减少转义字符的使用，是程序看起来更简洁，更清晰。
举个两个例子：
1、包含单引号的字符串假如你想定义一个字符串my_str，其值为： I'm a student，
则可以采用如下方式，通过转义字符 '\' 进行定义 my_str = 'I\'m a student'
也可以不使用转义字符，利用双引号直接进行定义my_str = "I'm a student"
2、包含双引号的字符串假如你想定义一个字符串my_str，其值为： Jason said "I like you" ，
则可以采用如下方式，通过转义字符 '\' 进行定义my_str = "Jason said \"I like you\""
也可以不使用转义字符，利用单引号直接进行定义my_str = 'Jason said "I like you"'
通过这种方式，在合适的场景下采用单引号，或者双引号，是不是可以非常有效的避免转义字符的使用，
并且可以使代码看起来更加的简洁清晰，易懂



在需要在字符中使用特殊字符时，python 用反斜杠 “\” 转义字符

转义字符	描述	实例

\(在行尾时)	续行符	
>>> print("line1 \
... line2 \
... line3")
line1 line2 line3
>>> 

\\	反斜杠符号	
>>> print("\\")
\

\'	单引号	
>>> print('\'')
'

\"	双引号	
>>> print("\"")
"

'''

my_str = 'I\'m a student'
print(my_str)
my_str2 = "I'm a student"
print(my_str2)
print("*" * 22)
my_str3 = "Jason said \"I like you\""
print(my_str3)
my_str4 = 'Jason said "I like you"'
print(my_str4)
my_str5 = "'test'"
print(my_str5)


# 续行符的使用，注意续行符后无任何元素，包括空格等
# 使用方式：输入续行符“\”后，回车，再继续输入
print("*"*30)
print("a"\
    'b')
print("dfadf"\
    "12434")

print("dfadf\
12434")  
