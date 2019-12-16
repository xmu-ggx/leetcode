import re
import sys

class Solution:
    def countSegments(self, s):
        temp = re.split(r'[ ]+', s)
        res = 0
        for item in temp:
            if item != '':
                res += 1
        return res

if __name__ == '__main__':
    test_str = sys.argv[1]
    print(Solution().countSegments(test_str))
