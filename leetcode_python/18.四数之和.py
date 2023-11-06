""" 18. 四数之和
https://leetcode.cn/problems/4sum/
给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。请你找出并返回满足下述全部条件且不重复的四元组 [nums[a], nums[b], nums[c], nums[d]] （若两个四元组元素一一对应，则认为两个四元组重复）：

0 <= a, b, c, d < n
a、b、c 和 d 互不相同
nums[a] + nums[b] + nums[c] + nums[d] == target
你可以按 任意顺序 返回答案 。 """

from typing import List


class Solution:

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # 先排序
        nums.sort()
        # 答案
        ans = []
        n = len(nums)
        for first in range(n - 3):
            if first != 0 and nums[first - 1] == nums[first]:
                # 和上一次first循环重复了，下一轮
                continue
            for second in range(first + 1, n - 2):  # 每一轮 second 从 first+1 开始
                if second != first + 1 and nums[second - 1] == nums[second]:
                    # 和上一次second循环重复了，下一轮
                    continue
                third, fourth = second + 1, n - 1
                while third < fourth:
                    if third != second + 1 and nums[third - 1] == nums[third]:
                        # 和上一次third循环重复了，下一轮
                        third += 1
                        continue
                    tmp = nums[first] + nums[second] + nums[third] + nums[
                        fourth]
                    if tmp == target:
                        l = [
                            nums[first], nums[second], nums[third],
                            nums[fourth]
                        ]
                        ans.append(l)
                        third += 1
                        fourth -= 1
                    elif tmp < target:
                        third += 1
                    else:
                        fourth -= 1
        return ans
