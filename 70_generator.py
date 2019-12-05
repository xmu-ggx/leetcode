import sys

class Solution:
    def climbStairs(self, n):
        
        if n == 1:
            return 1
        if n == 2:
            return 2

        i, a, b = 1, 1, 2
        while  i < n:
            yield b
            a, b = b, a+b
            i += 1



if __name__ == '__main__':
    n = int(sys.argv[1])
    print(list(Solution().climbStairs(n)))
