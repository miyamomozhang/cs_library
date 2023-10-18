""" 27. 移除元素
https://leetcode.cn/problems/remove-element/
给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。

不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。 """
from typing import List


class Solution:

    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        # 1. val的个数，当前数不为val，前面有多少个val，当前数就需要往前挪几个
        """ cnt = 0
        for i in range(n):
            if nums[i] == val:
                cnt += 1
            else:
                nums[i - cnt] = nums[i]
        return n - cnt """
        # 2. 双指针
        # slow:不为val的数存放的位置
        # num:遍历原来的数组
        slow = 0
        for num in nums:
            if num != val:
                nums[slow] = num
                slow += 1
        return slow
