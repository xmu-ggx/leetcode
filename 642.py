
class Solution:
    def __init__(self):
        self.fre_list = []

    def topKFrequent(self, words, k):
        hashtable = {}
        for word in words:
            if word in hashtable:
                hashtable[word] += 1
            else:
                hashtable[word] = 1

        res_dic = {}
        for word, fre in hashtable.items():
            if fre in res_dic:
                res_dic[fre].append(word)
            else:
                res_dic[fre] = [word]
                self.fre_list.append(fre)
        self.fre_list.sort(reverse=True)

        res = []
        count = 0
        for i in self.fre_list:
            ls = res_dic[i]
            ls.sort()
            for i in range(len(ls)):
                if count < k:
                    res.append(ls[i])
                    count += 1
        return res


if __name__ == '__main__':
    test = ["i", "love", "leetcode", "i", "love", "coding"]
    Solution().topKFrequent(test,0)
