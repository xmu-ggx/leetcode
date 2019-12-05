# -*- coding: utf-8 -*-
"""
Created on Thu May  2 11:50:35 2019

@author: GGX
"""

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    dic = {}
    
    for i in range(len(nums)):
        
        if nums[i] in dic:
            return (dic[nums[i]] , i)
        else:
            dic.update({target-nums[i] : i})
        
    
    
    
    
    
    
if __name__ == '__main__':
    
    nums = [2, 7, 11, 15]
    target = 9
    print(twoSum(nums , target))
       
    
    
    
    
    
    
    
    
    
    
    