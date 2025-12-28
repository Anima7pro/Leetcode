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
    # 前序遍历，左节点在 (left, x) 之间, 右节点在 (x, right) 之间
    def isValidBST(self, root: Optional[TreeNode], left = -inf, right = inf) -> bool:
        if root is None:
            return True
        x = root.val
        return left < x < right and self.isValidBST(root.left, left, x) and self.isValidBST(root.right, x, right)
    
    # 中序遍历
