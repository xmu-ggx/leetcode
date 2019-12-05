import sys

class Solution:
    def mySqrt(self,x):

        if x == 1 : return 1

        l, r = 0, x
        while l < r-0.001:
            mid = (l+r)/2
            if mid * mid > x:
                r = mid
            elif mid * mid < x:
                l = mid
            else:
                return int(mid)
        print(l,r)

        return int(r) if int(r) **2 == x else int(l)


if __name__ == '__main__':
    x = int(sys.argv[1]) 
    print(Solution().mySqrt(x))
    
