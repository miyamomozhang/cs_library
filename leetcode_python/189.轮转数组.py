""" 189. 轮转数组
https://leetcode.cn/problems/rotate-array/

给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。 """

from typing import List


class Solution:

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 向右轮转k位，原来i位置的数在（i+k)%length 的位置
        n = len(nums)
        k %= n
        if k == 0:
            return
        preindex = i = 0
        old = nums[0]
        cnt = 0
        while cnt < n:
            new_index = (i + k) % n
            # 原来i位置的数放在 new_index 的位置
            # new_index原来放的数放在old中
            tmp = nums[new_index]
            nums[new_index] = old
            old = tmp
            cnt += 1
            # 下一轮我们要确定的是 new_index 对应的数 轮转后的位置
            i = new_index
            # 我们遍历的下标: 0 , k%n , 2k%n，……（中间有可能又回到0，遍历次数不够）
            # 如果要遍历的下标之前遍历过了，下一组：1，（1+k)%n,……
            if i == preindex:
                i += 1
                preindex = i
                old = nums[i]
