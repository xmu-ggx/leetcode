
class Solution:
    def peakIndexInMoutainArray(self, A):
        n = len(A)

        for i in range(n-1):
            if A[i+1] < A[i]:
                return i


