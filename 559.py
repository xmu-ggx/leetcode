
class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0

        queue = [root]
        res = 0

        while queue:
            res += 1
            for i in range(len(queue)):
                node = queue.pop(0)
                for item in node.children:
                    if item is not None:
                        queue.append(item)
        return res

