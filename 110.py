
class Solution:
    def isBalanced(self, root):
        if root is None:
            return True
        queue = [root]
        while queue:
            node = queue.pop(0)
            if abs(self.getTreeHeight(node.left) - self.getTreeHeight(node.right)) > 1:
                return False
            if node.left is not None: queue.append(node.left)
            if node.right is not None: queue.append(node.right)
        return True

    def getTreeHeight(self, root):
        if root is None:
            return 0
        queue = [root]
        res = 0
        while queue:
            res += 1
            for i in range(len(queue)):
                node = queue.pop(0)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
        return res
                        
