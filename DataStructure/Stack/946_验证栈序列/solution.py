from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i = 0 # 指针
        result = list()
        for ele in pushed:
            result.append(ele)
            while result and result[-1] == popped[i]:
                i += 1
                result.pop()
        return True if len(result)==0 else False

"""
https://leetcode.cn/problems/validate-stack-sequences/description/
"""