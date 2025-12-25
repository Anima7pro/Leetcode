from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda p :p[0])
        ans = []
        for x in intervals:
            if ans and ans[-1][1] >= x[0]:
                ans[-1][1] = max(x[1], ans[-1][1])
            else:
                ans.append(x)
        return ans