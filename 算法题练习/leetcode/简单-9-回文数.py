"""
题目描述：
    给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。
    回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。例如，121 是回文，而 123 不是。

示例 1：
    输入：x = 121
    输出：true
示例 2：
    输入：x = -121
    输出：false
    解释：从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。

链接：https://leetcode-cn.com/problems/palindrome-number
"""
# 解法1 先转换成字符串 利用reversed函数
class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x=str(x)
        revese_x_list=list(reversed(str_x))
        revese_x="".join(revese_x_list)
        if revese_x==str_x:
            return True
        return False

# 解法2 字符串切片+条件运算符

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return True if str(x)==str(x)[::-1] else False
        
# 解法3 n个月前的操作

class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        if len(s) == 1 and '0' <= s <= '9':
            return True
        elif s[0] == '-':
            return False
        elif s.isdigit():
            for i in range(int(len(s) / 2)):
                if s[i] != s[len(s) - 1 - i]:
                    return False
            else:
                return True
        else:
            return False