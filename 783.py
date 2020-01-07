
class Solution:
    def minDiffInBST(self,  root):
        ll = self.inorderTraversal(root)
        min_ = ll[1] - ll[0]
        for i in range(len(ll)-1):
            if ll[i+1] - ll[i] < min_:
                min_ = ll[i+1] - ll[i]
        return min_

    def inorderTraversal(self, root):
        if root is None:
            return []

        stack = []
        res = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            if stack:
                a = stack.pop()
                res.append(a.val)
                root = a.right
        return res
