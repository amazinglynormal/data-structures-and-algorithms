from typing import Optional
from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __str__(self) -> str:
        return f"val = {self.val}, neighbors = {self.neighbors}"


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return None

        nodes = {}
        queue = deque()
        queue.append(node)

        while queue:
            node = queue.popleft()
            clone = Node(node.val) if not nodes.get(node.val) else nodes.get(node.val)
            for neighbor in node.neighbors:
                if nodes.get(neighbor.val):
                    clone.neighbors.append(nodes.get(neighbor.val))
                else:
                    new_node = Node(neighbor.val)
                    clone.neighbors.append(new_node)

                    nodes.update({neighbor.val: new_node})
                    queue.append(neighbor)
            nodes.update({node.val: clone})

        return nodes.get(1)
