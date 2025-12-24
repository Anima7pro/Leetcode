from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums = sorted(nums)
        ans = set()
        if n == 3:
            return [] if sum(nums)!=0 else [nums]

        for i in range(n - 3):
            cnt = {}
            #nums_j = nums[i+1: ]
            for j in range(i+1, n):
            #for j, ele in enumerate(nums_j):               
                nums_k = -(nums[i]+nums[j])
                if nums_k in cnt:
                    ans.add((nums[i], nums[j], nums_k))
                cnt[nums[j]] = True
        return [list(t) for t in ans]
                

