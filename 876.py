import sys

class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None

class Solution:
    def middleNode(self,head):
       fast,slow = head,head
       while fast and fast.next:
           fast = fast.next.next
           slow = slow.next
        
        return slow
