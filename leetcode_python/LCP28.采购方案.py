""" LCP 28. 采购方案
https://leetcode.cn/problems/4xy4Wx/
小力将 N 个零件的报价存于数组 nums。小力预算为 target，假定小力仅购买两个零件，要求购买零件的花费不超过预算，请问他有多少种采购方案。

注意：答案需要以 1e9 + 7 (1000000007) 为底取模，如：计算初始结果为：1000000008，请返回 1 """

from typing import List


class Solution:

    def purchasePlans(self, nums: List[int], target: int) -> int:
        # 先排序
        nums.sort()
        ans = 0
        left, right = 0, len(nums) - 1
        while left < right:
            tmp = nums[left] + nums[right]
            if tmp <= target:
                # right满足条件，left 和 right及right左边的数组合都满足条件
                ans += right - left
                # 下一轮，left要右移
                left += 1
            else:
                # right太大了，right左移
                right -= 1
        return int(ans % (1e9 + 7))
