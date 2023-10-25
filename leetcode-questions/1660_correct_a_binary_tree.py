# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        seen = set()

        def invalid(root, seen) -> bool:
            if not root:
                return False

            seen.add(root.val)

            if root.right and root.right.val in seen:
                return True

            isRightInvalid = invalid(root.right, seen)
            isLeftInvalid = invalid(root.left, seen)
            if isRightInvalid:
                root.right = None
            if isLeftInvalid:
                root.left = None

        invalid(root, seen)

        return root
