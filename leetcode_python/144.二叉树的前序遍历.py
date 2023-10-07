""" 144. 二叉树的前序遍历
https://leetcode.cn/problems/binary-tree-preorder-traversal/

给你二叉树的根节点 root ，返回它节点值的 前序 遍历。 """

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 前序遍历：根左右，递归实现
        def preorder(root: Optional[TreeNode]):
            if not root:
                return
            ans.append(root.val)
            preorder(root.left)
            preorder(root.right)

        ans = []
        preorder(root)
        return ans
