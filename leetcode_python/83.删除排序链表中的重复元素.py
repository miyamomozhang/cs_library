""" 83. 删除排序链表中的重复元素
https://leetcode.cn/problems/remove-duplicates-from-sorted-list/

给定一个已排序的链表的头 head ， 删除所有重复的元素，使每个元素只出现一次 。返回 已排序的链表 。 """

from typing import Optional


# Definition for singly-linked list.
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        # h是要返回的链表的头，slow 是在新链表中的节点，fast 用来遍历
        slow = h = head
        fast = head.next
        while fast:
            # slow.next = None这句很关键，位置也很关键
            # 其实很简单，在没有找到符合条件的fast之前，slow的next是为空的
            # 找到符合条件的fast之后，slow的next指向fast
            # 也就是 slow的next 只有在满足条件的fast存在时才存在，其它时候为None
            slow.next = None
            if fast.val != slow.val:
                slow.next = fast
                slow = slow.next
            fast = fast.next
        return h
