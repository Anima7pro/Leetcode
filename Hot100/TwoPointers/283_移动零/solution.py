from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        stack_size = 0
        for i, num in enumerate(nums):
            if num:
                nums[stack_size] = num
                stack_size += 1
        nums[stack_size: ] = [0] * (n - stack_size)


class Solution:
    def moveZeroes1(self, nums: List[int]) -> None:
        i0 = 0
        for i, num in enumerate(nums):
            if num:
                nums[i0], nums[i] = nums[i], nums[i0]
                i0 += 1
            
            
            
        