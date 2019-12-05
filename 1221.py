import sys

def f(s):
    res = 0
    c = 0
    for i in s:
        if i == 'R':
            c += 1 
            if c == 0:
                res += 1
        else:
            c -= 1
            if c == 0:
                res += 1
    return res

s = sys.argv[1]
print(f(s))

