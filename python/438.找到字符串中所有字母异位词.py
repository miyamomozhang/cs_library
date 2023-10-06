""" 438. 找到字符串中所有字母异位词
https://leetcode.cn/problems/find-all-anagrams-in-a-string/

给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。

异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。 """

from typing import List


class Solution:

    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        len_p = len(p)
        sorted_p = sorted(p)
        len_s = len(s)
        for i in range(0, len_s + 1 - len_p):
            tmp = s[i:i + len_p]
            if sorted(tmp) != sorted_p:
                continue
            else:
                ans.append(i)

        return ans
