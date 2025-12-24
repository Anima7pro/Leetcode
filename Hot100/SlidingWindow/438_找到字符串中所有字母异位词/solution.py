from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        cnt_p = Counter(p)
        cnt_s = Counter()
        ans = []
        for right, ele in enumerate(s):
            cnt_s[ele] += 1
            left = right-len(p)+1
            if left < 0:
                continue
            if cnt_s == cnt_p:
                ans.append(left)
            out = s[left]
            cnt_s[out] -= 1
            if cnt_s[out] == 0:
                del cnt_s[out]
        return ans
            
            




        