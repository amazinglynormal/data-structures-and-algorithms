class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(root):
    vals = []

    def inorder(node):
        if not node:
            return

        inorder(node.left)
        vals.append(node.val)
        inorder(node.right)

    inorder(root)

    return vals
