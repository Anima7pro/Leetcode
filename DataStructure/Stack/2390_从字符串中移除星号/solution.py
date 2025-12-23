class Solution:
    def removeStars(self, s: str) -> str:
        ans = []
        for cha in s:
            if cha != "*":
                ans.append(cha)
            else:
                ans.pop()
        return "".join(ans)
        
"""
https://leetcode.cn/problems/remove-stars-from-a-string/
"""