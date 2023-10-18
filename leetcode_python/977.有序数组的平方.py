""" 977. 有序数组的平方
https://leetcode.cn/problems/squares-of-a-sorted-array/
给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。 """
from typing import List


class Solution:

    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        neg_index = -1
        for i, num in enumerate(nums):
            if num < 0:
                neg_index = i
            else:
                break
        for i, num in enumerate(nums):
            nums[i] = num * num
        if neg_index == -1:
            # 全是正数，已经排序完成
            return nums
        # 有负数，0~neg_index为负数，neg_index+1~n-1为正数
        # 取平方之后，两边最大，中间最小
        ans = []
        left, right = neg_index, neg_index + 1  # left, right中间最小，分别向两边
        while left >= 0 and right <= n - 1:
            if (nums[left] <= nums[right]):
                ans.append(nums[left])
                left -= 1
            else:
                ans.append(nums[right])
                right += 1
        while left >= 0:
            ans.append(nums[left])
            left -= 1
        while right <= n - 1:
            ans.append(nums[right])
            right += 1
        return ans
