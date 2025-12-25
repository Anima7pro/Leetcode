from collections import defaultdict
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        cnt = defaultdict(list)
        multiply = 1
        for j, num in enumerate(nums):
            cnt[num].append(j)
            multiply *= num if num != 0 else 1

        if len(cnt[0]) > 1:
            return [0] * len(nums)
        if len(cnt[0]) == 1:
            ans[cnt[0][0]] = multiply
            return ans
        for i in range(len(nums)):
            ans[i] = multiply // nums[i]
        return ans

# 前后缀积

    def productExceptSelf1(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = surf = [1] * n

        for i in range(1, n):
            pre[i] = pre[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            surf[i] = surf[i + 1] * nums[i + 1]

        return [p * s for p, s in zip(pre, surf)]


# 优化前后缀积
# 在更新答案的同时计算pre

    def productExpectSelf2(self, nums: List[int]) -> List[int]:
        n = len(nums)
        surf = [1] * n
        for i in range(n-2,-1,-1):
            surf[i] = surf[i+1] * nums[i+1]
        
        pre = 1
        for i, x in enumerate(nums):
            surf[i] *= pre
            pre *= x

""" 
https://leetcode.cn/problems/product-of-array-except-self/description/?envType=study-plan-v2&envId=top-100-liked
"""