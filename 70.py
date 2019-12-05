import sys

class Solution:
    def climbStairs(self, n):

        if n == 1:
            return 1
        if n == 2:
            return 2

        res = [0,1,2]

        i = 3
        while i < n + 1: 
            res.append(res[i-1]+res[i-2])
            i += 1
        return res[-1]



if __name__ == '__main__':
    n = int(sys.argv[1])
    print(Solution().climbStairs(n))
