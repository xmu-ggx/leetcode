from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):
        hashtable = defaultdict(list)
        for _ in strs:
            hashtable[''.join(sorted(_))].append(_)
        return hashtable.values()


