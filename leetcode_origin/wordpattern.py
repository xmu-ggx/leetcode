# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 17:15:16 2019

@author: 2220170898
"""


def wordPattern( p , s ):

    dic = {}

    tmp = []

    l = s.split( sep = ' ' )
    
    if len(p) != len(l):
        return False
    if len(set(p)) != len(set(l)):
        return False   # 一一映射关系的必要条件


    for i in range(len(p)):

        if p[i] not in tmp :
            
            dic.update({p[i] : l[i]})
            tmp.append(p[i])
        else:
            
            if dic[p[i]] != l[i]:

                return False
    
    return True
            
    
    
    
    
    
    
   






















