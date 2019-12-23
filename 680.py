import sys
class Solution:
    def validPalindrome(self, s):

        isValidPalindrome = lambda x : x == x[::-1]

        left, right = 0, len(s) - 1

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                if isValidPalindrome(s[left+1:right+1]) or isValidPalindrome(s[left:right]):
                    return True
                else:
                    return False
        return True

if __name__ == '__main__':
    test = sys.argv[1]
    print(Solution().validPalindrome(test))

