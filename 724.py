
class Solution:
    def pivotIndex(self, nums):
        total_sum = sum(nums)
        temp_sum = 0

        for i in range(1, len(nums)):
            temp_sum += nums[i-1]
            if temp_sum == (total_sum - nums[i])//2:
                return i
        return -1

