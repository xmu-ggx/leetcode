
class Solution:
    def longestPalindrome(self, s):
        hashtable = {}
        for i in s:
            if i in hashtable:
                hashtable[i] += 1
            else:
                hashtable[i] = 1

        res = 0
        status = 0
        for key in hashtable:
            if hashtable[key]%2 == 0:
                res += hashtable[key]
            else:
                if hashtable[key] > 1:
                    res += (hashtable[key] - 1)
                    status = 1
                else:
                    status =1
        return res+status
