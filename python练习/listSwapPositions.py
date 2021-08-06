# coding=utf-8
'''
练习list
    pop 和 insert 内置函数的用法
    
list.pop([index=-1])
    index -- 可选参数，要移除列表元素的索引值，不能超过列表总长度，默认为 index=-1，删除最后一个列表值。
    该方法返回从列表中移除的元素对象。

list.insert(index, obj)
    index -- 对象obj需要插入的索引位置。
    obj -- 要插入列表中的对象
    该方法没有返回值，但会在列表指定位置插入对象。
'''


def swapPositions(list, pos1, pos2):
     
    first_ele = list.pop(pos1)    
    second_ele = list.pop(pos2-1)  # 删除一个元素后，列表长度-1，后续元素下标也减1，但要保证 pos1<pos2
     
    list.insert(pos1, second_ele)  
    list.insert(pos2, first_ele)  
     
    return list
 
List = [23, 65, 19, 90]
pos1, pos2  = 1, 3
 
print(swapPositions(List, pos1-1, pos2-1))