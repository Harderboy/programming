"""
字典 in 操作符用于判断键是否存在于字典中，如果键在字典 dict 里返回 true，否则返回 false。

in 操作符语法：
    key in dict
参数
    key -- 要在字典中查找的键。
返回值
    如果键在字典里返回true，否则返回false。

"""

dict = {'Name': 'Runoob', 'Age': 7}

# 检测键 Age 是否存在
if 'Age' in dict:
    print("键 Age 存在")
else:
    print("键 Age 不存在")

# 检测键 Sex 是否存在
if 'Sex' in dict:
    print("键 Sex 存在")
else:
    print("键 Sex 不存在")


# not in

# 检测键 Age 是否存在
if 'Age' not in dict:
    print("键 Age 不存在")
else:
    print("键 Age 存在")
