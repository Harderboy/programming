import json
import sys

str = '''
[{
    "name": "Tom",
    "gender": "male"
}, {
    "name": "Jack",
    "gender": "male"   
}]
'''
# 将json字符串转为python对象
print(type(str))
data = json.loads(str)
print(type(data))
print(data)

data = [{
    "name": "Tom",
    "gender": "male"
}, {
    "name": "杰克",
    "gender": "男"
}]

# 将python对象转为json字符串（json数组）
print(type(data))
str = json.dumps(data, indent=2)  # indent=2按照缩进格式
print(type(str))
print(str)

print("*" * 33)

data1 = {
    'no': 1,
    'name': 'Runoob',
    'url': 'http://www.runoob.com'
}
# Python 字典类型转换为 JSON 字符串
json_str = json.dumps(data1)
print("Python 原始数据：", repr(data1))
print("JSON 对象：", json_str)
print(type(json_str))

print("*" * 33)

# 将 JSON 字符串转换为 Python 字典
data2 = json.loads(json_str)
print("data2['name']: ", data2['name'])
print("data2['url']: ", data2['url'])
print(type(data2))

print(repr(data2))

print(sys.path)

print("*" * 55)
a_json = json.load(open('a.json','r'))
print(a_json)
print(type(a_json))
print(type(open('a.json','r')))