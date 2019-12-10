
import re
import sys

class Solution:
    @classmethod
    def reverseWords(cls, s):

        return ' '.join(re.split(r'[ ]+', s.strip())[::-1])

if __name__ == '__main__':
    test_str = sys.argv[1]
    print(Solution.reverseWords(test_str))

