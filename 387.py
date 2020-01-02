
class Solution:
    def firstUniqChar(self, s):
        res = {}
        for item in s:
            if item in res:
                res[item] += 1
            else:
                res.update({item:1})
        for i in res:
            if res[i] == 1:
                return s.index(i)
        return -1
