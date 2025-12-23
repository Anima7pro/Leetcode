from itertools import accumulate, pairwise
from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        s = list(accumulate((x % 2 == y % 2 for x, y in pairwise(nums)),initial = 0))
        return [s[from_] == s[to_] for from_, to_ in queries]
    

""" 
定义一个长为 n-1 的数组 a， 其中 a[i] = 1 当且仅当 nums[i] 和 nums[i+1] 同奇偶性，否则 a[i] = 0。

则对于每个查询 [from, to]，判断 nums[from] 和 nums[to] 是否同奇偶性等价于判断 a[from..to-1] 中是否全为 1，即判断 sum(a[from..to-1]) == to - from。

预处理时，计算前缀和 s，其中 s[i] = sum(a[0..i-1])。

则 sum(a[from..to-1]) = s[to] - s[from]，从而判断条件等价于 s[to] - s[from] == to - from，即 s[to] == s[from]。

"""

        