
class Solution:
    def detectCapitalUse(self, word):
        case1 = word.islower()
        case2 = not word[0].islower() and word[1:].islower()
        case3 = len([ w for w in word if w.islower()]) == 0

        return case1 or case2 or case3
