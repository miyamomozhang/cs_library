""" 206. 反转链表
https://leetcode.cn/problems/reverse-linked-list/
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。  """

from typing import Optional


# Definition for singly-linked list.
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # prehead是反转后链表的头节点的父节点
        prehead = ListNode()
        # 头插法
        while head:
            # 每一次循环，新节点插到前面作为链表的头节点
            # 节点p指向要插入的节点
            p = head
            head = head.next
            # p插到prehead后面，作为头节点
            p.next = prehead.next
            prehead.next = p

        return prehead.next
