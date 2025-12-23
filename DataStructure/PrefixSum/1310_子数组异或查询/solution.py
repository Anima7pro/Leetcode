from typing import List


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        pre = [0] * (len(arr)+1)
        for i, num in enumerate(arr):
            pre[i+1] = pre[i] ^ num
        return [pre[r+1]^pre[l] for l, r in queries]
        

        