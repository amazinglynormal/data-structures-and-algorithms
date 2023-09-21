class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


###########################################################


def buildTree(preorder, inorder):
    if not preorder:
        return

    root = TreeNode(preorder[0])

    inorderRootIdx = inorder.index(preorder[0])

    leftInorder = inorder[0:inorderRootIdx]
    leftPreorder = preorder[1 : len(leftInorder) + 1]

    root.left = buildTree(leftPreorder, leftInorder)

    rightInorder = inorder[inorderRootIdx + 1 :]
    rightPreorder = preorder[len(leftInorder) + 1 :]

    root.right = buildTree(rightPreorder, rightInorder)

    return root


############################################################


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


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]

root = buildTree(preorder, inorder)

print(inorderTraversal(root))
