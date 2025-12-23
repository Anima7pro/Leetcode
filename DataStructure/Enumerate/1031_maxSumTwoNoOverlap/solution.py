
from itertools import accumulate
from typing import List


class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        s = list(accumulate(nums, initial = 0))
        ans = maxSumA = maxSumB = 0
        for i in range(firstLen + secondLen, len(s)):
            maxSumA = max(maxSumA, s[i - secondLen] - s[i- secondLen - firstLen])
            # second 在 first 的右面
            maxSumB = max(maxSumB, s[i - firstLen]-s[i-secondLen-firstLen])
            # second 在 first 的左面
            ans = max(ans, maxSumA + s[i] - s[i - secondLen], maxSumB + s[i] - s[i - firstLen])
        return ans

        