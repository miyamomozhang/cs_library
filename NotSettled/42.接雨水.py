""" 42. 接雨水
https://leetcode.cn/problems/trapping-rain-water/

给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。 """
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        