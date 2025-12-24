from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        stack = []
        for i in range(n-1, -1, -1):
            t = temperatures[i]
            while stack and t >= temperatures[stack[-1]]:
                stack.pop()
            if stack:
                ans[i] = stack[-1] - i
            stack.append(i)
        return ans
    
class Solution:
    def dailyTemperatures1(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        st = []
        for i in range(n):
            t = temperatures[i]
            while st and t > temperatures[st[-1]]:
                idx = st.pop()
                ans[idx] = i - idx
            st.append(i)
        return ans