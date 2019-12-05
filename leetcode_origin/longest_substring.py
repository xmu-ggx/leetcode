#!/user/bin/env python
#coding:utf-8
"""
Spyder Editor

This is a temporary script file.
2019.3.1

"""

    
# 动态规划： 网格法（二维数组进行标记）求取最长公共子串 
#  mmax 记录长度 ， p 记录位置   

def longest_substring( s1 , s2 ):
    
    m = len(s1)
    n = len(s2)
    
    # 生成二维全0 数组
    l = [ [0 for j in range(len(s2))] for i in range(len(s1)) ]
    mmax = 0   
    
    for j in range(n):
        if s2[j] == s1[0]:
            mmax = 1
            p = 0
    for i in range(m):
        if s1[i] == s2[0]:
            mmax = 1
            p = i
    
    for i in range(1,m):
        for j in range(1,n):
            
            if s1[i] == s2[j]:
            
                l[i][j] = l[i-1][j-1] + 1
                if l[i][j] > mmax:
                    mmax = l[i][j]
                    p = i
                    
    return mmax , s1[p+1-mmax :p+1]
                    


s1 = "aacdefcaa"
s2 = s1[::-1]
longest_substring(s1 , s2)







