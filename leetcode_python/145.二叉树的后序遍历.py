""" 145. 二叉树的后序遍历
https://leetcode.cn/problems/binary-tree-postorder-traversal/

给你一棵二叉树的根节点 root ，返回其节点值的 后序遍历 。 """

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 后序遍历：左右根，递归实现
        def postorder(root: Optional[TreeNode]):
            if root is None:
                return
            postorder(root.left)
            postorder(root.right)
            ans.append(root.val)

        ans = []
        postorder(root)
        return ans
