
class Solution:
    def insertIntoBST(self, root, val):
        if root is None:
            root = TreeNode(val)
            return root

        cur = root
        node = TreeNode(val)

        while True:
            if cur.val > val:
                if cur.left is None:
                    cur.left = node
                    return root
                else:
                    cur = cur.left
            else:
                if cur.right is None:
                    cur.right = node
                    return root
                else:
                    cur = cur.right


