# coding=utf-8

# 输入一个链表，反转链表后，输出新链表的表头。
'''
示例1
输入
    {1,2,3}
返回值
    {3,2,1}
说明：本题目包含复杂数据结构[ListNode](https://blog.nowcoder.net/n/954373f213e14eeab0a69ed0e9ef1b6e)，点此查看相关信息
'''

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if pHead == None or pHead.next == None:
            return pHead
        pre = None
        cur = pHead
        while cur != None:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre
