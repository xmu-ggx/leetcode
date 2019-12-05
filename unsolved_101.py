
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    res1=[]
    res2=[]

    def isSymmetric(self, root):
        if not root:
            return True

        self.ldr_search(root.left)
        self.rdl_search(root.right)
        return self.res1 == self.res2


    def ldr_search(self, root):

        if not root:
            return
        else:
            self.ldr_search(root.left)
            self.res1.append(root.val)
            self.ldr_search(root.right)

    def rdl_search(self, root):

        if not root:
            return
        else:
            self.lrd_search(root.right)
            self.res2.append(root.val)
            self.lrd_search(root.left)

