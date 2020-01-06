
class Solution:
    def largestValues(self, root):
        if root is None:
            return []

        res, queue = [], [root]

        while len(queue):
            max_ = float('-inf')
            for i in range(len(queue)):
                node = queue.pop(0)
                if node.val > max_:
                    max_ = node.val
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            res.append(max_)
        return res

