
class Solution:
    @classmethod
    def plusOne(cls,digits):
        
        status, i = 0, len(digits)-1
        res = []

        while i >=0 :
            temp = digits[i] + 1 
            
            if temp < 10:
                res.append(temp)
                break
            else:
                res.append(0)
                i -= 1

        return [1] + res[::-1] if i == -1 else digits[:i] + res[::-1]

if __name__ == '__main__':

    digits = [8,9,9]
    print(digits)
    print(Solution.plusOne(digits))
