# -*- coding: utf-8 -*-
"""
Created on Thu May  2 12:06:16 2019

@author: GGX
"""

# 排序之后左右指针(双指针），注意对于重复值的筛选处理



    
def threeSum( nums):
    
    length = len(nums)
    resultList = []
    nums.sort()
    
    for i in range(0,length-2):
        
        j = i + 1
        k = length - 1
        
        while (j < k):
            
            sum0 = nums[i] + nums[j] + nums[k]
            
            if (sum0 == 0):
                result = []
                result.append(nums[i])
                result.append(nums[j])
                result.append(nums[k])
                if result not in resultList:
                    resultList.append(result)
                j +=1
                
            if (sum0 < 0):
                j +=1
            if (sum0 > 0):
                k -=1
                
    return resultList
        
        
        
        
      
if __name__ == '__main__' :
    nums = [-1, 0, 1, 2, -1, -4]
    print(threeSum(nums))            
            
            
       


            
            
            
            
            
            
            
            