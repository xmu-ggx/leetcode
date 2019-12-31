
class Solution:
    def numPairDivisibleBy60(self, time):
        res = 0
        res_dict = {}
        modify_time = [x%60 for x in time]

        for item in modify_time:
            if item in res_dict:
                res_dict[item] += 1
            else:
                res_dict.update({item:1})

        for i in range(31):
            if i in [0, 30]:
                temp = res_dict.get(i, 0)
                res += temp * (temp-1) // 2

            elif i in res_dict:
                temp = res_dict[i] * res_dict.get(60-i, 0)
                res += temp
        
        return res

