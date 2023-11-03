""" 209. 长度最小的子数组
https://leetcode.cn/problems/minimum-size-subarray-sum/

找出该数组中满足其总和大于等于 target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。 """
from typing import List


class Solution:

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        sums = [0] * (n + 1)
        ans = 0
        for i, num in enumerate(nums):
            # sums[i]： range(0,i)的和
            sums[i + 1] = num + sums[i]
            if ans == 0 and sums[i + 1] >= target:
                ans = i + 1
        if sums[n] < target:
            # 所有数的和都 < target，没有满足条件的子数组
            return 0
        # i~j的和：sums[j+1] - sums[i]，这个长度j-i+1的选取要 < 前面的 ans
        # i从1开始
        for i in range(1, n):
            # j-i+1<ans   j<ans+i-1
            for j in range(i + 1, ans + i - 1):
                if sums[j] - sums[i] >= target:
                    ans = j - i - 1
                    if ans == 1:
                        return ans
                    break
        return ans
