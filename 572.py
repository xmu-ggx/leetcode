
class Solution:
    def isSubtree(self, s, t):
        target = self.levelSearch(t)
        queue = [s]
        while queue:
            node = queue.pop(0)
            if self.levelSearch(node) == target:
                return True
            if node.left is not None: queue.append(node.left)
            if node.right is not None: queue.append(node.right)
        return False

    def levelSearch(self, root):
        if root is None:
            return ''

        queue = [root]
        res = ''
        while queue:
            node = queue.pop(0)
            if node is not None:
                res += str(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                res += '#'
        return res
