# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 20:55:32 2019

@author: 2220170898

"""




# 最长求公共前后缀个数

def pre_num(p):
    
    n = len(p)
    mmax = 0
    m = n // 2 +1 if n%2 else n/2
    m = int(m)
    
    for i in range(m):
        if p[:i+1] == p[-1-i:]:
            if i+1 > mmax:
                mmax = i+1
    return mmax
        


# 造表
def prefix_table(p):
    
    l = [0]
    
    for i in range( 1 , len(p)):
        
        if p[i] == p[l[-1]]:
            
            l.append(l[-1]+1)
            
        else:
            l.append(pre_num(p[:i+1]))
            
    return l

# kmp 算法匹配字符串

def search(s , p):
    
    m = len(s)
    n = len(p)
    ini = 0
    
    l = prefix_table(p)
    
    for i in range(m-n+1):
        
        j = ini
        
        while j < n :
            
            if s[i+j] != p[j]:
                
                ini = l[j-1]
                print( ' default' )
                print(i)
                
                break
                
            j += 1
            
        if j < n:
            continue
        else:
            print('success')
            return i , s[i:i+n]
            
    

    
    
s = 'ababcabaad'
p = 'aad'   
search(s,p)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
