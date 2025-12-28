class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from math import inf
from typing import List 
from typing import Optional
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def dps(node: Optional[TreeNode], depth: int) -> None:
            if node is None:
                return
            if depth == len(ans):
                ans.append(node.val)
            dps(node.right, depth + 1)
            dps(node.left, depth + 1)
        dps(root, 0)
        return ans