from itertools import accumulate
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre = list(accumulate(nums, initial=0))
        ans = min_pre_sum = 0
        for j in range(1, len(pre)):
            ans = max(ans, pre[j] - min_pre_sum)
            min_pre_sum = min(min_pre_sum, pre[j])
        return ans

    def maxSubArray1(self, nums: List[int]) -> int:
        f = [0] * len(nums)
        f[0] = nums[0]
        for i in range(1, len(nums)):
            f[i] = max(f[i - 1], 0) + nums[i]
        return max(f)

    """ 由于计算 f[i] 只会用到 f[i - 1]，不会用到更早的状态，所以可以用一个变量滚动计算。"""
    def maxSubArray2(self, nums: List[int]) -> int:
        ans  = -int(1e9)
        f= 0 
        for x in nums:
            f = max(f, 0) + x
            ans = max(ans, f)
        return ans
        
""" 
https://leetcode.cn/problems/maximum-subarray/description/?envType=study-plan-v2&envId=top-100-liked
"""
