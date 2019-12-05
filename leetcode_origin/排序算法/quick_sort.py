# -*- coding: utf-8 -*-


# 快速排序是冒泡排序的一种改进；
#它的基本思想是：通过一趟排序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比另外一部分的所有数据都要小，然后再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行，以此达到整个数据变成有序序列。



def quick_sort(alist):
    
    if len(alist) <= 1:
        return alist
    
    midvalue = alist[len(alist) // 2]
    
    left = []
    mid = []
    right = []
    for i in alist:
        if i < midvalue:
            left.append(i)
        elif i == midvalue:
            mid.append(i)
        else:
            right.append(i)
    
    return quick_sort(left) + mid +quick_sort(right)




if __name__ == '__main__' :
    
    import numpy as np
    m = np.random.randint(1,100,60)
    print(quick_sort(m))




















