""" 15. 三数之和
https://leetcode.cn/problems/3sum/

给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请

你返回所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。 """
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        # nums排序
        nums.sort()
        # ans 存放结果
        ans = []
        # i<j<k
        i = 0
        j = 1
        k = n - 1
        while i < n - 2:
            if i > 0 and nums[i] == nums[i-1]:
                # 跟上一轮重复了，下一个
                i += 1
                continue
            j = i + 1
            k = n - 1
            while j < k:
                if j > i + 1 and nums[j] == nums[j-1]:
                    # 跟上一轮重复了，下一个
                    j += 1
                    continue
                if nums[i] + nums[j] + nums[k] == 0:
                    # 符合条件，存进去
                    ans.append([nums[i], nums[j], nums[k]])
                    # 开始里面(j,k)的下一轮
                    j += 1
                    k -= 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    # 太大了，k左移
                    k -= 1
                else:
                    # 太小了，j右移
                    j += 1
            # 开始下一轮
            i += 1
        return ans

