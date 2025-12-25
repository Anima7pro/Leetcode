from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        ans = []
        for i, num in enumerate(nums): # 遍历nums中的元素
            while q and num >= nums[q[-1]]: # 如果q不为空且nums[i]大于q的队尾的下标对应的nums的值
                q.pop() # 则弹出，一直到第一个大于num的数字，此时队首储存的永远是窗口中最大值，因为超出窗口的下标已经在下面的代码中被弹出
            q.append(i)
            if q[0] < i - k: # 如果下标代码超限
                q.popleft() # 弹出
            if i > k - 1: # 如果窗口形成
                ans.append(nums[q[0]]) # 更新答案
        return ans
    
""" 
https://leetcode.cn/problems/sliding-window-maximum/description/?envType=study-plan-v2&envId=top-100-liked
"""
