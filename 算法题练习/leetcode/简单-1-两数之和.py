'''
题目描述：
    给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target 的那两个整数，并返回它们的数组下标。
    你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
    你可以按任意顺序返回答案。

示例 1：
    输入：nums = [2,7,11,15], target = 9
    输出：[0,1]
    解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。


链接：https://leetcode-cn.com/problems/two-sum

'''

# 法1
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length=len(nums)
        for i in range(length):
            for j in range (i+1,length):
                if nums[i]+nums[j]==target:
                    return [i,j]

# 法2

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        while True:
            if i<len(nums):
                for j in range(i+1, len(nums)):
                    if nums[i] + nums[j] == target:
                        return [i, j]
            i+=1

# 上述方法时间复杂度差得多
# 思考空间换时间的方法，结合哈希表
