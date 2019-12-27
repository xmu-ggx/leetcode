
class Solution:
    def findNumbers(self, nums):
        res = 0
        for item in nums:
            temp = len(str(item))
            if temp % 2 == 0: res +=1
        return res
