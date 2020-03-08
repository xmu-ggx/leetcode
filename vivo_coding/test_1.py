import sys
'''
1+2+2+3+3+3+4+  ... 求和，形参代表上诉数字的个数。
'''
def solution(n):
    res  = 0
    status = 0
    status_i = 0
    count = 0

    while count < n:
        if status_i < status:
            res += status
            print(status)
            status_i += 1
            count += 1
        else:
            status += 1
            status_i = 0
    return res

if __name__ == '__main__':
    m = int(sys.argv[1])
    print(solution(m))
