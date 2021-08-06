
print(len("123"))
print(len("123\
123"))
print("123\
adaf")


print("123"\
    "adaf")
# 第二种
print("123\
adaf")

print(r'\n')
print(R'\n')
print(len(r'\n'))

print("daf\n1234")
print("dsf\radf")

a=2
for i in range(5):
    a+=i

print(a)
print(i)

print("dfasdf""1243")

def aa(*args,**kwrgs):
    print(aa.__name__)
    print(args)
    print(kwrgs)


aa()
aa(2,3,2,q=1)


class foo():
    def __init__(self,func):
        self.func=func
    def __call__(self):
        print("------")
        self.func()
        print("over")

@foo
def f():
    print("f")

f()


def test():
    print("-----test----")

test.x =1
test.y =2
print(test.__dict__)



class MyList(object):
    def __init__(self):
        self.container = []
    def add(self, item):
        self.container.append(item)
    def __iter__(self):
        """返回一个迭代器"""
        # 我们暂时忽略如何构造一个迭代器对象
        pass

mylist = MyList()

from collections import Iterable

print(isinstance(mylist, Iterable))

# print(next(mylist))

print("*"*22)

str1="2sfsf"
num=10
str_s="%s"%str1
str_i="%7.2f"%num  
print(str_i)
str_n="%s"%num  # f{num}
str_f=f"{num}"
print(str_s,str_n)
print(f"{num}")
# print(type(str_i))
# print(type(str_n))
# print(type(str_f))

list=[1,2,3,4,5]
# print(list[1::2])
print(list[3:10])
print(list[-3:1])
print(list[-3:0])
print(list[-3:0:-1])

print("*"*22)


# 切片 
print(list[:6])
print(list[6:])

print("-"*22)
a=[1,2,3,4]
print(a[:])
print("id-a-1:",id(a))
b=[5,6,7]
c=a+b
# a[:]=a[:4]+b[:3]
# print(a)
# print("id-a-2:",id(a))
a[:]=a+b
print(a)
print("id-a-3:",id(a))
print(c)
print("c-id:",id(c))
a2=[1,2,3,4,0,0,0]
print("a2-1:",a2)
a2[4:]=b
print("a2-2:",a2)

print("-"*22)
list[1::2]=[22,44]
print(list[1::2])

# import time

# for i in range(10):
#     print(i)
#     # print(time.time())

print("&"*22)
nums = [2,2,3,1]
pivot=nums[0]
bigger=[ii for ii in nums[1:] if ii>=pivot]
# print(ii)
print(bigger)

for i in range(5):
    a=1+i
print(i,a)


print("ab" in "sdfas")
