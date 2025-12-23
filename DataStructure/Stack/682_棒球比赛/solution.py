from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans = []
        charlist = ["C","D","+"]
        for ele in operations:
            if ele not in charlist:
                ans.append(int(ele))
            elif ele == charlist[0]:
                ans.pop()
            elif ele == charlist[1]:
                ans.append(ans[-1]*2)
            else:
                ans.append(ans[-1]+ans[-2])

        return sum(ans)

""" 
https://leetcode.cn/problems/baseball-game/
"""