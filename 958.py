
class Solution:
    def isCompleteTree(self, root):
        item_list = []
        queue = [root]

        while len(queue):
            node = queue.pop(0)
            if node is None:
                item_list.append(-10)
            else:
                item_list.append(node.val)
                queue.append(node.left)
                queue.append(node.right)

        for i in range(len(item_list)):
            if item_list[i] == -10:
                for j in item_list[i+1:]:
                    if j != -10:
                        return False
                return True


