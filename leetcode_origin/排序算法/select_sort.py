# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 12:45:50 2019

@author: 2220170898
"""

# 思想：每一轮选择一个最小的元素放在前面排序好的后面；原地排序
# 性能：O(n^2) 

def select_sort(alist):
    
    n = len(alist)
    
    for i in range(n):
        
        for j in range(i+1,n):
            
            if alist[j] < alist[i]:
                
                alist[i] , alist[j] = alist[j] , alist[i]
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                