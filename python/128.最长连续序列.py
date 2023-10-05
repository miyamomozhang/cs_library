""" 128. 最长连续序列
https://leetcode.cn/problems/longest-consecutive-sequence/

给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

请你设计并实现时间复杂度为 O(n) 的算法解决此问题。 """

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n
        # set无序，唯一
        ans = 0
        num_set = set(nums)
        for num in num_set:
            # 只有没有遍历到的num才需要遍历，看以num开始的序列有多长
            # 如果 num-1 在num_set中出现了，说明至少应该从num-1开始遍历，不应该从num开始
            if num - 1 not in num_set:
                cur_num = num
                cur_ans = 1
                while cur_num + 1 in num_set:
                    cur_num += 1
                    cur_ans += 1
                ans = max(ans, cur_ans)
        return ans



