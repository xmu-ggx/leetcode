from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def averageOfLevels(self, root)-> List[float]:
        d = deque()
        d.append(root)
        res = []

        while d:
            addition = 0
            count = 0

            for _ in range(len(d)):
                temp = d.popleft()
                if temp is not None:
                    addition += temp.val
                    count += 1
                    if temp.left is not None : d.append(temp.left)
                    if temp.right is not None : d.append(temp.right)
            res.append(addition/count)
            
        return res
                
                

