""" 21. 合并两个有序链表
https://leetcode.cn/problems/merge-two-sorted-lists/

将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 """

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # prehead = pre, 是新链表的头节点的父节点
        # 要返回新链表的头节点，新链表生成需要移动节点，所以需要两个
        # prehead保持不动，pre来移动
        prehead = ListNode()
        pre = prehead
        while list1 and list2:
            if list1.val < list2.val:
                pre.next = list1
                list1 = list1.next
            else:
                pre.next = list2
                list2 = list2.next
            pre = pre.next
        # 把没合并完的 list1/list2 合并完，直接接到后面
        pre.next = list1 if list1 is not None else list2

        return prehead.next
                
