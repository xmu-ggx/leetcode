
class Solution:
    def uniquePaths(self, m, n):
        target_arr = [[0 for _ in range(n+1)] for _ in range(m+1)]
        target_arr[0][1] = 1
        for i in range(1, m+1):
            for j in range(1, n+1):
                target_arr[i][j] = target_arr[i][j-1] + target_arr[i-1][j]
        return target_arr[-1][-1]
        
        
