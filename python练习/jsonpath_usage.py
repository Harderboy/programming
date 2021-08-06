import json

from jsonpath import jsonpath
# jsonpath方法 返回值为列表或者bool类型

if __name__ == '__main__':
    dict = {"class": {"students": [{"student_id": "1", "name": "bob", "sex": "male", "age": 6},
                                   {"student_id": "2", "name": "amy",
                                       "sex": "female", "age": 6},
                                   {"student_id": "3", "name": "pery", "sex": "male", "age": 5}],
                      "teachers": {"teacher_id": "1", "name": "anne", "sex": "female", "age": 32}}}

    # 获取根节点下的任意name属性的值
    print(jsonpath(dict, '$..name'))  # 输出 ['bob', 'amy', 'pery', 'anne']

    # 获取teachers节点
    # 输出 [{'teacher_id': '1', 'name': 'anne', 'sex': 'female', 'age': 32}]
    print(jsonpath(dict, '$.class.teachers'))

    # 获取第一个students数据
    # 输出  [{'student_id': '1', 'name': 'bob', 'sex': 'male', 'age': 6}]
    print(jsonpath(dict, '$..students[0]'))

    # 获取students的第一条数据的name属性
    print(jsonpath(dict, '$..students[0].name'))  # 输出 ['bob']
    # print(type(jsonpath(dict, '$..students[0].name')[0]))
    print(jsonpath(dict, '$..students[0].name')[0])  # 输出 bob
    print(jsonpath(dict, '$..students[0].[name]'))
    # print(type(jsonpath(dict, '$..students[0].[name]')))
    print(dict["class"]["students"][1]["name"])

    # 获取students的0,1条数据
    # 输出 [{'student_id': '1', 'name': 'bob', 'sex': 'male', 'age': 6}, {'student_id': '2', 'name': 'amy', 'sex': 'female', 'age': 6}]
    print(jsonpath(dict, '$..students[0,1]'))
    # 输出 [{'student_id': '1', 'name': 'bob', 'sex': 'male', 'age': 6}, {'student_id': '2', 'name': 'amy', 'sex': 'female', 'age': 6}]
    print(jsonpath(dict, '$..students[:2]'))

    # 获取students的最后一条数据
    # 输出 [{'student_id': '3', 'name': 'pery', 'sex': 'male', 'age': 5}]
    print(jsonpath(dict, '$..students[-1:]'))
