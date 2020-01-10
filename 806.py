
class Solution:
    def numberOfLines(self, widths, S):
        d = dict(zip([chr(_) for _ in range(97,123)], widths))
        lines = 1
        currsum = 0
        i, n = 0, len(S)
        while i < n:
            currsum += d[S[i]]
            if currsum > 100:
                lines += 1
                currsum = 0
            else:
                i += 1
        return [lines, currsum]
