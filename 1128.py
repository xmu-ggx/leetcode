
class Solution:
    def numEquivDominoPairs(self, dominoes):
        counts = [0]*89
        res = 0
        for item in dominoes:
            i, j  = item
            if i > j:
                i, j = j, i
            counts[10*i+j-11] += 1
        for count in counts:
            if count > 1:
                res += count*(count+1)/2
        return int(res)

