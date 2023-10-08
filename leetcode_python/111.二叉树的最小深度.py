""" 111. 二叉树的最小深度
https://leetcode.cn/problems/minimum-depth-of-binary-tree/

给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明：叶子节点是指没有子节点的节点。 """

from typing import Optional


# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def minDepth(self, root: Optional[TreeNode]) -> int:
        # 如果左子树为空，树的最小深度 = 右子树的最小深度 + 1
        # 如果右子树为空，树的最小深度 = 左子树的最小深度 + 1
        # 都不空，树的最小深度=min(左子树的最小深度,右子树的最小深度）+ 1

        # 根为空，返回0
        if not root:
            return 0
        # 无左右子树，返回1
        if not root.left and not root.right:
            return 1
        # 只有左子树
        if root.left and not root.right:
            return self.minDepth(root.left) + 1
        # 只有左子树
        if root.right and not root.left:
            return self.minDepth(root.right) + 1
        # 有左右子树
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
