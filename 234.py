
class Solution:
    def isPalindrome(self, head):
        res = []
        while head is not None:
            res.append(head.val)
            head = head.next
        return res == res[::-1]
