from itertools import accumulate
from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        pre = list(accumulate(nums, initial = 0))
        self.pre = pre
        

    def sumRange(self, left: int, right: int) -> int:
        return self.pre[right+1] - self.pre[left]
        # s[i] = a[0] + a[1] + ... + a[i - 1]
        # s[i + 1] = a[0] + a[1] + ... + a[i - 1] + a[i]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)