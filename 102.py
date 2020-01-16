
class Solution:
    def levelOrder(self, root):
        if root is None:
            return []
        res = []
        queue = [root]
        while queue:
            temp = []
            for i in range(len(queue)):
                node = queue.pop(0)
                temp.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)

            res.append(temp)
        return res
