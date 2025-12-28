# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from math import inf
from typing import List 
from typing import Optional

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = -inf
        def dps(root: Optional[TreeNode]):
            if root is None:
                return 0
            l_val = dps(root.left)
            r_val = dps(root.right)
            nonlocal ans
            ans = max(l_val + r_val + root.val, ans)
            return max(max(l_val, r_val) + root.val)

        dps(root)
        return ans
