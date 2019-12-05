import numpy as np
import sys
import re


def f(n,m,indices):

    res = 0
    matrix = np.zeros(shape=(n,m))
    for index in np.array(indices):
        row, col = index
        matrix[row] += 1
        matrix[:,col] += 1

    for i in range(n):
        for j in range(m):
            if matrix[i,j] % 2 != 0:
                res += 1 
    return res, matrix

args = sys.argv[1:]
n = int(args[0])
m = int(args[1])

p = re.compile(r'[\[\],]')
s = list(map(int, [x for x in p.split(args[2]) if x != '']))
indices = np.array(s).reshape((int(len(s)/2),2))

print(f(n,m,indices))
