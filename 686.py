
class Solution:
    def repeatedStringMatch(self, A, B):
        try_times = len(B) // len(A) + 3
        for i in range(1,try_times):
            if B in A*i:return i
        return -1

