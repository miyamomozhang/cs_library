""" 34. 在排序数组中查找元素的第一个和最后一个位置
https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/

给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target，返回 [-1, -1]。

你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。 """

from typing import List


class Solution:

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        left = 0
        right = n - 1
        # 二分查找
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                ans = [mid, mid]
                # 找起始值
                start = end = mid
                while start >= 0:
                    if nums[start] == target:
                        ans[0] = start
                    else:
                        break
                    start -= 1
                while end < n:
                    if nums[end] == target:
                        ans[1] = end
                    else:
                        break
                    end += 1
                return ans
        return [-1, -1]
