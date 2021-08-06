"""
题目描述：
    给定一个非负整数数组 A， A 中一半整数是奇数，一半整数是偶数。
    对数组进行排序，以便当 A[i] 为奇数时，i 也是奇数；当 A[i] 为偶数时， i 也是偶数。
    你可以返回任何满足上述条件的数组作为答案。

示例：
    输入：[4,2,5,7]
    输出：[4,5,2,7]
    解释：[4,7,2,5]，[2,5,4,7]，[2,7,4,5] 也会被接受。
 

提示：
    2 <= A.length <= 20000
    A.length % 2 == 0
    0 <= A[i] <= 1000

链接：https://leetcode-cn.com/problems/sort-array-by-parity-ii
"""
# 解法
# 思路：将列表拆分为一奇一偶两个列表，然后循环1/2长度，每循环一次依次从一偶一奇两个列表各取一个元素
# 英文命名：奇数 odd 偶数 even

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odd,even=[],[]
        for i in range(len(nums)):
            if nums[i]%2==0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        res=[]
        for j in range(len(odd)):
            res.append(even[j])
            res.append(odd[j])
        return res
