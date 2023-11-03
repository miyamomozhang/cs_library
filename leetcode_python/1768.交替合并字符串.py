""" 1768. 交替合并字符串
https://leetcode.cn/problems/merge-strings-alternately/
给你两个字符串 word1 和 word2 。请你从 word1 开始，通过交替添加字母来合并字符串。如果一个字符串比另一个字符串长，就将多出来的字母追加到合并后字符串的末尾。

返回 合并后的字符串 。 """


class Solution:

    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1 = len(word1)
        len2 = len(word2)
        word = ""
        first = 0
        second = 0
        while first < len1 and second < len2:
            word += word1[first] + word2[second]
            first += 1
            second += 1
        while first < len1:
            word += word1[first]
            first += 1
        while second < len2:
            word += word2[second]
            second += 1
        return word
