'''
题目描述：
    给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表没有交点，返回 null 。

题目链接：
    https://leetcode-cn.com/problems/intersection-of-two-linked-lists/

参考答案链接：
    https://leetcode-cn.com/problems/intersection-of-two-linked-lists/solution/chi-xiao-dou-python-tu-wen-xiang-jie-by-j7tyi/

思路：
    这道题目让求两个链表相交的节点, 利用双指针法 O(m+n) 就可以遍历完成
    这道题目的思想是让 a, b 指针都走一遍 headAA，headB 两个链表，a b相遇的地方就是两个链表相交的地方.
        - a 指向 headA, 一步一步往 next 走, 走到结尾 null 时, 跳到 headB 继续往后遍历
        - b 指针跟 a 一样的, 只不过先遍历 headB, 到结尾了再跳到 headA

为什么不相交的情况这个代码也支持？

    如果不相交的话, a 和 b 都会最终同时到达 null, 因此返回null指针即可

复杂度：
    - 时间复杂度 O(m+n), m, n 分别为两个链表的节点数
    - 空间复杂度 O(1)
'''
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
        a, b = headA, headB
        while a != b:
            if a:
                a = a.next 
            else:
                a = headB

            if b:
                b = b.next
            else:
                b = headA
            
        return a
