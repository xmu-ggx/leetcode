# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 13:43:40 2019

@author: 2220170898
"""


# 考虑用栈结构实现
# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def reverseKGroup( head, k ) :
    
    resl = cur = ListNode(0)
    l = []
    
    while head:
        
        for i in range(k):
            if head:
                l.append(head)
                head = head.next
            else:
                break
        if len(l) == k :
            
            for j in range(len(l)):
                cur.next = l.pop()
                cur = cur.next
        else:
            for j in l:
                cur.next = j
                cur = cur.next
            
    cur.next = None  # 需要注意一下
    
                
    return resl.next
        
   





     
        