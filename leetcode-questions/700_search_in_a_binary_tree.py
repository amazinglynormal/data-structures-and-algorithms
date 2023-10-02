class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def searchBST(root, val):
    node = root

    while node:
        if node.val == val:
            return node
        if val > node.val:
            node = node.right
        else:
            node = node.left

    return node
