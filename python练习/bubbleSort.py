# coding=utf-8

def bubble_sort(list):
    for x in range(len(list)-1):
        for y in range(len(list)-x-1):
            if list[y]>list[y+1]:
                list[y],list[y+1]=list[y+1],list[y]
    return list

if __name__=="__main__":
    list=[2,4,5,0,3,6,5]
    list_sort=bubble_sort(list)
    print(list_sort)
    print(list)

