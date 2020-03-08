import  sys

'''
给定一个数字n（大于9），找到最小的数字m，使得m的各个位置上数字的乘积为n。
如果没有，则输出 -1 。
'''

def Solution(n):
    number = len(str(n)) 
    edge = int(str(9)*number)
    for i in range(1,edge+1):
        if mul(i) == n:
            return i
    return -1

def mul(m):
    res = 1
    while m:
        res *= m % 10
        m //= 10
    return res
    

if __name__ == '__main__':

    n = int(sys.argv[1])
    print(Solution(n))

