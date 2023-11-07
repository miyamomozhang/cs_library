""" 61. 旋转链表
https://leetcode.cn/problems/rotate-list/
给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。 """

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n, nodes = 0, []
        h = head  # 不改变原来head的指向
        while h:
            nodes.append(h)
            h = h.next
            n += 1
        if n == 0 or k == 0:
            return head
        k %= n
        prehead = ListNode()
        pre = prehead
        res = n-k  # 在下面循环中没用到的节点，需要在后面添加
        while k >= 1:
            pre.next = nodes[n-k]
            pre = pre.next
            pre.next = None  # 断链
            k -= 1
        for i in range(res):
            pre.next = nodes[i]
            pre = pre.next
            pre.next = None  # 断链

        return prehead.next