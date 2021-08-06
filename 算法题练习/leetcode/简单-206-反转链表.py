"""
题目描述：
    给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。

示例：
    输入：head = [1,2,3,4,5]
    输出：[5,4,3,2,1]

    输入：head = []
    输出：[]

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 头插法？
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or head.next==None:
            return head
        pre=None
        cur=head
        while cur!=None:
            tmp=cur.next
            cur.next=pre
            pre=cur
            cur=tmp 

        return pre
