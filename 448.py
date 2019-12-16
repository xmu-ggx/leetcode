
class Solution:
    def findDisappearedNumbers(self, nums):
        new_nums = [-1 for i in range(len(nums))]
        nums.sort()
        res = []

        for item in nums:
            new_nums[item-1] = 0

        for idx in range(len(nums)):
            if new_nums[idx] == 0:
                res.append(idx+1)

        return res

