import sys
import re

class Solution:
    def isPalindrome(self, s):
        pattern = re.compile(r'[A-Za-z0-9]')
        res = "".join([x.lower() for x in s if pattern.match(x)])
        print(res)
        return res == res[::-1]

if __name__ == "__main__":
    s = sys.argv[1]
    print(Solution().isPalindrome(s))


