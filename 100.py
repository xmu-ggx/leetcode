
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p, q):

        return self.bfs(p) == self.bfs(q)


    def bfs(self, node):
        l = [node]
        res = []

        while l:
            temp = l.pop(0)
            if not temp:
                res.append('null')
            else:
                res.append(temp.val)
                l.append(temp.left)
                l.append(temp.right)
        
        return res





            
