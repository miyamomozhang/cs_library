""" 100. 相同的树
https://leetcode.cn/problems/same-tree/

给你两棵二叉树的根节点 p 和 q ，编写一个函数来检验这两棵树是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。 """

from typing import Optional


# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # p和q只有一个为空，返回false，结构不相同
        if p is None and q is not None:
            return False
        if p is not None and q is None:
            return False
        # p和q都空，返回true
        if p is None and q is None:
            return True
        # p和q都非空
        return (p.val == q.val) and self.isSameTree(
            p.left, q.left) and self.isSameTree(p.right, q.right)
