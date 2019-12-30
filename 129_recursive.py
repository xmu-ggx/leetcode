
class Solution:
    def sumNumbers(self, root):
        self.sum = 0
        
        def dfs(node, curr_num):
            if node is None:
                return
            curr_num += node.val
            if node.left is None and node.right is None:
                self.sum += curr_num
            else:
                curr_num *= 10
                dfs(node.left, curr_num)
                dfs(node.right, curr_num)

        dfs(root, 0)
        return self.sum

