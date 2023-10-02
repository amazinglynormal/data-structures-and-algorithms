class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def getMinNode(root):
    curr = root
    while curr and curr.left:
        curr = curr.left
    return curr


def deleteNode(root, key):
    if not root:
        return None

    if key < root.val:
        root.left = deleteNode(root.left, key)
    elif key > root.val:
        root.right = deleteNode(root.right, key)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        else:
            minNode = getMinNode(root.right)
            root.val = minNode.val
            root.right = deleteNode(root.right, minNode.val)

    return root
