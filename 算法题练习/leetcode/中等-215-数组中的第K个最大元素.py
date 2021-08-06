"""
题目描述：
    在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:
    输入: [3,2,1,5,6,4] 和 k = 2
    输出: 5
    示例 2:

    输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
    输出: 4
    说明:

你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。

链接：https://leetcode-cn.com/problems/kth-largest-element-in-an-array

"""

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        return nums[-k]



# 考察快排，先写一遍快排
# 注意写法

# 写法1
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partiton(arr, low, high):
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
                q = partiton(arr, low, high)
                quick_sort(arr, low, q-1)
                quick_sort(arr, q+1, high)
        quick_sort(nums,0,len(nums)-1)
        return nums[-k]

# 写法2
class Solution:
    def partiton(self,arr, low, high):
        i = low-1
        pivot = arr[high]
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[high] = arr[high], arr[i+1]
        return i+1

    def quick_sort(self,arr, low, high):
        if low < high:
            q = self.partiton(arr, low, high)
            self.quick_sort(arr, low, q-1)
            self.quick_sort(arr, q+1, high)

    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.quick_sort(nums,0,len(nums)-1)
        return nums[-k]

