""" 53. 最大子数组和
https://leetcode.cn/problems/maximum-subarray/

给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

子数组 是数组中的一个连续部分。 """

import collections
from typing import List


class Solution:

    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        maxsum = nums[0]
        # 前缀和 presum
        presum = nums[0]
        i = 1
        for i in range(1, n):
            # 前缀和小于0，i会舍掉前缀和重新开始；
            # 前缀和大于0，i会拉上前面的一起
            presum = max(nums[i], nums[i] + presum)
            maxsum = max(presum, maxsum)
        return maxsum
