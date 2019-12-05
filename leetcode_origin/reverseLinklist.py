# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 14:17:18 2019

@author: 2220170898
"""
# 使用栈的结构

class ListNode:
    def __init__(self , x):
        self.val = x
        self.next = None
        
def reverseLinkList(head):
    
    rel = cur = ListNode(0)
    l = []
    
    while head:
        l.append(head)
        head = head.next
        
    while l:
        cur.next = l.pop()
        cur = cur.next
        
    cur.next = None
        
    return rel.next




















