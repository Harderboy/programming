"""
题目描述：
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。


示例 1：
    输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
    输出：6
    解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
    示例 2：

    输入：nums = [1]
    输出：1

    输入：[-2,-3]
    输出：-2

    预期结果：-2

链接：https://leetcode-cn.com/problems/maximum-subarray

参考：https://leetcode-cn.com/problems/maximum-subarray/solution/dong-tai-gui-hua-fen-zhi-fa-python-dai-ma-java-dai/
"""

# 思路：动态规划 求最大和，开始的元素必须为正数

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # length=len(nums)
        # if length==1:
        #     return nums[0]
        # max_list=[]
        # for i in range(1,length):
        #     if nums[i-1]>0:
        #         nums[i]=nums[i]+nums[i-1]
        #     bigger=max(nums[i-1],nums[i])
        #     max_list.append(bigger)
        # res=max(max_list)
        # return res
        length=len(nums)
        for i in range(1,length):
            if nums[i-1]>0:
                nums[i]=nums[i]+nums[i-1]
        res=max(nums)
        return res
        