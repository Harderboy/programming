"""
题目描述：
    编写一个函数来查找字符串数组中的最长公共前缀。
    如果不存在公共前缀，返回空字符串 ""。

示例 1：
    输入：strs = ["flower","flow","flight"]
    输出："fl"
    示例 2：

    输入：strs = ["dog","racecar","car"]
    输出：""
    解释：输入不存在公共前缀。
 
提示：
    0 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] 仅由小写英文字母组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-common-prefix
"""

# 方法1 高阶函数zip的使用

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for tmp in zip(*strs):
            tmp_set = set(tmp)
            if len(tmp_set) == 1:
                res += tmp[0]
            else:
                break
        return res


# 方法2 调内部os方法

import os
class Solution2:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        return os.path.commonprefix(strs)

# 多种解法：
# 参考：https://leetcode-cn.com/problems/longest-common-prefix/solution/0014-zui-chang-gong-gong-qian-zhui-4chon-76k2/

# 解法1
# 思路
# 先找出数组中字典序最小和最大的字符串(两者的差别是最大的), 最长公共前缀即为这两个字符串的公共前缀

# 复杂度
# 时间复杂度O(N)O(N), N为所有字符串长度的平均值
# 空间复杂度O(1)O(1)

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        str0 = min(strs)
        str1 = max(strs)
        for i in range(len(str0)):
            if str0[i] != str1[i]:
                return str0[:i]
        return str0  # 考虑到特殊case：[""] 空字符的ascii最小
# 解法2 find()函数
# 思路
# 取一个单词s, 和后面单词比较, 看s与每个单词相同的最长前缀是多少！遍历所有单词。

# 复杂度
# 时间复杂度O(N)O(N), N为所有字符串的总长度
# 空间复杂度O(1)O(1)

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        res = strs[0]
        i = 1
        for i in range(1, len(strs)):
            # find() 方法检测字符串中是否包含子字符串 str, 如果指定begin和end范围, 则检查是否包含在指定范围内, 如果包含子字符串返回开始的索引值, 否则返回-1
            while strs[i].find(res) != 0:
                res = res[0: len(res) - 1]
        return res
