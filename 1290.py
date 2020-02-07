
class Solution:
    def getDecimalValue(self, head):
        res = 0
        cur = head
        ls = []
        while cur:
            ls.append(cur.val)
            cur = cur.next
        while ls:
            temp = ls.pop(0)
            res += 2**len(ls)*temp
        return res
        
