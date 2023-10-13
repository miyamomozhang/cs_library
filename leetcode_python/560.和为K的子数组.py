""" 560. 和为 K 的子数组
https://leetcode.cn/problems/subarray-sum-equals-k/
给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的连续子数组的个数 。

子数组是数组中元素的连续非空序列。 """

import collections
from typing import List


class Solution:

    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = 0
        n = len(nums)
        preSums = collections.defaultdict(int)
        preSums[0] = 1  # 有这一条，下面的j才可以从0开始
        presum = 0
        for i in range(n):
            # presum:从0到i的子数组的和
            presum += nums[i]
            # preSums当前存放的是0~0、0~1、0~i-1的数组和的分布，此外和为0默认有个1
            # 我们要找从j开始，i结束的子数组的和等于k
            # 如果 presum - k = 0，意味着当前presume：从0到i的子数组的和满足条件
            # 此时 preSums[0]就表示的是 从0到i的子数组的和
            cnt += preSums[presum - k]
            # 下面语句执行后preSums存放的是0~0、0~1、0~i-1、0~i的数组和的分布
            preSums[presum] += 1
        return cnt
