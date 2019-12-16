import sys

class Solution:
    def compress(self, chars):

        i, n, res = 0, len(chars), []

        while i < n-1:

            num = 0
            while i < n-1 and chars[i+1] == chars[i]:
                num += 1
                i += 1

            if num == 0:
                res.append(chars[i])
            else:
                res.append(chars[i])
                res.append(str(num+1))
            i += 1

        return res, len(res)
            



if __name__ == "__main__":

    test_chars = sys.argv[1]
    print(Solution().compress(test_chars))

