
class Solution:
    def subSets(self, nums):
        res = [[]]
        
        for num in nums:
            for i in range(len(res)):
                temp = res[i].copy()
                temp.append(num)
                res.append(temp)
        return res
