# 法1
def partition(arr, low, high):
    i = low-1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1


def quick_sort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quick_sort(arr, low, p-1)
        quick_sort(arr, p+1, high)

    return arr  # 写不写都行

arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
a=quick_sort(arr, 0, n-1)
print(arr)
print(a)


# def partition(arr, low, high):
#     i = (low-1)         # 最小元素索引
#     pivot = arr[high]

#     for j in range(low, high):

#         # 当前元素小于或等于 pivot
#         if arr[j] <= pivot:

#             i = i+1
#             arr[i], arr[j] = arr[j], arr[i]

#     arr[i+1], arr[high] = arr[high], arr[i+1]
#     return (i+1)


# # arr[] --> 排序数组
# # low  --> 起始索引
# # high  --> 结束索引

# # 快速排序函数
# def quickSort(arr, low, high):
#     if low < high:

#         pi = partition(arr, low, high)

#         quickSort(arr, low, pi-1)
#         quickSort(arr, pi+1, high)


# arr = [10, 7, 8, 9, 1, 5]
# n = len(arr)
# quickSort(arr, 0, n-1)
# print(arr)

# 法2
def quick_sort(lists,i,j):
    if i >= j:
        return 
    pivot = lists[i]
    low = i
    high = j
    while i < j:
        while i < j and lists[j] > pivot:
            j -= 1
        lists[i]=lists[j]
        while i < j and lists[i] <=pivot:
            i += 1
        lists[j]=lists[i]
    lists[j] = pivot
    quick_sort(lists,low,i-1)
    quick_sort(lists,i+1,high)
    return lists

lists=[30,24,5,58,18,36,12,42,39]
b=quick_sort(lists,0,len(lists)-3)
print(b)

# 优化 随机快速排序
# 添加以下三行代码
# index = random.randint(left, right)
# pivot = nums[index]
# nums[index], nums[left] = nums[left], nums[index]

# 参考链接：
# https://leetcode-cn.com/problems/sort-an-array/solution/python3-sui-ji-kuai-su-pai-xu-by-v12de-a-cuf3/


# 优化后的 随机快速排序
import random
def quick_sort_random(arr,left,right):
    if left>=right:
        return
    index=random.randint(left,right)
    pivot=arr[index]
    arr[left],arr[index]=arr[index],arr[left]
    low=left
    high=right
    while left<right:
        while left<right and arr[right]>pivot:
            right-=1
        arr[left]=arr[right]
        while left<right and arr[left]<=pivot:
            left+=1
        arr[right]=arr[left]
    arr[left]=pivot
    quick_sort_random(arr,low,left-1)
    quick_sort_random(arr,right+1,high)

    return arr

lists=[30,24,5,58,18,36,12,42,39]
c=quick_sort_random(lists,0,len(lists)-1)
print(c)