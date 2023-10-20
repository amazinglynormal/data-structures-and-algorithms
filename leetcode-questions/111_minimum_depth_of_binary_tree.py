from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# DFS approach
class DFSSolution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        if root.left and root.right:
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

        if root.left:
            return 1 + self.minDepth(root.left)
        else:
            return 1 + self.minDepth(root.right)


# BFS approach
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque()
        queue.append(root)
        depth = 0

        while queue:
            depth += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left and node.right:
                    queue.append(node.left)
                    queue.append(node.right)
                elif node.left:
                    queue.append(node.left)
                elif node.right:
                    queue.append(node.right)
                else:
                    return depth
