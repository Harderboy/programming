"""
题目描述：
    给你一个整数数组 nums，请你将该数组升序排列。

示例 1：

    输入：nums = [5,2,3,1]
    输出：[1,2,3,5]

示例 2：
    输入：nums = [5,1,1,2,0,0]
    输出：[0,0,1,1,2,5]
 

提示：
    1 <= nums.length <= 50000

链接：https://leetcode-cn.com/problems/sort-an-array

"""

# 使用优化过的快速排序算法
# 否则对于基本有序的数组会报超时
# 参考链接：
# https://leetcode-cn.com/problems/sort-an-array/solution/python3-sui-ji-kuai-su-pai-xu-by-v12de-a-cuf3/

class Solution:
    def quick_sort(self,lists,i,j):
        if i >= j:
            return 
        index = random.randint(i, j)
        pivot = lists[index]
        lists[index], lists[i] = lists[i], lists[index]
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
        self.quick_sort(lists,low,i-1)
        self.quick_sort(lists,i+1,high)
        return lists

    def sortArray(self, nums: List[int]) -> List[int]:
        self.quick_sort(nums,0,len(nums)-1)
        return nums
