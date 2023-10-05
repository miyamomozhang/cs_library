""" 136. 只出现一次的数字
https://leetcode.cn/problems/single-number/

给你一个 非空 整数数组 nums ，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

你必须设计并实现线性时间复杂度的算法来解决此问题，且该算法只使用常量额外空间。 
"""

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        # 异或，相同的数异或为0
        for num in nums:
            ans ^= num
        # 就算只出现一次的数是0也没关系，因为异或出来还是0
        return ans