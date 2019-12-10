
class Solution:
    def findMin(self, nums):
        if len(nums) == 1:
            return nums[0]

        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                return nums[i]
        return nums[0]
