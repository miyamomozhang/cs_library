""" 234. 回文链表
https://leetcode.cn/problems/palindrome-linked-list/

给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。 """

from typing import Optional


# Definition for singly-linked list.
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head.next == None:
            return True
        nodelist = []
        # 把所有节点放到list列表中
        while head:
            nodelist.append(head)
            head = head.next
        # 双指针遍历
        left = 0
        right = len(nodelist) - 1
        while left < right:
            if nodelist[left].val != nodelist[right].val:
                return False
            else:
                left += 1
                right -= 1

        return True
