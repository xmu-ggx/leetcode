
class Solution:
    def singleNumber(self, nums):
        res = 0
        for num in nums:
            res ^= num

        return res



if __name__ == '__main__':

    im = [2,2,1]
    print(Solution().singleNumber(im))
