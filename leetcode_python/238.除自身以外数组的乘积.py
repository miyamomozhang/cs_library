""" 238. 除自身以外数组的乘积
https://leetcode.cn/problems/product-of-array-except-self/

给你一个整数数组 nums，返回 数组 answer ，其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积 。

题目数据 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内。

请 不要使用除法，且在 O(n) 时间复杂度内完成此题。 """

from typing import List


class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        cnt_0 = nums.count(0)
        n = len(nums)
        if cnt_0 >= 2:
            # 有两个或两个以上的0，返回全0
            return [0] * n
        if cnt_0 == 1:
            # 有一个0，除了index_0位置不为0，其它都是0
            ans = [0] * n
            tmp = 1
            for i, num in enumerate(nums):
                if num != 0:
                    # 非零值相乘
                    tmp *= num
                else:
                    # ans中非零值的位置
                    index_0 = i
            ans[index_0] = tmp
            return ans
        else:
            # 全都不是0
            ans = []
            # left[i]、right[i]分别是i左边所有数的乘积、右边所有数的乘积
            left = [1] * n
            right = [1] * n
            for i in range(1, n):
                left[i] = nums[i - 1] * left[i - 1]
            # 注意range反向遍历的写法！！！reversed函数
            for j in reversed(range(n - 1)):
                right[j] = right[j + 1] * nums[j + 1]
            for i in range(n):
                ans.append(left[i] * right[i])
            return ans
