
class Solution:
    def findWords(self, words):
        res = []
        d = {}
        linelist = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
        for num, line in enumerate(linelist, 1):
            for letter in line:
                d.update({letter:num})
        
        for word in words:
            status = d[word[0].lower()]
            for i in range(len(word)):
                if d[word[i].lower()] != status:
                    break

            if i == len(word)-1 and d[word[i].lower()] == status:
                res.append(word)
            else:
                continue
        return res

