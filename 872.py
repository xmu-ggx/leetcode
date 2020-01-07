
class Solution:
    def leafSimilar(self, root1, root2):
        return self.depth_search(root1) == self.depth_search(root2)

    def depth_search(self, root):
        if root is None:
            return []

        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            if node.left is None and node.right is None:
                res.append(node.val)
            if node.left is not None: stack.append(node.left)
            if node.right is not None: stack.append(node.right)
        return res
