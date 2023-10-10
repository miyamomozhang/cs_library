""" 19. 删除链表的倒数第 N 个结点
https://leetcode.cn/problems/remove-nth-node-from-end-of-list/

给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。 """

from typing import Optional


# Definition for singly-linked list.
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def removeNthFromEnd(self, head: Optional[ListNode],
                         n: int) -> Optional[ListNode]:
        # 记录链表的头节点
        l = head
        # 计算链表的长度
        cnt = 0
        while head:
            cnt += 1
            head = head.next
        # 让head重新指向链表的头节点
        head = l
        # 删除的是第1个节点
        if cnt == n:
            return head.next
        # pcnt是要删除的节点的前一节点的index(从0开始)
        pcnt = cnt - n - 1
        while pcnt:
            head = head.next
            pcnt -= 1
        # 删除的是最后一个节点
        if head.next is None:
            head.next = None
        else:
            head.next = head.next.next
        return l
