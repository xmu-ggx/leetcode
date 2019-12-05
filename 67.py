import sys

class Solution:
    def plusOne(self,s):
        i, status, res = len(s)-1, 1, ''
        
        while i >= 0:
            temp = int(s[i]) + status
            
            if temp == 2:
                res += '0'
                status = 1
            else:
                res += str(temp)
                status = 0

            i -= 1
        
        if status:
            res += '1'

        return res

    def addBinary(self,a,b):
        i, j, status = len(a)-1, len(b)-1, 0
        res = ''

        while i >= 0 and j >=0 :

            temp = int(a[i]) + int(b[j]) + status

            if temp >= 2 :
                res += str(temp % 2)
                status = 1
            else:
                res += str(temp)
                status = 0

            i -= 1
            j -= 1
        
        if i == j:
            if status == 1:
                res += '1'
        else:
            print(i,j,status) 
            if status == 1:

                if i > j:
                    res += self.plusOne(a[:i+1])
                elif i < j:
                    res += self.plusOne(b[:j+1])
            else:
                if i > j:
                    res += a[:i+1][::-1]
                elif i < j:
                    res += b[:j+1][::-1]


        return res[::-1]



if __name__ == '__main__':

    a,b = sys.argv[1:]
    print(Solution().addBinary(a,b))
