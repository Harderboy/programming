# coding=utf-8

"""
查找指定字符串中第一个出现且频率为1的数字

拆解：
    数字
    第一个出现
    只出现一次


Python 字典 in 操作符用于判断 键 是否存在于字典中，如果键在字典 dict 里返回 true，否则返回 false。
而 not in 操作符刚好相反，如果键在字典 dict 里返回 false，否则返回 true。

in 操作符语法：
    key in dict
参数
    key -- 要在字典中查找的键。
返回值
    如果键在字典里返回true，否则返回false。

举例：
dict = {'Name': 'Runoob', 'Age': 7}

# 检测键 Age 是否存在
if  'Age' in dict:
    print("键 Age 存在")
else :
    print("键 Age 不存在")
"""


def find_once_num(str):
    dict = {}
    # 遍历字符串，拿到各个字符对应的个数，放到字典中
    for i in range(len(str)):
        if str[i] in dict:
            dict[str[i]] += 1
        else:
            dict[str[i]] = 1

    # print(dict)
    for i in range(len(str)):
        # 出现次数为1，并且为数字
        if dict[str[i]] == 1 and str[i].isdigit():
            return str[i]


# str1 = input("输入一串包含数字的运算符")
str2 = "sdfa1230321456"
res = find_once_num(str2)
print(res)
