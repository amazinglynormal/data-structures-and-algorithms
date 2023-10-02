class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def hasPathSum(root, targetSum):
    if not root:
        return False

    targetSum -= root.val

    if not root.left and not root.right:
        if targetSum == 0:
            return True
        return False

    left = hasPathSum(root.left, targetSum)
    right = hasPathSum(root.right, targetSum)

    if left or right:
        return True

    return False
