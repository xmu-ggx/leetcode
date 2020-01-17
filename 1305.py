
class Solution:
    def getAllElements(self, root1, root2):
        l1, l2, res = self.inorderSearch(root1), self.inorderSearch(root2), []
        i, j, m, n = 0, 0, len(l1), len(l2)
        while i < m and j < n:
            if l1[i] <= l2[j]:
                res.append(l1[i])
                i += 1
            else:
                res.append(l2[j])
                j += 1
        if i == m:
            res.extend(l2[j:])
        else:
            res.extend(l1[i:])
        return res

    def inorderSearch(self, root):
        if root is None:
            return []
        
        stack = []
        res = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop()
            res.append(node.val)
            root = node.right
        return res
     
