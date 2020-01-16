
class Solution:
    def majorityElement(self, nums):
        idx = len(nums) // 2
        nums.sort()
        return nums[idx]
