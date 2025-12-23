from itertools import accumulate
from typing import List


class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        pre = list(accumulate(nums, initial = 0))
        ans = 0
        for i, num in enumerate(nums):
            ans += pre[i+1] - pre[max(0,i-num)]
        return ans

        