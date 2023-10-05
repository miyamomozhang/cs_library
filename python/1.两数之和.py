""" 1. 两数之和
https://leetcode.cn/problems/two-sum/

给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。 """

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # num_index，字典，nums中元素为key,对应的数组下标为value
        num_index = {}
        # enumerate，用于可迭代的对象，同时得到下标和对应的值
        for i,num in enumerate(nums):
            # 对于当前num,在哈希表中找target-num
            tmp = target - num
            if  tmp in num_index.keys():
                return [num_index[tmp],i]
            # 没找到，把当前num存入哈希表
            num_index[num] = i
        return []
