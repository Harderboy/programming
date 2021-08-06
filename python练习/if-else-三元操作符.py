# coding=utf-8

# python中的三元操作符
# res2 = a if tmp else b，解释：如果tmp为真，结果为a，否则执行b（为b）
tmp = ''
a = "asd"
b = "123"
res1 = a if tmp else print("test")
res2 = a if tmp else b
print("res1:", res1)
print("res2:", res2)
print(a)
print(b)
