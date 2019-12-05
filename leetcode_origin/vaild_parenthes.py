# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 12:43:43 2019

@author: 2220170898
"""

def isValid(self, s: str) -> bool:
    
    left = '([{'
    right = ')]}'
    l = []
    
    if s == '' or s[0] in right:
        return False

    for i in range(len(s)):

        if s[i] in left:
            l.append(s[i])
        else:
            if right.index(s[i]) == left.index(l[-1]): 
                del l[-1]
            else:
                return False
    return True













