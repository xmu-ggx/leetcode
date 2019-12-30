import sys
class Solution:

    def longestCommonSubsequence(self, text1, text2):

        i, j, m, n =0, 0, len(text1), len(text2)

        if  m == 0 or n == 0:
            return 0

        while i < m or j < n:
            if text1[i] == text2[j]:
                return self.longestCommonSubsequence(text1[i+1:], text2[j+1:]) + 1
            else:
                return max(self.longestCommonSubsequence(text1[i+1:], text2), self.longestCommonSubsequence(text1, text2[j+1:]))

if __name__ == '__main__':
    test1, test2 = sys.argv[1:3]
    print(Solution().longestCommonSubsequence(test1, test2))
