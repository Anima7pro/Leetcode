from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        m = n - k % n
        nums += [0] * m
        for i in range(m):
            nums[i + n] = nums[i]
            nums[i] = 0
        nums[:] = nums[m:]

    def rotate1(self, nums: List[int], k: int) -> None:
        def reverse(i: int, j: int) -> None:
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            n = len(nums)
            reverse(0, n - 1)
            reverse(0, k - 1)
            reverse(k, n - 1)

        """
        Do not return anything, modify nums in-place instead.
        """
