import sys

class Solution:
    @classmethod
    def lengthOfLastWord(cls, s):
        return len(s.strip().split(' ')[-1])


if __name__ == '__main__':
    s = sys.argv[1]
    print(Solution.lengthOfLastWord(s))
