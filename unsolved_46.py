
class Solution:
    def permute(self, nums):
        
        def recursive(nums):
            if len(nums) == 1:
                return nums
            for i in range(len(nums)):
                temp = recursive(nums[:i]) + nums[i] + recursive(nums[i:])
                print(temp)


if __name__ == '__main__':

    test_data = [1,2,3]
    print(Solution().permute(test_data))
