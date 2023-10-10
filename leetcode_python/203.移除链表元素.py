""" 203. 移除链表元素
https://leetcode.cn/problems/remove-linked-list-elements/
给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。  """

from typing import Optional


# Definition for singly-linked list.
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def removeElements(self, head: Optional[ListNode],
                       val: int) -> Optional[ListNode]:
        prehead = ListNode()
        prev = prehead
        while head:
            prev.next = None
            if head.val != val:
                prev.next = head
                prev = prev.next
            head = head.next
        return prehead.next
