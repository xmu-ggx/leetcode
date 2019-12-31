
class Solution:
    def isSymmetric(self,root):
        return self.dlrSearch(root.left) == self.drlSearch(root.right)
    
    def dlrSearch(self, node):
        res = []
        stack = [node]
        while len(stack):
            curr_node = stack.pop()
            if curr_node is None:
                res.append(-1)
            else:

                res.append(curr_node.val)
                stack.append(curr_node.right)
                stack.append(curr_node.left)
        return res

    def drlSearch(self, node):
        res = []
        stack = [node]
        while len(stack):
            curr_node = stack.pop()
            if curr_node is None:
                res.append(-1)
            else:
                res.append(curr_node.val)
                stack.append(curr_node.left)
                stack.append(curr_node.right)
        return res

