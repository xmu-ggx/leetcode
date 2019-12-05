import sys

def f(s):

    cnt = 0
    previ = 0
    res = ''

    for index,item in enumerate(s):
        if item == '(':
            cnt += 1
        else:
            cnt -= 1
        
        if cnt == 0:
            res += s[previ+1:index]
            previ = index +1

    return res


if __name__ == '__main__':

    s = sys.argv[1]
    print(f(s))



