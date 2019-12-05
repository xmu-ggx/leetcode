# -*- coding: utf-8 -*-
"""
Created on Wed May  1 15:43:52 2019

@author: GGX
"""



# 判断链表是否有环思路：利用快慢指针进行判断


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None



def hasCycle(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    if head is None:
        return False
    
    quick_cur = slow_cur = head
    
    while slow_cur:
        
        try:   # 无环链表，quick_cur引发一个AttributeError 进行捕获
            
            slow_cur = slow_cur.next
            quick_cur = quick_cur.next.next
        
        except AttributeError :
            return False
        
        if slow_cur == quick_cur:
            return True
        
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    