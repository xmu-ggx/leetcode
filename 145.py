
class Solution:
    def postorderTraversal(self, root):
        if root is None:
            return []

        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.left is not None: stack.append(node.left)
            if node.right is not None: stack.append(node.right)

        return res[::-1]


