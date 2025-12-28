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
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dps(node):
            if node is None:
                return
            dps(node.left)
            ans.append(node.val)
            dps(node.right)
        
        ans = []
        dps(root)
        return ans[k-1]
