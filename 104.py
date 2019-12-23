
class TreeNode:
    def __init__(self, x):
        self.x = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
