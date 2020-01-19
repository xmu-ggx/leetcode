
class Solution:
    def findMode(self, root):
        if root is None:
            return []
        ls = self.inorderSearch(root)

        hashtable = {}
        for i in ls:
            if i in hashtable:
                hashtable[i] += 1
            else:
                hashtable[i] = 1

        max_ = max(hashtable.values())
        res = []
        for num in hashtable:
            if hashtable[num] == max_:
                res.append(num)
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

