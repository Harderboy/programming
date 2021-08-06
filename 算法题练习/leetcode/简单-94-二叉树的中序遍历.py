"""
题目描述：
    给定一个二叉树的根节点 root ，返回它的 中序 遍历。

示例：
    输入：root = [1,null,2,3]
    输出：[1,3,2]
示例 2：
    输入：root = []
    输出：[]
示例 3：
    输入：root = [1]
    输出：[1]

链接：https://leetcode-cn.com/problems/binary-tree-inorder-traversal

其他写法参考；
https://leetcode-cn.com/problems/binary-tree-inorder-traversal/solution/python3-er-cha-shu-suo-you-bian-li-mo-ban-ji-zhi-s
"""
# 递归 
# 通用模版 其他如先序遍历、后序遍历类似

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        return self.inorderTraversal(root.left)+[root.val]+self.inorderTraversal(root.right)

# 其他解法 待继续学习