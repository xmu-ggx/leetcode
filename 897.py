class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def increasingBst(self, root):
        ls = self.ldr_search(root)
        node_ls = [TreeNode(x) for x in ls]
        for i in range(len(node_ls)-1):
            node_ls[i].right = node_ls[i+1]
        return node_ls[0]


    def ldr_search(self, root):
        if root is None:
            return []

        stack = []
        res = []

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            if stack:
                node = stack.pop()
                res.append(node.val)
                root = node.right
        return res
            


