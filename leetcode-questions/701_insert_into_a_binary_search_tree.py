class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insertIntoBSTRecursive(root, val):
    if not root:
        return TreeNode(val)

    if val > root.val:
        root.right = insertIntoBSTRecursive(root.right, val)
    elif val < root.val:
        root.left = insertIntoBSTRecursive(root.left, val)
    else:
        return root


def insertIntoBST(root, val):
    if not root:
        return TreeNode(val)

    curr = root

    while curr:
        if val < curr.val:
            if curr.left:
                curr = curr.left
            else:
                curr.left = TreeNode(val)
                break
        else:
            if curr.right:
                curr = curr.right
            else:
                curr.right = TreeNode(val)
                break

    return root
