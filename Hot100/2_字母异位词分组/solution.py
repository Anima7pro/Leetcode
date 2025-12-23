from collections import defaultdict
from typing import Counter, List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cnt = defaultdict(int)
        num = 0
        result = [[] for _ in range(len(strs))]

        for j, string in enumerate(strs):
            c = Counter(string)
            key = tuple(sorted(c.items()))
            if key in cnt:
                result[cnt[key]].append(string)
            else:
                result[num].append(string)
                cnt[key] = num
                num += 1
        return list(filter(None, result))
    

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d =defaultdict(list)
        for s in strs:
            sorted_s = ''.join(sorted(s))
            d[sorted_s].append(s)
        return list(d.values())
    
