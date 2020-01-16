
class Solution:
    def longestWord(self, words):
        words.sort()
        res = ''
        status = 0
        temp = ['']

        for w in words:
            if w[:-1] in temp:
                temp.append(w)
                if len(w) > status:
                    status = len(w)
                    res = w
        return res

