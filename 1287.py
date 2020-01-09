
class Solution:
    def findSpecialInteger(self, arr):
        i, j, n = 0, 0, len(arr)
        while j < n:
            while arr[j] == arr[i]: 
                j += 1
                if j == n:
                    break

            if (j-i)/n > 0.25:
                return arr[i]
            else:
                i = j
