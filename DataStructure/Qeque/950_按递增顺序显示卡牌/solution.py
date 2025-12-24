from collections import deque


class Solution(object):
    def deckRevealedIncreasing(self, deck):
        n = len(deck)
        ans = [None] * n
        index = deque(range(n))
        
        for card in sorted(deck):
            ans[index.popleft()] = card
            if index:
                index.rotate(-1)
        return ans
""" 
https://leetcode.cn/problems/reveal-cards-in-increasing-order/description/
"""