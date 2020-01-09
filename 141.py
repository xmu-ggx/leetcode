
class Solution:
    def hasCycle(self, head):
        if head is None:
            return False
        quick, slow = head, head
        while quick:
            try:
                quick = quick.next.next
                slow = slow.next
            except AttributeError:
                return False

            if quick == slow:
                return True
