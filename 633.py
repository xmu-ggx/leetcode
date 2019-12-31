
class Solution:
    def judgeSquareSum(self,c):
        i, j = 0, int(c**0.5)
        while i <= j:
            temp = i**2 + j **2
            if temp < c:
                i += 1
            elif temp > c:
                j -= 1
            else:
                return True
        return False
