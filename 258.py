
class Solution:
    def addDigits(self, num):
        if num < 10: return num
        while num >= 10:
            sum_ = 0
            while num:
                sum_ += num%10
                num //= 10
            if sum_ >= 10:
                num = sum_
            else:
                return sum_
