import sys
class Solution:
    def validPalindrome(self, s):
        if self.isValidPalindrome(s):
            return True
        else:
            if self.isValidPalindrome(s[1:]):
                return True
            if self.isValidPalindrome(s[:-1]):
                return True
            else:
                for i in range(1, len(s)-1):
                    if self.isValidPalindrome(s[:i] + s[i+1:]):
                        return True
        return False


    def isValidPalindrome(sef, s):
        i, j = 0, len(s) -1

        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True

if __name__ == '__main__':
    test = sys.argv[1]
    print(Solution().validPalindrome(test))
