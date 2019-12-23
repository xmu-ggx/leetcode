
class Solution:
    def nthUglyNumber(self, n):
        res = [1]
        idx2, idx3, idx5 = 0, 0, 0
        while len(res) < n:
            if res[idx2]*2 <= res[-1]:
                idx2 += 1
            if res[idx3]*3 <= res[-1]:
                idx3 += 1
            if res[idx5]*5 <= res[-1]:
                idx5 += 1
            curr = min(res[idx2]*2, res[idx3]*3, res[idx5]*5)
            res.append(curr)
        return res[-1]

if __name__ == '__main__':
    print(Solution().nthUglyNumber(10))
