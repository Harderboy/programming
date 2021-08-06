"""
题目描述：
    给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表没有交点，返回 null 。
   
题目链接：
    https://leetcode-cn.com/problems/intersection-of-two-linked-lists/

参考题解：   
    https://leetcode-cn.com/problems/intersection-of-two-linked-lists/solution/chi-xiao-dou-python-tu-wen-xiang-jie-by-j7tyi/
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        a,b=headA,headB
        while a!=b:
            if a:
                a=a.next
            else:
                a=headB
            if b:
                b=b.next
            else:
                b=headA
        return a

