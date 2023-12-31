""" 94. 二叉树的中序遍历
https://leetcode.cn/problems/binary-tree-inorder-traversal/

给定一个二叉树的根节点 root ，返回 它的 中序 遍历 。 """

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 中序遍历：左根右，递归实现
        def inorder(root: Optional[TreeNode]):
            if root is None:
                return
            inorder(root.left)
            ans.append(root.val)
            inorder(root.right)

        ans = []
        inorder(root)
        return ans
