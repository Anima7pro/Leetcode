from collections import defaultdict
from itertools import accumulate
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        pre = list(accumulate(nums, initial=0))
        cnt = defaultdict(int)
        for s in pre:
            # ans += cnt[s-k]
            # cnt[s] += 1
            if s - k in cnt:
                ans += cnt[s - k]
            cnt[s] += 1
        return ans
    
""" 
https://leetcode.cn/problems/subarray-sum-equals-k/description/?envType=study-plan-v2&envId=top-100-liked
"""
