""" 11. 盛最多水的容器 
https://leetcode.cn/problems/container-with-most-water/
给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。

找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

返回容器可以储存的最大水量。

说明：你不能倾斜容器。 """

from typing import List


class Solution:

    def maxArea(self, height: List[int]) -> int:
        # 双指针
        # 容积 = 宽 * 高
        # 宽度最开始是最大的，那么唯一可能让容器变大的方法就是高度了
        n = len(height)
        # left 和 right 分别指向两端
        left = 0
        right = n - 1
        max_volume = 0
        while left < right:
            # left和right, 哪个高度小哪个移
            if height[left] > height[right]:
                cur_volume = height[right] * (right - left)
                right -= 1
            else:
                cur_volume = height[left] * (right - left)
                left += 1
            max_volume = max(max_volume, cur_volume)

        return max_volume
