class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        cnt = set()
        ans = 0
        i = 0
        for j, ele in enumerate(s):
            while ele in cnt:
                cnt.remove(s[i])
                i += 1
            cnt.add(ele)
            ans = max(ans, j - i + 1)
        return ans