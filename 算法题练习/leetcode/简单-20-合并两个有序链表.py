"""
题目描述：
    将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：
    输入：l1 = [1,2,4], l2 = [1,3,4]
    输出：[1,1,2,3,4,4]
    示例 2：

    输入：l1 = [], l2 = []
    输出：[]
    示例 3：

    输入：l1 = [], l2 = [0]
    输出：[0]

链接：https://leetcode-cn.com/problems/merge-two-sorted-lists

关于递归讲解：
    https://leetcode-cn.com/problems/merge-two-sorted-lists/solution/yi-kan-jiu-hui-yi-xie-jiu-fei-xiang-jie-di-gui-by-/
"""

# 解法1 递归

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        elif not l2:
            return l1
        elif l1.val<=l2.val:
            l1.next=self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next=self.mergeTwoLists(l1,l2.next)
            return l2

# 解法2 迭代
# 题解1 迭代法
# 同合并两个有序数组逻辑基本一样，只不过这里是链表。

# 1.新建一个链表承接结果。
# 2.从头开始，比较链表值，将较小的存入新链表，然后较小的链表向前走一步。
# 3.当一个链表遍历结束后，将剩余部分追加到新链表后即可。

# 链接：https://leetcode-cn.com/problems/merge-two-sorted-lists/solution/he-bing-liang-ge-you-xu-lian-biao-by-zxh-or2g/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3=ListNode()
        cur=l3
        while l1 and l2:
            if l1.val<=l2.val:
                cur.next=l1
                l1=l1.next
            else:
                cur.next=l2
                l2=l2.next
            cur=cur.next
        cur.next=l1 if l1 else l2  # 关键一步   三目（元）（条件）运算符
        return l3.next