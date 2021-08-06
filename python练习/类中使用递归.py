class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        else:
            pivot=nums[0]
            bigger=[i for i in nums[1:] if i>=pivot]
            less=[j for j in nums if j<pivot]
            return self.sortArray(less)+[pivot]+self.sortArray(bigger)

sort=Solution()
a=sort.sortArray([5,3,2,6,4,9,2])
print(a)