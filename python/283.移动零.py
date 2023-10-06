""" 11. 盛最多水的容器
https://leetcode.cn/problems/container-with-most-water/

给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。

找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

返回容器可以储存的最大水量。

说明：你不能倾斜容器。 """

from typing import List


class Solution:

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n <= 1:
            return

        # slow 要存放非0数的位置
        slow = 0
        # fast 用来遍历
        fast = 0
        while fast < n:
            # 当前fast位置为0，说明不是slow位置要的数，继续找fast+1
            if nums[fast] != 0:
                # 非0值，交换, slow和fast双双往下走
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
            fast += 1
