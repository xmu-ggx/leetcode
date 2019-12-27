
class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead
        """
        for i in range(k):
            n = len(nums) - 1
            while n >= 1:
                nums[n-1], nums[n] = nums[n], nums[n-1]
                #print(nums)
                n -= 1
            
        return nums

if __name__ == '__main__':
    test_nums = [1,2,3,4,5]
    print(Solution().rotate(test_nums, 2))
