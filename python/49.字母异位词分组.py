""" 49. 字母异位词分组
https://leetcode.cn/problems/group-anagrams/

给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。

字母异位词 是由重新排列源单词的所有字母得到的一个新单词。
 """
from typing import List


class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        if n <= 1:
            return [strs]
        str_hash = {}
        for str in strs:
            # 注意：list列表是不可哈希的，不能当做字典的key
            sorted_str = tuple(sorted(str))  # 转成tuple元组,可哈希，做key
            # sorted()：new list  可应用在所有的可迭代对象，不改变原对象，返回一个新的对象
            # L.sort()：in-place  应用在 list 上的方法，改变原来的list
            if sorted_str in str_hash.keys():
                str_hash[sorted_str].append(str)
            else:
                str_hash[sorted_str] = [
                    str,
                ]
        # dict.values()得到的是dict_values对象
        # Python3 字典 values() 方法返回一个视图对象。视图对象:元组
        # dict.keys()、dict.values() 和 dict.items() 返回的都是视图对象（ view objects），提供了字典实体的动态视图，这就意味着字典改变，视图也会跟着变化。
        # 视图对象不是列表，不支持索引，可以使用 list() 来转换为列表。
        # 我们不能对视图对象进行任何的修改，因为字典的视图对象都是只读的。
        """例子
        a = {'a':[1,3,5],'b':[2,4,6]}
        print(a.keys())  
        print(a.values())  
        print(a.items())

        dict_keys(['a', 'b'])
        dict_values([[1, 3, 5], [2, 4, 6]])
        dict_items([('a', [1, 3, 5]), ('b', [2, 4, 6])])
        """
        return list(str_hash.values())


""" 力扣官方参考，使用了collections容器
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 使用 list 作为 default_factory, 将key-value转换为key-list字典
        mp = collections.defaultdict(list)

        for st in strs:
            key = "".join(sorted(st))
            mp[key].append(st)
        
        return list(mp.values())

作者：力扣官方题解
链接：https://leetcode.cn/problems/group-anagrams/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
