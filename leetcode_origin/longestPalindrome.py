# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 14:45:51 2019

@author: 2220170898
"""
# 扩散找回文数子串

def longestPalindrome( s: str) -> str:
    
    mmax = 0
    
    for k in range(len(s)-1):
            
        i = k
        j = k
        
        count = 0
        
        while k+count < len(s) and s[k] == s[k+count]:
            count += 1
        
        j += count 
        i -= 1
            
        while True:
            if i < 0 or j >len(s):
                break
            else:
                tmp = s[i:j+1]
                
                if tmp == tmp[::-1]:  # 反向切片不能直接作用到切片上
                    
                    i -= 1
                    j += 1
                    
                else:
                    break
                
        if j-i-1 > mmax:
            mmax = j-i-1
            p = i+1

    return s[p:p+mmax]
                
                
                
                

                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                