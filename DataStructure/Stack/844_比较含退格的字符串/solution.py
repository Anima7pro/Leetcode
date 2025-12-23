def stack(s: str) -> str:
    ans = []
    for char_s in s:
        if char_s != '#':
            ans.append(char_s)
        elif len(ans)==0 :
            continue
        else:
            ans.pop()
    return "".join(ans)
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return stack(s) == stack(t)

""" 
https://leetcode.cn/problems/backspace-string-compare/description/

"""
        