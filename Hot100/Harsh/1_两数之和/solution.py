from collections import defaultdict
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx = defaultdict()
        for i, ele in enumerate(nums):
            if target- ele in idx:
                return [idx[target - ele], i]
            idx[ele] = i