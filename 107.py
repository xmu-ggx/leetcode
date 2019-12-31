
class Solution:
    def levelOrderBottom(self, root):
        if root is None:return []
        queue = [root]
        res = []
        while queue:
            curr_res = []
            for i in range(len(queue)):
                temp = queue.pop(0)
                curr_res.append(temp.val)
                if temp.left is not None:
                    queue.append(temp.left)
                if temp.right is not None:
                    queue.append(temp.right)
            res.append(curr_res)

        return res[::-1]


