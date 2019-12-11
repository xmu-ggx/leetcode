
class Solution:
    def thirdMax(self, nums):
        first, second, third = 0, 0, 0
        for num in nums:
            if num in (first, second, third):
                continue
            if num > first:
                third, second, first = second, first, num
            elif num > second:
                third, second = second, num
            elif num > third:
                third = num

        return third if third != 0 else first

if __name__ == '__main__':
    test_nums = [3,2,1,5,8,3,8,6]
    print(Solution().thirdMax(test_nums))
