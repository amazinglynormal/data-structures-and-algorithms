# Definition for a binary tree node.
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def trav(root):
            if root is None:
                return

            result.append(root.val)
            trav(root.left)
            trav(root.right)
        
        trav(root)
        return result