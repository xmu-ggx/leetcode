
class Solution:
    def rightSideView(self, root):
        if root is None:
            return []
        res = []
        queue = [root]
        while queue:
            n = len(queue)
            for _ in range(n):
                node = queue.pop(0)
                if _ == n-1: res.append(node.val)
                if node.left is not None:queue.append(node.left)
                if node.right is not None:queue.append(node.right)
        return res
