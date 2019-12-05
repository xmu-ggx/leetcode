# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 19:19:06 2019

@author: 2220170898
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(l1, l2):  

    head = cur = ListNode(0)
    count = 0

    while l1 and l2:
        s = l1.val + l2.val + count 

        if s >= 10:
            count = 1
            cur.next = ListNode(s % 10)
        else:
            count = 0
            cur.next = ListNode(s)

        cur = cur.next
        l1 = l1.next
        l2 = l2.next

    if not count :  # count 是0
        cur.next = l1 if l1 else l2
        
    else:  # count 是1的情况
        
        if l1:
            while l1:
                x = l1.val + count
                
                if x >= 10:
                    count = 1
                    cur.next = ListNode(x%10)
                    l1 = l1.next
                    cur = cur.next
                else:
                    count = 0
                    cur.next = ListNode(x)
                    cur.next.next = l1.next
                    break
            if count:
                cur.next = ListNode(1)
        elif l2:
            while l2:
                y = l2.val + count
                if y >= 10:
                    count = 1
                    cur.next = ListNode(y%10)
                    l2 = l2.next
                    cur = cur.next
                else:
                    count = 0
                    cur.next = ListNode(y)
                    cur.next.next = l2.next
                    break
            if count:
                cur.next = ListNode(1)
            


        else:
            cur.next = ListNode(1) 

    return head.next





def list_tolinklist(l):
    
    head = cur = ListNode(0)
    for i in l:
        cur.next = ListNode(i)
        cur = cur.next
    return head.next
        

l1 = list_tolinklist([2,4,3])
l2 = list_tolinklist([5,6,4])












 
        
