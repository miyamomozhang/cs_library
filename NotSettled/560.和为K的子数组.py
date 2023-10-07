""" 560. 和为 K 的子数组
https://leetcode.cn/problems/subarray-sum-equals-k/
给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的连续子数组的个数 。

子数组是数组中元素的连续非空序列。 """

from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = 0
        n = len(nums)
        for i in range(n):
            
