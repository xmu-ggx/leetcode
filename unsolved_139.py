
class Solution:
    def wordBreak(self, s, wordDict):
        while s:
            n = len(s)
            for item in wordDict:
                if s.startswith(item):
                    s = s[len(item):]

            if len(s) == n: return False
        return True
