
class Solution:
    def permute(self, nums):
        res, n = [], len(nums)

        def recurise(answer=[]):
            if len(answer) == n:
                res.append(answer)
                return
            for item in nums:
                if item in answer:
                    continue
                else:
                    recurise(answer+[item])

        recurise()

        return res

if __name__ == '__main__':
    test = [1, 2, 3]
    print(Solution().permute(test))
