
class Solution:
    def findOcurrence(self, text, first, second):
        text_ls = text.split()
        res = []
        for i in range(len(text_ls)-2):
            if text_ls[i] == first and text_ls[i+1] == second:
                res.append(text_ls[i+2])
        return res
