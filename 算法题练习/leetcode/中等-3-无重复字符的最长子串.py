'''
设计知识点：
    字串：考虑滑动窗口
    哈希相关
    待总结

题目描述：
    给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例:
    输入: s = "abcabcbb"
    输出: 3 
    解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

    输入: s = ""
    输出: 0

提示：
    0 <= s.length <= 5 * 104
    s 由英文字母、数字、符号和空格组成

https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
'''

# 方法1 使用字符串存储最长子串

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        max_length=0
        tmp=''
        for i in s:
            if i in tmp:
                tmp=tmp[tmp.find(i)+1:]+i
            else:
                tmp+=i
            if len(tmp)>max_length:
                max_length=len(tmp)
        return max_length


# 方法2 使用列表存储最长子串
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        max_length=0
        tmp=[]
        for i in s:
            while i in tmp:
                tmp.pop(0) # 删除队列左边第一个，直到没有重复的字符串
            tmp.append(i)
            if len(tmp)>max_length:
                max_length=len(tmp)
        return max_length

# 其他方法待学习