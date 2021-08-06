"""
题目描述：
    给定一个链表，判断链表中是否有环。
    如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。
    如果链表中存在环，则返回 true 。 否则，返回 false 

示例：
    输入：head = [3,2,0,-4], pos = 1
    输出：true
    解释：链表中有一个环，其尾部连接到第二个节点。

    输入：head = [1], pos = -1
    输出：false
    解释：链表中没有环。

提示：
    链表中节点的数目范围是 [0, 104]
    -105 <= Node.val <= 105
    pos 为 -1 或者链表中的一个 有效索引 。
链接：https://leetcode-cn.com/problems/linked-list-cycle
"""

# 解法1 使用哈希，python中的集合

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        collection=set()
        if not head or not head.next:
            return False
        while head:
            if head in collection:
                return True
            collection.add(head)
            head=head.next
        
        return False

# 解法2 快慢指针

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        slow=quick=head
        # slow=head
        # quick=head.next # 没有以上执行用时和内存消耗优
        while quick and quick.next:
            slow=slow.next
            quick=quick.next.next
            if slow==quick:
                return True
        return False
        


