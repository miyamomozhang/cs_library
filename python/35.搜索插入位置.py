""" 35. 搜索插入位置
https://leetcode.cn/problems/search-insert-position/

给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

请必须使用时间复杂度为 O(log n) 的算法。
"""
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        # 二分查找
        left = 0
        right = n - 1
        while left <= right:
            mid = (right - left)//2 + left
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return left