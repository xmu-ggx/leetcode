import sys
class Solution:
    def freAlphabets(self, s):
        alphabets = [chr(i) for i in range(97, 123)]
        values = [str(i) for i in range(1, 10)] + [str(i)+'#' for i in range(10, 27)]
        hashtable = dict(zip(values, alphabets))
        print(hashtable)
        res, i, n = '', 0, len(s)
        while i < n:
            if i+2 < n and s[i+2] == '#':
                res += hashtable[s[i:i+3]]
                i += 3
            else:
                res += hashtable[s[i]]
                i += 1
        return res
if __name__ == '__main__':
    s = sys.argv[1]
    print(Solution().freAlphabets(s))
