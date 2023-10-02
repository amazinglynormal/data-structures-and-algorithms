from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rightSideView(root):
    vals = []

    if not root:
        return vals

    queue = deque()

    queue.append(root)

    while len(queue) > 0:
        for _ in range(len(queue)):
            node = queue.popleft()
            vals.append(node.val)
            if node.right:
                queue.append(node.right)
            elif node.left:
                queue.append(node.left)

    return vals
