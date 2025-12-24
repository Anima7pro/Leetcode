from collections import defaultdict


class Solution:
    def calculateScore(self, s: str) -> int:
        ans = 0
        cnt = defaultdict(list)
        for j, ele in enumerate(s):
            mirror = 219 - ord(ele)
            if mirror in cnt and cnt[mirror]:
                ans += j - cnt[mirror][-1]
                cnt[mirror].pop()
                if cnt[mirror] == []:
                    del cnt[mirror]
                continue
            cnt[ord(ele)].append(j)
        return ans

        