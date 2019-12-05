
class Solution:

    @classmethod
    def searchInsert(cls,nums,target):
        if target <= nums[0]:
            return 0
        if target == nums[-1]:
            return len(nums)-1
        if target > nums[-1]:
            return len(nums)

        l,r = 0,len(nums)-1

        while l < r-1:
            m = int((l+r)/2)
            if nums[m] > target:
                print(m)
                r = m
            elif nums[m] == target:
                print(m)
                return m
            else:
                nums[m] < target
                print(m)
                l = m
        return r

if __name__ == '__main__':
    nums = [1,3,5]
    target = 14
    print(Solution.searchInsert(nums,target))
