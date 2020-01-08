
class Solution:
    def commonChars(self, A):
        dict_list = []
        res = []
        for i in range(len(A)):
            name = 'dict_' + str(i)
            locals()[name] = {}
            
            dict_ = eval(name)
            for item in A[i]:
                if item in dict_:
                    dict_[item] += 1
                else:
                    dict_.update({item:1})
            dict_list.append(dict_)
        
        for elem in dict_list[0]:
            status = min(dict_list[i].get(elem, 0) for i in range(len(dict_list)))
            if status:
                for x in range(status):
                    res.append(elem)
        return res

if __name__ == '__main__':
    test_data = ['abc', 'bcd', 'cde']
    result = Solution().commonChars(test_data)
    print(result)
    for d in result:
        print(d)

