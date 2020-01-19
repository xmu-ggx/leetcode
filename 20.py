
class Solution:
    def isValid(self, s: str) -> bool:

        if s == '':
            return True

        left = '([{'
        right = ')]}'
        l = []

        for i in s:
            if i in left:
                l.append(i)
            else:
                try:
                    
                    if right.index(i) == left.index(l.pop()):
                        continue
                    else:
                        return False
                    
                except IndexError:
                    return False

        return True if not l else False
