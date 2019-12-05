# -*- coding: utf-8 -*-
"""
Created on Wed May  1 14:58:32 2019

@author: GGX
"""

# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



def partition(head , x):
    
    minlist = curmin = ListNode(0)
    maxlist = curmax = ListNode(0)
    
    cur = head
    
    while cur:
        
        if cur.val < x:
            curmin.next = cur
            curmin = curmin.next
        else:
            curmax.next = cur
            curmax = curmax.next
            
        cur = cur.next
        
    curmax.next = None  # 保证链表结尾是空
    
    curmin.next = maxlist.next  # 连接两部分链表(最小值和最大值链表)
    
    return minlist.next
        
        
if __name__ == '__main__':
      
    l = [1,4,3,2,5,2] 
    nodes = [ListNode(i) for i in l ] 
    
    for j in range(len(l)-1):
        nodes[j].next = nodes[j+1]
        
    head = nodes[0]
           
    cur = partition(head , 3)        
    while cur:
        print(cur.val)
        cur = cur.next       
        
        
        
        
        
        
        