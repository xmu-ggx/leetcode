# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 17:01:21 2019

@author: 2220170898
"""

def search( nums, target):
    
    if len(nums) == 1:
        return 0 if target == nums[0] else -1

    
    n = len(nums)
    
    start = 0
    end = n-1
    if nums[start] == target:
        return start
    elif nums[end] == target:
        return end
    else:
        while start != end -1 :
        
            mid = (start+end) // 2
            
            if nums[mid] > target:
                end = mid
            elif nums[mid] < target:
                start = mid
            else:
                return mid
            
        return -1


