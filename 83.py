
class LinkNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        res = LinkNode('x')
        res_cur = res
        check_cur = head

        while check_cur:
            if check_cur.val == res_cur.val:
                check_cur = check_cur.next
            else:
                res_cur.next = check_cur
                check_cur = check_cur.next
                res_cur = res_cur.next

        res_cur.next = None

        return res.next

