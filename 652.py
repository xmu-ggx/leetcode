
class Solution:
    def findDuplicateSubtrees(self, root):
        if root is None:
            return []
        queue = [root]
        res = []
        search_list = {}
        while queue:
            node = queue.pop(0)
            temp = self.dlr_search(node)
            freq = search_list.get(temp,0)
            if freq == 1:
                res.append(node)
                search_list[temp] += 1
            elif freq == 0:
                search_list.update({temp:1})
            else:
                search_list[temp] += 1
            if node.left is not None: queue.append(node.left)
            if node.right is not None: queue.append(node.right)
        return res



    def dlr_search(self, root):
        if root is None:
            return ''

        stack = [root]
        res = ''
        while stack:
            node = stack.pop()
            if node is None:
                res += 'x'
                continue
            else:
                res += str(node.val)

            if node.left is None and node.right is None:
                continue
            else:
                stack.append(node.right)
                stack.append(node.left)
        return res
