""" 24. 两两交换链表中的节点
https://leetcode.cn/problems/swap-nodes-in-pairs/

给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。 """

from typing import Optional


# Definition for singly-linked list.
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = prev = ListNode()
        pre.next = head.next
        while head and head.next:
            pre.next = head.next
            head.next = head.next.next
            pre.next.next = head
            # 准备下一轮的pre和head
            pre = head
            head = head.next
        return prev.next
