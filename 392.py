
import sys

class Solution:
    def isSubsequence(self, s, t):
        i, j, m, n = 0, 0, len(s), len(t)

        while i < m and j < n:
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j +=1

        if i == m:
            return True
        else:
            return False

if __name__ == '__main__':

    s, t = sys.argv[1:3]
    print(Solution().isSubsequence(s,t))
