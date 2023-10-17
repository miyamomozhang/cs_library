""" 148. 排序链表
https://leetcode.cn/problems/sort-list/
给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。 """

from typing import Optional


# Definition for singly-linked list.
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            # 链表为空或只有一个元素，直接返回
            return head
        nodes = []
        # 节点全部放到list列表中
        while head:
            nodes.append(head)
            head = head.next
        # lambda表达式sort排序
        nodes.sort(key=lambda node: node.val)
        pre = ListNode()
        prev = pre
        for node in nodes:
            pre.next = node
            pre = pre.next
            # None很重要!!! 要破坏原来的节点之间的链接关系
            pre.next = None
        return prev.next


# head = [-1,5,3,4,0]
nodes = [-1, 5, 3, 4, 0]
prev = ListNode()
pre = prev
for node in nodes:
    prev.next = ListNode(node)
    prev = prev.next
head = pre.next

s = Solution()
head = s.sortList(head)
while head:
    print(head.val)
    head = head.next
