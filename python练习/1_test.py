# print({'a':"\'"})
# print("#"*22)
# print({2:r'\\\"'})
# print({2:'\\\"'})

# print("\\\"")
# print("\"")


# a=r"""



# dfadfa

# """
# print(a)

# mydict = {'file_path1': r'\\11.1.2.3file1', 'file_path2': r'\\111232.3blabla'}
# mydict2 = {'file_path1': r'\*11.1.2.3file1', 'file_path2': r'\*111232.3blabla'}
# list1=['\\11.1.2.3file1']
# str1='\\11.1.2.3file1'
# print(mydict)
# print(mydict2)
# print(list1[0])
# print(str1)
# print(r'\\11.1.2.3file1')



# class str3():
#     a=None
#     def __init__(self,a):
#         self.a=a
    
#     def seta(self,b):
#         self.a+=b


# b=str3("asdasdsadsa")
# print(id(b.a))
# b.seta("10")
# b.a+="10"
# print(id(b.a))
# print(b.a)

# b="ada"
# print(id(b))
# b+="d"
# print(id(b))


print(id([]))
s=[].append("123123123")
print(s)
s2=[]
print(type([]))
s2.append("sdfsdf")
print(s2)
# str()
# s.append("123123123")
# print(s)
# def sets(s):
#     print(id(s))
#     print(s[0])
#     s[0]+="10"

# sets(s)
# print(s)
# print(id(s))

# import string

# print(string.digits)

# print("a" in "sdfas")

print("*"*22)
my_list=[1,2]

for i in my_list:
    print(i)
else:
    print("没有循环数据")


from datetime import datetime
# datetime.now：动态的当前时间，也就是数据库添加、修改的时间
# datetime.now()：固定的时间，程序部署的时间
print(datetime.now)
print(datetime.now())
    

a="2222"
msg="start"+"dfadf:%s"%a+"end"

print(msg)

try:
    print(2/0)
    ddd_1="ddd"
    # print(ddd_1)
except Exception as e:  # e不是全局变量
    pass
    print(msg)
    # print(ddd_1)

# print(ddd_1)
str_seq=["flower", "flow", "flight",'']
str_max=max(str_seq)
print(str_max)

print(str_seq[0:0])

for i in range(0):
    print("000")

str1="abb"
print(list(reversed(str1)))

# str.replace(old, new[, max])  
# 返回值：返回字符串中的 old（旧字符串）替换成 new(新字符串)后生成的新字符串，如果指定第三个参数max，则替换不超过 max 次。
s = "()[]{}"
s.replace("[]","")
print(s)
s=s.replace("[]","")
print(s)
s=s.replace("{}","")
s=s.replace("()","")
print(s)


s1="adfasdf234e444sds"
for i in s1:
    if i=="2":
        print(i,type(i))

print(type(ch.lower() for ch in s1 if ch.isalnum()))


if s1:print(s1)

url="https://page.udache.com/activity/apps/preference-recharge/index.html#/index?hash_passport_login"
print(url[-19::])


try:
    2/0
except Exception as e:
    print(e)
    print("异常为：%s"%e)


str2 = "123abcrunoob321"
print (str2.strip())  # 字符序列为 12

s="a good   example"
print(s.split())


print(bin(11))
print(bin(0b00000000000000000000000000001011))
print(bin(1011))
print(int(0b00000000000000000000000000001011))  # 数字前必须有0b 11
print(str(0b00000000000000000000000000001011))  # "11" 会先将二进制串转成十进制数，再转成字符串
print(str(5)) # str() 函数将对象转化为适于人阅读的形式

num=2
print(str(num))
print(str(1))
print(11&1)  # 11&01

# print(print_num())  # 必须先定义才能被调用

def print_num():
    return 22

print(print_num())


class TestOrder:
    def a(self):
        b=self.b()
        c=self.c()
        # a=self.a()
        return 1
    def b(self):
        return 2
    def c(self):
        return 3

a=TestOrder()
res=a.a()
print(res)

# 正常情况下，函数必须先定义才能被调用，否则会报错
# 但是在一个类中，没有这种顺序，因为类中方法地位都是相等的，都是实例的属性

import math

print(math.inf)
print(type(math.inf))
print(max(math.inf,999))
print(dir())


import inspect
for i in inspect.getmembers(TestOrder):  #获取Page类中的所有成员方法，i返回的是一个元祖,第一个元素是方法名，第二个是内存地址
    if inspect.isfunction(i[1]):  #判断成员是不是一个函数方法
        # print(i[1].__doc__)  #是打印他的doc
        print(i[1].__name__)


str3 = "123abcrunoob321"
print(str3[::-1])
print(str3[::1])
print(str3[::2])
print(str3[::-2])
# print(str3[0:10:-1])
# print(str3[0:10:-2])
print(str3[-1:-10:-2])
# 切片索引正负要与步长正负一致

s4=[7]
print(s4[-1])


import re
str5='''
dfadfadf
dfadfa    def test_ddd():dfadfa
dfadsf
'''
res=re.findall(r'(test_.*)\(',str5)
print(res)

print(-1)
print(bin(-1))
print(~1)
# 1->~1
# 0000 0001 补码
# 1111 1110 取反得到补码
# 1111 1101 补码-1
# 1000 0010 取反 

a=123
print(f'{a:.2f}')
print(("%.2f")%a)
print(("%s")%a)
# print(("%2s")%a) # 123
# print(("%.2s")%a) # 12
# print(("%3.2s")%a) #  12

print(len("99.12%"))

print("%s"%(9*100//(9+10))+"%")


list1 = ['Google', 'Runoob', 'Taobao', 'Baidu']
print(id(list1))
# 浅复制
list2 = list1.copy()
print ("list2 列表: ", list2,id(list2))
list3=list1
print(id(list1),id(list3))
list4=list1[:]
print(id(list1),id(list4))


def none():
    return

print(none()==None)
print(none() is None)

print(type([])==list)
print(type([]) is list)

import traceback

try:
    2/0
except Exception as e:
    traceback.print_exc()
    # print(traceback.format_exc())



import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)
print(os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)))