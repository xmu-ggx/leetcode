
class Solution:
    def findTilt(self, root):
        if root is None:
            return 0
        result = 0
        queue = [root]
        while len(queue):
            node = queue.pop()

            if node.left is None:
                a = 0
            else:
                a = self.bfs_sum(node.left)
                queue.append(node.left)

            if node.right is None:
                b = 0
            else:
                b = self.bfs_sum(node.right)
                queue.append(node.right)
            result += abs(a-b)
        return result


    def bfs_sum(self, node):
        res = 0
        queue = [node]
        while len(queue):
            curr_node = queue.pop()
            if curr_node is None:
                continue
            else:
                res += curr_node.val
                queue.append(curr_node.left)
                queue.append(curr_node.right)
        return res

