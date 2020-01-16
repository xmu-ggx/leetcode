
class Solution:
    def inorderTraversal(self, root):
        if root is None:
            return root
        res = []
        stack = []

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop()
            res.append(node.val)
            root = node.right
        return res


