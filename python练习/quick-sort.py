# coding=utf-8

# from typing import List
# def quick_sort(list: List[int]) -> List[int]:

# 方法1 和以下方法2，效率不高，当数组元素数量在 5000 左右会出现超时的情况。
def quick_sort(list):
    if not list:
        return []
    else:
        pivot = list[0]
        less = [x for x in list if x < pivot]
        more = [x for x in list[1:] if x >= pivot]
        return quick_sort(less)+[pivot]+quick_sort(more)


if __name__=="__main__":
    list1=[4,1,3,5,2,8]
    list2=quick_sort(list1)
    print(list2)

# 方法2，类似方法1
class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        less = []
        pivotList = []
        more = []
        if len(nums) <= 1:
            return nums
        else:
            pivot = nums[0]      #将第一个值做为基准
            for i in nums:
                if i < pivot:
                    less.append(i)
                elif i > pivot:
	                more.append(i)
                else:
                    pivotList.append(i)
        less = self.sortArray(less)      #得到第一轮分组之后，继续将分组进行下去。
        more = self.sortArray(more)
        return less + pivotList + more

# 其他解法参考
# https://github.com/qiwsir/algorithm/blob/master/quick_sort.md
# https://www.runoob.com/w3cnote/quick-sort.html
# https://zhuanlan.zhihu.com/p/63227573
# 共同的重要条件（判断界限）：下标 i=j