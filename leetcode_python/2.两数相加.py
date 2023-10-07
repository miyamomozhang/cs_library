""" 2. 两数相加
https://leetcode.cn/problems/add-two-numbers/

给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。 """

from typing import Optional


# Definition for singly-linked list.
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode],
                      l2: Optional[ListNode]) -> Optional[ListNode]:
        pre = ListNode()
        prehead = pre
        # carry 进位
        carry = 0
        while l1 or l2 or carry:
            num1 = 0 if l1 is None else l1.val
            num2 = 0 if l2 is None else l2.val
            num = num1 + num2 + carry
            if num >= 10:
                carry = 1
                num -= 10
            else:
                carry = 0
            # 易错，注意下面的写法，如果不写 ListNode(), 原本next是None
            prehead.next = ListNode(num)
            prehead = prehead.next
            # 易错，None类型没有所谓的next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return pre.next
