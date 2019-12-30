
class Solution:
    def binaryTreePaths(self, root):
        self.paths = []

        def dfs(node, curr_path):
            if node is None:
                return

            curr_path += str(node.val)
            if node.left is None and node.right is None:
                self.paths.append(curr_path)
            else:
                curr_path += '->'
                dfs(node.left, curr_path)
                dfs(node.right, curr_path)

        dfs(root, '')
        return self.paths
