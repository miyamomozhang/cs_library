""" 160. 相交链表
https://leetcode.cn/problems/intersection-of-two-linked-lists/ 
给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 null 。
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def getIntersectionNode(self, headA: ListNode,
                            headB: ListNode) -> Optional[ListNode]:
        # Optional 类型提示可以用于标记函数参数或返回值为可选类型，明确告诉其他开发者这个参数或返回值可以为指定类型或 None。

        # 把链表A的节点存放到一个集合中
        setA = set()
        while headA:
            setA.add(headA)
            headA = headA.next
        # 遍历链表B的节点，如果在setA中出现了，说明相交了，返回
        while headB:
            if headB in setA:
                return headB
            headB = headB.next
        # 没找到相交的节点，返回None
        return None
