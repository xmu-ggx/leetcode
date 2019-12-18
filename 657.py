class Solution:
    def judgeCircle(self,moves):
        i, j = 0, 0
        for item in moves:
            if item == 'U':
                i += 1
            elif item == 'D':
                i -= 1
            elif item == 'L':
                j += 1
            else:
                j -= 1
        return i==0 and j==0
