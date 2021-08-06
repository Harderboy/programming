"""
题目描述：
    假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

    每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

    注意：给定 n 是一个正整数。

示例 1：
    输入： 2
    输出： 2
    解释： 有两种方法可以爬到楼顶。
    1.  1 阶 + 1 阶
    2.  2 阶
示例 2：
    输入： 3
    输出： 3
    解释： 有三种方法可以爬到楼顶。
    1.  1 阶 + 1 阶 + 1 阶
    2.  1 阶 + 2 阶
    3.  2 阶 + 1 阶

链接：https://leetcode-cn.com/problems/climbing-stairs
"""

# 解法 暴力递归 超时 待优化（学习算法复杂度（时间、空间））

class Solution:
    def climbStairs(self, n: int) -> int:
        # 1阶 1
        # 2阶 2=1+1
        # 3阶 3=1+2
        # 4阶 5=1+3+1
        # f(n)=f(n-1)+f(n-2)
        if n<=3:
            return n
        else:
            return self.climbStairs(n-1)+self.climbStairs(n-2)

# 递推式   dp(n)=dp(n-1)+dp(n-2)  动态规划

class Solution:
    def climbStairs(self, n: int) -> int:
        # 1阶 1
        # 2阶 2=1+1
        # 3阶 3=1+2
        # 4阶 5=1+3+1
        # f(n)=f(n-1)+f(n-2)
        if n<=3:
            return n
        dp1=1
        dp2=2
        for i in range(3,n+1):
            dp2,dp1=dp1+dp2,dp2
        return dp2
        

# 其他人的解法如下：

class Solution:
    def climbStairs(self, n: int) -> int:
        """
        多种方案：每次1或2个台阶。动态规格问题
        状态是n，台阶
        dp(n):当前需要n台阶才能到楼顶，有dp(n)种方法。
        base case：1或者2，都是一步
        状态转移方程：dp(n) = dp(n-1)+dp(n-2):表示到达第n个台阶，需要到达第n-1台阶时的方法+第n-2台阶时的方法。
                        dp(1) = 1
                        dp(2) = 2
                        dp(3) = 3
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp1, dp2 = 1, 2
        for _ in range(n-2):
            dp2, dp1 = dp2 + dp1, dp2
        return dp2
            

# 作者：huoming
# 链接：https://leetcode-cn.com/problems/climbing-stairs/solution/dong-tai-gui-hua-by-huoming-edkb/

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return n
        dp1 = 1
        dp2 = 2
        for i in range(3, n + 1):
            dpsum   = dp1 + dp2
            dp1     = dp2
            dp2     = dpsum
        return dp2

# 作者：pinkman-r
# 链接：https://leetcode-cn.com/problems/climbing-stairs/solution/python3dong-tai-gui-hua-by-pinkman-r-q3sr/
