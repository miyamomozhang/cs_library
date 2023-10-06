""" 20. 有效的括号
https://leetcode.cn/problems/valid-parentheses/

给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

    左括号必须用相同类型的右括号闭合。
    左括号必须以正确的顺序闭合。
    每个右括号都有一个对应的相同类型的左括号。 
"""


class Solution:

    def isValid(self, s: str) -> bool:
        n = len(s)
        if n % 2 == 1:
            return False
        pairs = {')': '(', ']': '[', '}': '{'}
        left_brackets = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                left_brackets.append(c)
            else:
                # 当前遍历到右括号
                if len(left_brackets) == 0:
                    # 前面没有左括号，返回 false
                    return False
                elif left_brackets.pop() != pairs[c]:
                    # 左右括号不匹配，返回 false
                    return False
        # 还有左括号没有被匹配，返回false
        if len(left_brackets) != 0:
            return False
        # 都匹配完成，返回True
        return True
