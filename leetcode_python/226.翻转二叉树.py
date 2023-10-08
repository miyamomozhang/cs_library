""" 226. 翻转二叉树
https://leetcode.cn/problems/invert-binary-tree/

给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点。 """

from typing import Optional


# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 翻转，左右子树互换
        if root:
            left = root.left
            right = root.right
            root.right = self.invertTree(left)
            root.left = self.invertTree(right)
        return root
