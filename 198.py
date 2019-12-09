import sys

class Solution:
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        
        res_list = [nums[0], max(nums[0], nums[1])]
        res = 0

        for i in range(2, len(nums)):
            current_max = max(res_list[i-1], res_list[i-2]+nums[i])
            if current_max > res: res = current_max
            res_list.append(current_max)
        return res  

if __name__ == '__main__':
    nums = [int(x) for x in sys.argv[1:]]
    print(Solution().rob(nums))
