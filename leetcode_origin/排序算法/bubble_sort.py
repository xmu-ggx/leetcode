# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 11:49:59 2019

@author: 2220170898
"""

# 冒泡排序：
# 思想： 每一轮得到一个最小值放前面
# 性能： 时间复杂度： O(n^2); 原地排序
# 算法优化： 引入变量count，当某一轮没有选(相邻两个元素比较)出最小值，则意味着这一轮顺序是排列好了的。

def bubble_sort(alist):
       
    for j in range(len(alist) -1) :
    
        count = 0  # 引入变量count 对计算次数进行优化，发现不需要排序之后就停止
        
        for i in range(len(alist) -1 - j):
            
            if alist[i] > alist[i+1]:
                
                alist[i] , alist[i+1] = alist[i+1] , alist[i]
                count += 1
                
        if count == 0:
            return
            
            
            



























