
class Solution:
    def isHappy(self, n):
        got = set()

        while n !=1 and n not in got:
            got.add(n)
            sum_ = 0
            while n:
                sum_ += (n%10)**2
                n //=10
            n = sum_

        return n == 1
