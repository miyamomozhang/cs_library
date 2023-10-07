class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return n
        ans = 1
        start_index = 0
        end_index = 0
        for i in range(1, n):
            # 遍历节点
            # 如果节点 i 在s[start_index, end_index+1]中出现，位置为index
            # 那么start_index更新为index+1，end_index更新为 i
            for j in range(start_index, end_index + 1):
                if s[i] == s[j]:
                    start_index = j + 1
                    break
            end_index = i
            # 算出以当前位置为结束的当前子串长度
            cur_ans = end_index - start_index + 1
            ans = max(ans, cur_ans)
        return ans
