
class Solution:
    def partition(self, head, x):
        minlist = curmin = ListNode(0)
        maxlist = curmax = ListNode(0)

        while head:
            if head.val < x:
                curmin.next = head
                curmin = curmin.next
            else:
                curmax.next = head
                curmax = curmax.next

            head = head.next
        curmin.next = maxlist.next
        curmax.next = None
        return minlist.next
