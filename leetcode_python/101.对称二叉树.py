""" 101. 对称二叉树
https://leetcode.cn/problems/symmetric-tree/

给你一个二叉树的根节点 root ， 检查它是否轴对称。 """
from typing import Optional


# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def isSame(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if p is None and q is None:
                return True
            if p is None or q is None:
                return False
            return (p.val == q.val) and isSame(p.left, q.right) and isSame(
                p.right, q.left)

        return isSame(root.left, root.right)
