
class Solution:
    def twoSum(self, nums, target):
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                return [d[nums[i]], i]
            else:
                d.update({target-nums[i]})
