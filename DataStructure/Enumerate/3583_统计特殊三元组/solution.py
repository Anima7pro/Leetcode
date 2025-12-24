from collections import Counter, defaultdict
from typing import List


class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 1_000_000_007
        suf = Counter(nums)
        ans = 0
        pre = defaultdict(int)
        for x in nums:
            suf[x] -= 1
            ans += suf[x*2] * pre[x*2]
            pre[x] += 1
        return ans % MOD
    
"""

https://leetcode.cn/problems/count-special-triplets/description/

"""