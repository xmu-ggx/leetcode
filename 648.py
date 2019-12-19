
class Solution:
    def replaceWords(self, dict, sentence):
        dict.sort(key=len)

        def judge(word):
            for prefix in dict:
                if word.startswith(prefix):
                    return prefix
            return word
        return ' '.join(judge(x) for x in sentence.split(' '))
